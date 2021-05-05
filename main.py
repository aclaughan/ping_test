import os
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    ip_addresses = \
        [
            "192.168.60.1",
            "8.8.8.8",
            "8.8.8.4",
            "172.16.0.1"
        ]

    for ip in ip_addresses:
        result = os.popen(f"ping -c 3 {ip}").read()
        logging.info(result)
        if " 0.0% packet loss" in result:
            print(f"{ip:>16} reachable")
        else:
            print(f"{ip:>16} UNREACHABLE")
    pass


if __name__ == '__main__':
    main()
