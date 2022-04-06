#!/usr/bin/env python3
import logging
import requests
from opentelemetry import trace
from opentelemetry.sdk._logs import OTLPHandler

tracer = trace.get_tracer("shopper", "0.1.2")
logger = logging.getLogger("shopper")
logger.setLevel(logging.DEBUG)
logger.addHandler(OTLPHandler())


@tracer.start_as_current_span("add item to cart")
def add_item_to_cart(item, quantity):
    span = trace.get_current_span()
    span.set_attributes(
        {
            "item": item,
            "quantity": quantity,
        }
    )
    logger.info("add {} to cart".format(item))


@tracer.start_as_current_span("browse")
def browse():
    resp = requests.get("http://localhost:5000/products")
    add_item_to_cart("orange", 5)


@tracer.start_as_current_span("visit store")
def visit_store():
    browse()


if __name__ == "__main__":
    visit_store()
