# ToDo Prometheus Metrics

This is a simple ToDo application built using Python & Flask. It makes use of the official [Promethues Python SDK](https://github.com/prometheus/client_python) to add custom metrics to the app.
These metrics are added to `/metrics` endpoint which can be exported to apps like Grafana, New Relic etc. for visualization. 

**Note:**
The app makes use of Redis to store ToDo items, so make sure that Redis is installed and running before you run this application. You can refer to this documentation on [Python with Redis](https://developer.redis.com/develop/python/) to know more.
