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
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.44.0/otelcol-contrib_0.44.0_linux_amd64.tar.gz

# Linux arm64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.44.0/otelcol-contrib_0.44.0_linux_arm64.tar.gz

# MacOS amd64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.44.0/otelcol-contrib_0.44.0_darwin_amd64.tar.gz

# MacOS arm64
wget -O otelcol.tar.gz https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.44.0/otelcol-contrib_0.44.0_darwin_arm64.tar.gz

tar -xzf otelcol.tar.gz otelcol-contrib
./otelcol-contrib --version
```

---

_Cloud Native Observability_
