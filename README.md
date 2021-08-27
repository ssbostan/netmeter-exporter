# netmeter-exporter

![Visits Badge](https://badges.pufler.dev/visits/ssbostan/netmeter-exporter)

Prometheus exporter for [netmeter](https://github.com/ssbostan/netmeter) monitoring tool.

For everyone who wants to learn how to develop prometheus exporters with python.

## Installation and usage:

### Step 1:

Run an instance of netmeter monitoring tool.

```bash
docker run -d --name netmeter -p 8080:8080 -v /sys:/host/sys:ro -e NETMETER_SYS_PATH=/host/sys ssbostan/netmeter:2
```

### Step 2:

Run an instance of netmeter-exporter that polling metrics from netmeter instance.

```bash
docker run -d --name netmeter-exporter -p 9909:9909 -e NETMETER_TARGET_ADDR=http://172.17.0.1:8080 ssbostan/netmeter-exporter:latest
```

## Available metrics:

| Name | Type | Description |
| -- | -- | -- |
| netmeter_receive_bytes | Counter | Network device received bytes |
| netmeter_receive_packets | Counter | Network device received packets |
| netmeter_transmit_bytes | Counter | Network device transmitted bytes |
| netmeter_transmit_packets | Counter | Network device transmitted packets |

## How to contribute:

All contributions are welcomed. We need to develop [netmeter](https://github.com/ssbostan/netmeter) first.

### TODO:

  - [ ] Collect more network statistics
