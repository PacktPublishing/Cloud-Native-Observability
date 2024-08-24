#!/usr/bin/env python3
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = SimpleSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer("1.py", "0.0.1")

def browse():
    print("visiting the grocery store")

if __name__ == "__main__":
    tracer = configure_tracer()
    span = tracer.start_span("visit store")
    browse()
    span.end()