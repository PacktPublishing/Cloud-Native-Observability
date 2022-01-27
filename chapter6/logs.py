import logging
import time
from opentelemetry.sdk._logs.export import ConsoleLogExporter, BatchLogProcessor
from opentelemetry.sdk._logs import (
    LogEmitterProvider,
    LogRecord,
    OTLPHandler,
    get_log_emitter_provider,
    set_log_emitter_provider,
)
from opentelemetry.sdk._logs.severity import SeverityNumber
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
    log_emitter.emit(
        LogRecord(
            timestamp=time.time_ns(),
            body="first log line",
            severity_number=SeverityNumber.INFO,
        )
    )
    logger = logging.getLogger(__file__)
    handler = OTLPHandler()
    logger.addHandler(handler)
    logger.warning("second log line")

