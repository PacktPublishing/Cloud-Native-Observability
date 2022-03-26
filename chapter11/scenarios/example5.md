# Example 5

## The setup

1. Edit docker-compose.yml to use the `chapter11-example5` tag:

```
 shopper:
    image: codeboten/shopper:chapter11-example5
...
  grocery-store:
    image: codeboten/grocery-store:chapter11-example5
...
  legacy-inventory:
    image: codeboten/legacy-inventory:chapter11-example5
```

2. Update the running containers

```
docker compose up -d legacy-inventory grocery-store shopper
```

<details>
  <summary>Click to see the solution!</summary>

## The solution

As first, deploying this last example doesn't appear to change anything. After a few minutes however, the number of requests in the "Application Metrics" dashboard starts to drop.

Looking through the "Container Metrics" there's a suspicious increase in memory consumed by `shopper`. As the containers exceed the memory available to them, they will be terminated by Docker. The following query shows us the count of `shopper` containers still reporting:

`count(container_memory_percent{container_name=~"chapter11_shopper.*"})`

Over time, this number will drop to 0 as all containers run out of memory. Better revert that change!

</details>

---

_Cloud Native Observability_
