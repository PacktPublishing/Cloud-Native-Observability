from opentelemetry.sdk._logs import LogEmitterProvider, set_log_emitter_provider
from opentelemetry.sdk.resources import Resource

def configure_log_emitter_provider():
    provider = LogEmitterProvider(resource=Resource.create())
    set_log_emitter_provider(provider)