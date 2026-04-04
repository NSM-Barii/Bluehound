// WORKING BLE SCANNER TEST
#pragma once

#include <NimBLEDevice.h>
#include <Arduino.h>

NimBLEScan* pScan;

void setupBLE(){
    Serial.println("Initializing BLE...");
    NimBLEDevice::init("");
    pScan = NimBLEDevice::getScan();
    pScan->setActiveScan(true);
    pScan->setInterval(1349);
    pScan->setWindow(449);
    Serial.println("BLE Ready!");
}

void scanBLE(int duration){
    Serial.println("Starting scan...");
    pScan->start(duration, false);

    NimBLEScanResults results = pScan->getResults();
    Serial.printf("Found %d devices:\n", results.getCount());

    for(int i = 0; i < results.getCount(); i++){
        const NimBLEAdvertisedDevice* device = results.getDevice(i);

        Serial.printf("  RSSI: %d | MAC: %s | Name: %s\n",
            device->getRSSI(),
            device->getAddress().toString().c_str(),
            device->getName().c_str()
        );
    }

    pScan->clearResults();
}
