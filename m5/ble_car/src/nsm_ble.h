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
            scanner->setScanCallbacks(this);
            scanner->setInterval(interval);
            scanner->setWindow(99);


            
        }


        void onResult(NimBLEAdvertisedDevice* device){
            // THIS METHOD WILL BE THE CALLBACK AUTOMATICALLY 


            int8_t rssi = device->getRSSI();
            String mac = String(device->getAddress().toString().c_str());
            String name = String(device->getName().c_str());
            const char* manuf_data = device->getManufacturerData().c_str();


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

           
            scanner->start(duration, false);
            delay(duration);
            scanner->clearResults();
            
           // sender.sendBatch(devices, devicecount);
            devicecount = 0;

        

        }
        

};


// THIS CLASS WILL BE CALLED ON FROM main.cpp along with serial init