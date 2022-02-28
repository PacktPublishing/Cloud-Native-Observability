# Chapter 10 examples

This folder contains examples for Chapter 10.

## Prerequisites

- Python 3.6+
- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

## Setup

```
mkdir cloud_native_observability
python3 -m venv cloud_native_observability
source cloud_native_observability/bin/activate

pip install opentelemetry-distro \
              opentelemetry-exporter-jaeger \
              opentelemetry-exporter-zipkin

docker compose up
```

## Status of exporters for officially supported backend in OpenTelemetry Python

| Exporter   | Signal  | Status             |
| ---------- | ------- | ------------------ |
| Jaeger     | Tracing | Stable             |
| Zipkin     | Tracing | Stable             |
| Prometheus | Metrics | Active development |

---

_Cloud Native Observability_
