#include <Arduino.h>

// TEST
#include "test_ble.h"

// NSM IMPORTS
// #include "nsm_ble.h"
#include "nsm_sender.h"

// EXTERNAL VARIABLES
// extern int devicecount;

// INSTANCES
ESP_Pusher sender;
// Bluetooth_Scanner ble;


void setup() {

  Serial.begin(115200);
  delay(1000); // Wait for serial to stabilize

  Serial.println("\n\n[+] Starting BLE Car Scanner...");

  setupBLE();

  //uint8_t masterAddr[] = {0x24, 0x6F, 0x28, 0xAA, 0xBB, 0xCC};
  //sender.setReceiver(masterAddr);

  // Serial.println("[*] Initializing ESP-NOW...");
  // sender.setup();
  Serial.println("[+] Setup complete!\n");

}

void loop() {

  scanBLE(5);
  delay(2000);

}
