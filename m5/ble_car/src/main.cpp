#include <Arduino.h>

// NSM IMPORTS
#include "nsm_ble.h"
#include "nsm_sender.h"

extern int devicecount;

// INSTANCES
ESP_Pusher sender;
Bluetooth_Scanner ble;


void setup() {

  Serial.begin(115200);
  delay(1000);

  Serial.println("\n\n[+] Starting BLE Scanner...");
  ble.setup();
  Serial.println("[+] Setup complete!\n");

}

void loop() {

  ble.Main(5000);
  delay(2000);

}



Starting scan...
Starting scan...
Starting scan...
Device:  | RSSI: -88 | MAC: b0:22:7a:99:e7:7b
Starting scan...
Starting scan...
Starting scan...
Starting scan...
Device: Smart Light | RSSI: -81 | MAC: 90:00:00:49:ce:15
Starting scan...