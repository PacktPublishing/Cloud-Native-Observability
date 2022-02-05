# Chapter 12 examples

This folder contains examples for Chapter 12.

## Prerequisites

- Python 3.6+

## Setup

```
mkdir cloud_native_observability
python3 -m venv cloud_native_observability
source cloud_native_observability/bin/activate

# install packages
pip install opentelemetry-distro \
            opentelemetry-exporter-otlp

pip freeze | grep opentelemetry

# download the collector

# Linux amd64
wget -O otelcol https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.40.0/otelcontribcol_linux_amd64

# Linux arm64
wget -O otelcol https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.40.0/otelcontribcol_linux_arm64

# MacOS amd64
wget -O otelcol https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.40.0/otelcontribcol_darwin_amd64

# MacOS arm64
wget -O otelcol https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.40.0/otelcontribcol_darwin_arm64

chmod +x ./otelcol
./otelcol --version
```

---

_Cloud Native Observability_
