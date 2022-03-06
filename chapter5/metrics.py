from opentelemetry._metrics import get_meter_provider, set_meter_provider
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk._metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from prometheus_client import start_http_server


def configure_meter_provider():
    start_http_server(port=8000, addr="localhost")
    reader = PrometheusMetricReader(prefix="MetricExample")
    provider = MeterProvider(metric_readers=[reader], resource=Resource.create())
    set_meter_provider(provider)


if __name__ == "__main__":
    configure_meter_provider()
    meter = get_meter_provider().get_meter(
        name="metric-example",
        version="0.1.2",
        schema_url=" https://opentelemetry.io/schemas/1.9.0",
    )
    input("Press any key to exit...")
