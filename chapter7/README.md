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

---

_Cloud Native Observability_
