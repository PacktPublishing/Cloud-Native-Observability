import time
from opentelemetry import trace

tracer = trace.get_tracer_provider().get_tracer(__name__)
with tracer.start_as_current_span("slow-span"):
    time.sleep(1)

for i in range(0, 20):
    with tracer.start_as_current_span("fast-span"):
        pass
