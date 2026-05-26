import time
import logging
import json

logging.basicConfig(level=logging.INFO)

class CableGuardPoC:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.status = "CONNECTED"

    def poll_sensor(self):
        # Dalam PoC, kita simulate dengan file atau random
        # Di sini kita letak logic: '0' = terputus, '1' = bersambung
        return 1 

    def send_alert(self):
        # Placeholder untuk Webhook (Slack/Discord/Custom API)
        logging.warning(f"ALERT: Cable {self.sensor_id} Tamper Detected!")

    def run(self):
        logging.info(f"Monitoring started for {self.sensor_id}...")
        while True:
            if self.poll_sensor() == 0:
                self.send_alert()
                break
            time.sleep(0.5)

if __name__ == "__main__":
    monitor = CableGuardPoC("RAIL-ZONE-A1")
    monitor.run()