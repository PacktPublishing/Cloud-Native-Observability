import requests

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.instrumentation.requests import RequestsInstrumentor


def rename_span(method, url):
    return f"Web Request {method}"


def add_response_attributes(span, response):
    span.set_attribute("http.response.headers", str(response.headers))


def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = BatchSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)


configure_tracer()
RequestsInstrumentor().instrument(
    name_callback=rename_span,
    span_callback=add_response_attributes,
)


url = "https://www.cloudnativeobservability.com"
resp = requests.get(url)
print(resp.status_code)
