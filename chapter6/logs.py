from opentelemetry.sdk._logs.export import ConsoleLogExporter, BatchLogProcessor
from opentelemetry.sdk._logs import (
    LogEmitterProvider,
    get_log_emitter_provider,
    set_log_emitter_provider,
)
from opentelemetry.sdk.resources import Resource


def configure_log_emitter_provider():
    provider = LogEmitterProvider(resource=Resource.create())
    set_log_emitter_provider(provider)
    exporter = ConsoleLogExporter()
    provider.add_log_processor(BatchLogProcessor(exporter))


if __name__ == "__main__":
    configure_log_emitter_provider()
    log_emitter = get_log_emitter_provider().get_log_emitter(
        "shopper",
        instrumenting_module_verison="0.1.2",
    )
