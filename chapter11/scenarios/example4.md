# Example 4

## The setup

1. Edit docker-compose.yml to use the `chapter11-example4` tag:

```
 shopper:
    image: codeboten/shopper:chapter11-example4
...
  grocery-store:
    image: codeboten/grocery-store:chapter11-example4
...
  legacy-inventory:
    image: codeboten/legacy-inventory:chapter11-example4
```

2. Update the running containers

```
docker compose up -d legacy-inventory grocery-store shopper
```

<details>
  <summary>Click to see the solution!</summary>

## The solution

The first thing to notice is a change in the "Request count per status code" chart of the "Application Metrics" dashboard. Instead of recording responses with a status code of `200`, the shopper application is seeing an increase in status code `429` (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429).

Searching for a trace containing an error, we find the following:

```
429 Too Many Requests: 2 per 1 minute
```

It appears a rate-limiter is restricting client requests and based on the impact to the rest of the application, it looks like it may need some more tweaking!

</details>

---

_Cloud Native Observability_
