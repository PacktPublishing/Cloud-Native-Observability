# Example 2

## The setup

1. Edit docker-compose.yml to use the `chapter11-example2` tag:

```
 shopper:
    image: codeboten/shopper:chapter11-example2
...
  grocery-store:
    image: codeboten/grocery-store:chapter11-example2
...
  legacy-inventory:
    image: codeboten/legacy-inventory:chapter11-example2
```

2. Update the running containers

```
docker compose up -d legacy-inventory grocery-store shopper
```

<details>
  <summary>Click to see the solution!</summary>

## The solution

Error rate for both `grocery-store` and `shopper` trend upward. Looking at a trace for `grocery-store` yields the following error:

```
HTTPConnectionPool(host='legacy-inventory', port=5001): Max retries exceeded with url: /inventory (Caused by
NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f5bc0534670>: Failed to establish a
new connection: [Errno 111] Connection refused'))
```

The metrics reported by the `inventory` container are normal, although it is not receiving any traffic. Searching through the logs for `inventory` shows the following message:

```
* Running on http://172.18.0.8:5005/ (Press CTRL+C to quit) service.version=9.8.5
```

The ports are mismatched! Example 2 contains a configuration error in the `inventory` service.

</details>

---

_Cloud Native Observability_
