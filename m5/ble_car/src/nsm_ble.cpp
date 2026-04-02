// THIS MODULE WILL BE RESPONSIBLE FOR BLE SCANNING


// IMPORTS
#include <NimBLEDevice.h>
#include <Arduino.h>

// THIS WILL BE HERE FOR REMEMBERING WHAT I NEED
#include <esp_now.h>
#include <WiFi.h>



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
*/


// THIS TOOK ME ^ HOURS TO RIGHT/FULlY COMPREHEND LOL



class Bluetooth_Scanner: public NimBLEAdvertisedDeviceCallbacks {

    

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
            scanner->setAdvertisedDeviceCallbacks(this);
            scanner->setInterval(interval);
            scanner->setWindow(99);


            
        }


        void onResult(NimBLEAdvertisedDevice* device){
            // THIS METHOD WILL BE THE CALLBACK AUTOMATICALLY 


            auto name = device->getName();
            int8_t rssi = device->getRSSI();
            auto mac = device->getAddress();
            auto manuf_data = device->getManufacturerData();


            Serial.printf(
            "RSSI: %d | Mac: %s | Name: %s | Data: %s\n",
            rssi, 
            mac.toString().c_str(),
            name.c_str(),
            manuf_data.c_str()
            );


        }



        void Main(int duration = 100){
            // THIS WILL BE USED TO LAUNCH ITER AND THEN LOOP ITERATE SCANNER

           
            scanner->start(duration, false);
            scanner->clearResults();
        

        }



};


// THIS CLASS WILL BE CALLED ON FROM main.cpp along with serial init