# Chapter 5 examples

This folder contains examples for Chapter 5.

## Prerequisites

- Python 3.6+

## Setup

```
mkdir cloud_native_observability
python3 -m venv cloud_native_observability
source cloud_native_observability/bin/activate

# install OpenTelemetry packages
pip install opentelemetry-api \
            opentelemetry-sdk \
            opentelemetry-propagator-b3

# install additional libraries
pip install flask requests
```

## Default aggregations

| Instrument                 | Default aggregation                |
| -------------------------- | ---------------------------------- |
| Counter                    | SumAggregation                     |
| Asynchronous Counter       | SumAggregation                     |
| UpDownCounter              | SumAggregation                     |
| Asynchronous UpDownCounter | SumAggregation                     |
| Histogram                  | ExplicitBucketHistogramAggregation |
| Asynchronous Gauge         | LastValueAggregation               |

---

_Cloud Native Observability_
