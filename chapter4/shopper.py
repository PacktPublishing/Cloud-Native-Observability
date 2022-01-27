#!/usr/bin/env python3
import requests

from opentelemetry import trace
from opentelemetry.propagate import inject
from opentelemetry.semconv.trace import HttpFlavorValues, SpanAttributes

from common import configure_tracer
from local_machine_resource_detector import LocalMachineResourceDetector


tracer = configure_tracer("shopper", "0.1.2")

@tracer.start_as_current_span("browse")
def browse():
    print("visiting the grocery store")
    with tracer.start_as_current_span(
        "web request", kind=trace.SpanKind.CLIENT
    ) as span:
        url = "http://localhost:5000/products"
        span.set_attributes(
            {
                SpanAttributes.HTTP_METHOD: "GET",
                SpanAttributes.HTTP_FLAVOR: HttpFlavorValues.HTTP_1_1.value,
                SpanAttributes.HTTP_URL: url,
                SpanAttributes.NET_PEER_IP: "127.0.0.1",

            }
        )
        headers = {}
        inject(headers)
        span.add_event("about to send a request")
        try:
            url = "invalid_url"
            resp = requests.get(url, headers=headers)
            span.add_event(
                "request sent",
                Attributes={"url": url},
                timestamp=0,
            )
            span.set_attribute(
                SpanAttributes.HTTP_STATUS_CODE,
                resp.status_code
            )
        except Exception as err:
            attributes = {
                SpanAttributes.EXCEPTION_MESSAGE: str(err),
            }
            span.add_event("exception", attributes=attributes)

    add_item_to_cart("orange", 5)

@tracer.start_as_current_span("add item to cart")
def add_item_to_cart(item, quantity):
    span = trace.get_current_span()
    span.set_attributes({
        "item": item,
        "quantity": quantity,
    })
    print("add {} to cart".format(item))

@tracer.start_as_current_span("visit store")
def visit_store():
    browse()


if __name__ == "__main__":
    visit_store()
