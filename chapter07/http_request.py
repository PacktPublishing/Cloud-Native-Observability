import requests

from opentelemetry.instrumentation.requests import RequestsInstrumentor


def rename_span(method, url):
    return f"Web Request {method}"


def add_response_attributes(span, response):
    span.set_attribute("http.response.headers", str(response.headers))


RequestsInstrumentor().uninstrument()
RequestsInstrumentor().instrument(
    name_callback=rename_span,
    span_callback=add_response_attributes,
)

resp = requests.get("https://www.cloudnativeobservability.com")
print(resp.status_code)
