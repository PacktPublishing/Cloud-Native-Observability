# Example 3

## The setup

1. Edit docker-compose.yml to use the `chapter11-example3` tag:

```
 shopper:
    image: codeboten/shopper:chapter11-example3
...
  grocery-store:
    image: codeboten/grocery-store:chapter11-example3
...
  legacy-inventory:
    image: codeboten/legacy-inventory:chapter11-example3
```

2. Update the running containers

```
docker compose up -d legacy-inventory grocery-store shopper
```

<details>
  <summary>Click to see the solution!</summary>

## The solution

An increase in the duration of requests across all services appears right away with this new version. The container metrics dashboard isn't showing any indication of a change in performance.

Looking through traces, the `inventory` service produces a span named `get_products` which contains the attribute `product_count`. Compared to an earlier span, that number seems quite a bit larger.

Additionally, looking through at other metrics produced by the inventory service, there is a jump in the value reported for `inventory_count` from 107 to 3317. This increase in inventory has increased the operation of retrieving the data and the response size. This scenario highlights a few new metrics that would be interesting to add to our dashboards.

</details>

---

_Cloud Native Observability_
