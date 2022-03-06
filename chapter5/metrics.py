from opentelemetry._metrics import get_meter_provider, set_meter_provider
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk._metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
import time
from opentelemetry._metrics.measurement import Measurement

def async_counter_callback():
    yield Measurement(10)



def configure_meter_provider():
    exporter = ConsoleMetricExporter()
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
    provider = MeterProvider(metric_readers=[reader], resource=Resource.create())
    set_meter_provider(provider)


if __name__ == "__main__":
    configure_meter_provider()
    meter = get_meter_provider().get_meter(
        name="metric-example",
        version="0.1.2",
        schema_url=" https://opentelemetry.io/schemas/1.9.0",
    )
    # counter = meter.create_counter(
    #     "items_sold",
    #     unit="items",
    #     description="Total items sold"
    # )
    # counter.add(6, {"apple": 5, "orange": 1})
    # counter.add(1, {"chair": 1})

    # meter.create_observable_counter(
    #     name="major_page_faults",
    #     callback=async_counter_callback,
    #     description="page faults requiring I/O",
    #     unit="fault",
    # )
    # time.sleep(10)

    inventory_counter = meter.create_up_down_counter(
        name="inventory",
        unit="items",
        description="Number of items in inventory",
    )
    inventory_counter.add(20, {"apples": 10, "oranges": 5})
    inventory_counter.add(-5, {"apples": 5})

