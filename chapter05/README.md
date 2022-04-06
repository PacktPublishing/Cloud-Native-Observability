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

## Instruments

| Instrument                 | Synchronicity | Monotonic |
| -------------------------- | ------------- | --------- |
| Counter                    | Synchronous   | Yes       |
| Asynchronous Counter       | Asynchronous  | Yes       |
| UpDownCounter              | Synchronous   | No        |
| Asynchronous UpDownCounter | Asynchronous  | No        |
| Histogram                  | Synchronous   | No        |
| Asynchronous Gauge         | Asynchronous  | No        |

## Default aggregations

| Instrument                 | Default aggregation                |
| -------------------------- | ---------------------------------- |
| Counter                    | SumAggregation                     |
| Asynchronous Counter       | SumAggregation                     |
| UpDownCounter              | SumAggregation                     |
| Asynchronous UpDownCounter | SumAggregation                     |
| Histogram                  | ExplicitBucketHistogramAggregation |
| Asynchronous Gauge         | LastValueAggregation               |

## Dimensions

| Customer | Country | Locale |
| -------- | ------- | ------ |
| 1        | Canada  | en-US  |
| 1        | France  | fr-FR  |
| 1        | Canada  | fr-FR  |

## Effect of attribute keys

| Counter operation                           | Transformed via attribute keys |
| ------------------------------------------- | ------------------------------ |
| `add(1,{"locale":"fr-FR"})`                 | `add(1,{"locale":"fr-FR"})`    |
| `add(1,{"country":"CA"})`                   | `add(1,{})`                    |
| `add(1,{"locale":"en-US", "country":"CA"})` | `add(1,{"locale":"en-US"})`    |
| `add(1,{})`                                 | `add(1,{})`                    |

---

_Cloud Native Observability_
