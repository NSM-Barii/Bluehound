#include <Arduino.h>


// NSM IMPORTS
#include "nsm_ble.h"
#include "nsm_sender.h"

// EXTERNAL VARIABLES
extern int devicecount;

// INSTANCES
ESP_Pusher sender;
Bluetooth_Scanner ble;


void setup() {

  Serial.begin(115200);
  delay(1000); // Wait for serial to stabilize

  Serial.println("\n\n[+] Starting BLE Car Scanner...");

  Serial.println("[*] Initializing BLE...");
  ble.setup();
  Serial.println("[+] BLE initialized!");

  //uint8_t masterAddr[] = {0x24, 0x6F, 0x28, 0xAA, 0xBB, 0xCC};
  //sender.setReceiver(masterAddr);

  // Serial.println("[*] Initializing ESP-NOW...");
  // sender.setup();
  Serial.println("[+] Setup complete!\n");

}

void loop() {

  Serial.println("[*] Starting BLE scan...");
  ble.Main(2000);
  Serial.printf("[*] Scan complete. Found %d devices\n\n", devicecount);

}
