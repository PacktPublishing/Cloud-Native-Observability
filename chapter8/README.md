# Chapter 8 examples

This folder contains examples for Chapter 8.

## Prerequisites

- Python 3.6+

## Setup

```
mkdir cloud_native_observability
python3 -m venv cloud_native_observability
source cloud_native_observability/bin/activate

# install packages

pip install opentelemetry-exporter-otlp

# download the collector

# Linux amd64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.43.0/otelcol-contrib_0.43.0_linux_amd64.tar.gz

# Linux arm64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.43.0/otelcol-contrib_0.43.0_linux_arm64.tar.gz

# MacOS amd64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.43.0/otelcol-contrib_0.43.0_darwin_amd64.tar.gz

# MacOS arm64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.43.0/otelcol-contrib_0.43.0_darwin_arm64.tar.gz

tar -xzf otelcol.tar.gz otelcol-contrib
./otelcol-contrib --version
```

## Receivers

Receivers included in the OpenTelemetry Core distribution.

|                      | Traces | Metrics | Logs |
| -------------------- | :----: | :-----: | :--: |
| Host Metrics         |        |   ✔️    |      |
| Jaeger               |   ✔️   |         |      |
| Kafka                |   ✔️   |   ✔️    |  ✔️  |
| OpenCensus           |   ✔️   |   ✔️    |      |
| OpenTelemetry (OTLP) |   ✔️   |   ✔️    |  ✔️  |
| Prometheus           |        |   ✔️    |      |
| Zipkin               |   ✔️   |         |      |

## Processors

Processors included in the OpenTelemetry Core distribution.

|                        | Traces | Metrics | Logs |
| ---------------------- | :----: | :-----: | :--: |
| Attributes             |   ✔️   |         |  ✔️  |
| Batch                  |   ✔️   |   ✔️    |  ✔️  |
| Filter                 |        |   ✔️    |  ✔️  |
| Memory Limiter         |   ✔️   |   ✔️    |  ✔️  |
| Probabilistic Sampling |   ✔️   |         |      |
| Resource               |   ✔️   |   ✔️    |  ✔️  |
| Span                   |   ✔️   |         |      |

## Exporters

Exporters included in the OpenTelemetry Core distribution.

|                      | Traces | Metrics | Logs |
| -------------------- | :----: | :-----: | :--: |
| File                 |   ✔️   |   ✔️    |  ✔️  |
| Jaeger               |   ✔️   |         |      |
| Kafka                |   ✔️   |   ✔️    |  ✔️  |
| Logging              |   ✔️   |   ✔️    |  ✔️  |
| OpenCensus           |   ✔️   |   ✔️    |      |
| OpenTelemetry (OTLP) |   ✔️   |   ✔️    |  ✔️  |
| Prometheus           |        |   ✔️    |      |
| Zipkin               |   ✔️   |         |      |

---

_Cloud Native Observability_
