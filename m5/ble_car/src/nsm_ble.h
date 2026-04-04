// THIS MODULE WILL BE RESPONSIBLE FOR BLE SCANNING
#pragma once

// IMPORTS
#include <NimBLEDevice.h>
#include <Arduino.h>

// THIS WILL BE HERE FOR REMEMBERING WHAT I NEED
#include <esp_now.h>
#include <WiFi.h>


// NSM IMPORTS
#include "nsm_sender.h"
#include "nsm_vars.h"



/*
obj.method()        → object
ptr->method()       → pointer
Class::method()     → class itself

[NimBLEDevice]
      ↓ owns
[NimBLEScan object]
      ↓ gives pointer
scanner → (points to it)

A pointer = an address to where an object lives in memory

Object = the house 🏠
Pointer = the address 📍


Object	you own the data
Pointer	you access someone else’s data

&name = “give me the address of name”

👉 " " = search your project first
👉 < > = search system libraries only

*/


// THIS TOOK ME ^ HOURS TO RIGHT/FULlY COMPREHEND LOL


// GLOBAL INSTANCES
extern ESP_Pusher sender;
Data devices[50];
int devicecount = 0;


class Bluetooth_Scanner: public NimBLEScanCallbacks {

    

    // THIS WILL BE USED TO PRIVATIZE INSTANCES // _function()
    private:
        NimBLEScan* scanner; // CREATE POINTER

    public:


        void setup(int interval = 100){
            // THIS METHOD WILL BE RESPONSIBLE FOR INITIALIZING THE BLE SCANNER


            // INIT SCANNER
            NimBLEDevice::init("");
            scanner = NimBLEDevice::getScan();  // THIS CLASS IS INSIDE THE POINTER
            scanner->setActiveScan(true);
            scanner->setScanCallbacks(this, false);
            scanner->setInterval(1349);
            scanner->setWindow(449);
            scanner->setMaxResults(0);


        }


        void onDiscovered(const NimBLEAdvertisedDevice* device){
            // THIS METHOD WILL BE THE CALLBACK AUTOMATICALLY


            Serial.println("starting");
            int8_t rssi = device->getRSSI();
            String mac = String(device->getAddress().toString().c_str());
            String name = String(device->getName().c_str());
            String manuf_data_str = device->getManufacturerData();
            const char* manuf_data = manuf_data_str.c_str();


            Serial.printf(
            "RSSI: %d | Mac: %s | Name: %s \n",
            rssi, 
            mac.c_str(),
            name.c_str()
            //manuf_data  // TAKE THIS OUT FOR NOW
            );
                 
            
            if (devicecount < 50){

                devices[devicecount++] = sender.createData(rssi, mac, name, manuf_data);

            }


        }



        void Main(int duration = 100){
            // THIS WILL BE USED TO LAUNCH ITER AND THEN LOOP ITERATE SCANNER
In file included from src/main.cpp:7:
src/nsm_ble.h: In member function 'virtual void Bluetooth_Scanner::onDiscovered(const NimBLEAdvertisedDevice*)':
src/nsm_ble.h:92:64: error: conversion from 'std::__cxx11::string' {aka 'std::__cxx11::basic_string<char>'} to non-scalar type 'String' requested
             String manuf_data_str = device->getManufacturerData();
                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~
*** [.pio/build/esp32dev/src/main.cpp.o] Error 1


            scanner->start(duration/1000, false);

           // sender.sendBatch(devices, devicecount);
            devicecount = 0;



        }
        

};


// THIS CLASS WILL BE CALLED ON FROM main.cpp along with serial init