// WORKING BLE SCANNER TEST
#pragma once

#include <NimBLEDevice.h>
#include <Arduino.h>

NimBLEScan* pScan;

class ScanCallbacks: public NimBLEScanCallbacks {
    void onResult(const NimBLEAdvertisedDevice* device) {
        Serial.printf("Device: %s | RSSI: %d | MAC: %s\n",
            device->getName().c_str(),
            device->getRSSI(),
            device->getAddress().toString().c_str()
        );
    }
};

void setupBLE(){
    Serial.println("Initializing BLE...");
    NimBLEDevice::init("");
    pScan = NimBLEDevice::getScan();
    pScan->setScanCallbacks(new ScanCallbacks());
    pScan->setActiveScan(true);
    pScan->setInterval(100);
    pScan->setWindow(99);
    Serial.println("BLE Ready!");
}

void scanBLE(int seconds){
    Serial.println("Starting scan...");
    pScan->start(seconds, false);
}
