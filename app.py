from os import environ
from time import sleep
from prometheus_client import Counter, start_http_server
from requests import get

TARGET_ADDR = environ.get("NETMETER_TARGET_ADDR", "http://localhost:8080")

POLLING_INTERVAL = int(environ.get("NETMETER_POLLING_INTERVAL", "5"))

network_receive_bytes = Counter(
    "netmeter_receive_bytes", "Network received bytes", ["device"]
)
network_receive_packets = Counter(
    "netmeter_receive_packets", "Network received packets", ["device"]
)
network_transmit_bytes = Counter(
    "netmeter_transmit_bytes", "Network transmitted bytes", ["device"]
)
network_transmit_packets = Counter(
    "netmeter_transmit_packets", "Network transmitted packets", ["device"]
)

def polling_metrics():
    while True:
        network_stats = get(TARGET_ADDR).json()
        for device in network_stats:
            network_receive_bytes.labels(device)._value.set(network_stats[device]["receive_bytes"])
            network_receive_packets.labels(device)._value.set(network_stats[device]["receive_packets"])
            network_transmit_bytes.labels(device)._value.set(network_stats[device]["transmit_bytes"])
            network_transmit_packets.labels(device)._value.set(network_stats[device]["transmit_packets"])
        sleep(POLLING_INTERVAL)

if __name__ == "__main__":
    start_http_server(9909)
    print("INFO: Netmeter exporter started...")
    polling_metrics()
