from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.trace.sampling import ALWAYS_OFF, ALWAYS_ON, TraceIdRatioBased

def configure_tracer(sampler):
    provider = TracerProvider(sampler=sampler)
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    return provider.get_tracer(__name__)

always_on_tracer = configure_tracer(ALWAYS_ON)
always_off_tracer = configure_tracer(ALWAYS_OFF)
ratio_tracer = configure_tracer(TraceIdRatioBased(0.5))

with always_on_tracer.start_as_current_span("always-on") as span:
    span.set_attribute("sample", "always sampled")

with always_off_tracer.start_as_current_span("always-off") as span:
    span.set_attribute("sample", "never sampled")

with ratio_tracer.start_as_current_span("ratio") as span:
    span.set_attribute("sample", "sometimes sampled")
