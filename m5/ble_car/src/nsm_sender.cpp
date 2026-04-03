// THIS MODULE WILL BE RESPONSIBLE FOR SENDING DATA TO MASTER NODE


// IMPORTS
#include <esp_now.h>
#include <WiFi.h>
#include <Arduino.h>






class ESP_Pusher{

    /*
    👉 char[] = perfect
    👉 String = not safe here
    */


    private:
        uint8_t receiverAddress[6];
       
        struct Data {
            int rssi;
            char mac[18];  // YOU MAKE THESE A ARRAY SO strcpy CAN
            char name[32];
            char manuf_data[64];

        };


    public:


        void send(int rssi, String mac, String name, const char* manuf_data){
            // THIS METHOD WILL BE USED TO DIRECTLY PUSH DATA TO MASTER


            // CREATE OBJECT & ASSIGN VARIABLES
            Data data;

            // VARS
            data.rssi = rssi;
            strcpy(data.mac, mac.c_str());
            strcpy(data.name, name.c_str());
            strcpy(data.manuf_data, manuf_data);

            esp_now_send(receiverAddress, (uint8_t*)&data, sizeof(data));


            
            Serial.println("[+] Successfully pushed datat to master!");
        }



        bool setup(){

            if (esp_now_init() == ESP_OK; WiFi.mode(WIFI_STA) && WiFi.getMode() == WIFI_STA){Serial.println("[+] Successfully initalized master");}
            else{Serial.print("[-] Failed to initialized Master");return false;}
        }
};