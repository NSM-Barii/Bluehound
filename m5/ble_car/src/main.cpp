#include <Arduino.h>


// NSM IMPORTS
#include "nsm_ble.h"
#include "nsm_sender.h"



// INSTANCES
ESP_Pusher sender;
Bluetooth_Scanner ble;


void setup() {
  
  Serial.begin(115200);
  ble.setup();
  uint8_t masterAddr[] = {0x24, 0x6F, 0x28, 0xAA, 0xBB, 0xCC};
  sender.setReceiver(masterAddr);
  sender.setup();
  

}

void loop() {
  
  ble.Main(2000);

}
