# Chapter 9 examples

This folder contains examples for Chapter 9.

## Prerequisites

- Docker (https://docs.docker.com/get-docker/)
- kubectl (https://kubernetes.io/docs/tasks/tools/)
- Kind (https://kind.sigs.k8s.io/docs/user/quick-start/)
- Helm (https://helm.sh/docs/intro/install/)

## Setup

```
kind create cluster

```

## Add Helm repo

```
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
```

## Corrections

The helm chart referred to in page 18-19 no longer supports both standalone and agent deployments configured within the same chart. The following commands configuration and commands should be used to deploy a standalone collector with an agent:

### config/collector/standalone.yml

```
mode: deployment

config:
  exporters:
    logging:
      loglevel: debug

resources:
  limits:
    cpu: 1
    memory: 512Mi
```

`$ helm install otel-collector-standalone open-telemetry/opentelemetry-collector -f ./config/collector/standalone.yml`

### config/collector/config.yml

```
extraEnvs:
  - name: NODE_NAME
    valueFrom:
      fieldRef:
        fieldPath: spec.nodeName

mode: daemonset

config:
  exporters:
    otlp:
      endpoint: otel-collector-standalone-opentelemetry-collector:4317
      tls:
        insecure: true
    logging:
      loglevel: debug
  processors:
    resource:
      attributes:
      - key: k8s.node.name
        value: ${NODE_NAME}
        action: upsert
  service:
    pipelines:
      logs:
        exporters:
         - otlp
         - logging
        processors:
         - batch
         - memory_limiter
         - resource
      metrics:
        exporters:
         - otlp
         - logging
        processors:
         - batch
         - memory_limiter
         - resource
      traces:
        exporters:
         - otlp
         - logging
        processors:
         - batch
         - memory_limiter
         - resource
```

`$ helm upgrade otel-collector open-telemetry/opentelemetry-collector -f ./config/collector/config.yml`

---

_Cloud Native Observability_
