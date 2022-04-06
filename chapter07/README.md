# Chapter 7 examples

This folder contains examples for Chapter 7.

## Prerequisites

- Python 3.6

## Setup

```
mkdir cloud_native_observability
python3 -m venv cloud_native_observability
source cloud_native_observability/bin/activate

pip install opentelemetry-api \
              opentelemetry-sdk \
              opentelemetry-instrumentation \
              opentelemetry-propagator-b3 \
              opentelemetry-distro

pip install flask \
              opentelemetry-instrumentation-flask \
              requests \
              opentelemetry-instrumentation-requests
```

## OpenTelemetry Distro Implementations

- OpenTelemetry Distro: https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/opentelemetry-distro/
- Lightstep Launcher Distro: https://github.com/lightstep/otel-launcher-python/blob/main/src/opentelemetry/launcher/configuration.py
- Splunk Distro: https://github.com/signalfx/splunk-otel-python/blob/main/splunk_otel/distro.py
- Uptrace: https://github.com/uptrace/uptrace-python/blob/master/src/uptrace/distro.py

---

_Cloud Native Observability_
