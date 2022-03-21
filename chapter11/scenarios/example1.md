# Example 1

## The setup

1. Edit docker-compose.yml to use the `chapter11-example1` tag:

```
 shopper:
    image: codeboten/shopper:chapter11-example1
...
  grocery-store:
    image: codeboten/grocery-store:chapter11-example1
...
  legacy-inventory:
    image: codeboten/legacy-inventory:chapter11-example1
```

2. Update the running containers

```
docker compose up -d legacy-inventory grocery-store shopper
```

<details>
  <summary>Click to see the solution!</summary>

## The solution

A significant increase in request duration from the `inventory` service leads us to look at the traces for that service. A suspiciously named span has appeared.

The **sleepy service** span shows that a 3 second delay was introduced in this version of the application causing issues in the system.

## </details>

_Cloud Native Observability_
