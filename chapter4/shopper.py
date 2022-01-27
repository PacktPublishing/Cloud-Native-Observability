#!/usr/bin/env python3
from opentelemetry import context, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = SimpleSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer("shopper.py", "0.0.1")

def browse():
    print("visiting the grocery store")

def add_item_to_cart(item):
    print("add {} to cart".format(item))


if __name__ == "__main__":
    tracer = configure_tracer()
    with tracer.start_as_current_span("visit store"):
        with tracer.start_as_current_span("browse"):
            browse()
            with tracer.start_as_current_span("add item to cart"):
                add_item_to_cart("orange")
