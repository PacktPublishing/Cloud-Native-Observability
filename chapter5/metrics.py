from opentelemetry._metrics import set_meter_provider
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk.resources import Resource

def configure_meter_provider():
    provider = MeterProvider(resource=Resource.create())
    set_meter_provider(provider)

if __name__ == "__main__":
    configure_meter_provider()
