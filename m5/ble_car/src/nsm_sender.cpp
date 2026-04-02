// THIS MODULE WILL BE RESPONSIBLE FOR SENDING DATA TO MASTER NODE


// IMPORTS
#include <esp_now.h>
#include <WiFi.h>
#include <Arduino.h>






class ESP_Pusher{


    private:
        uint8_t receiverAddress[6];

        struct data {
            int rssi,
            char mac[18],
            String name,
            String manuf_data

        };


    public:


        void send(int rssi, String mac, String name, const char* manuf_data){


            
            Serial.println("[+] Successfully pushed datat to master!");
        }



        bool setup(){

            if (esp_now_init() == ESP_OK; WiFi.mode(WIFI_STA) && WiFi.getMode() == WIFI_STA){Serial.println("[+] Successfully initalized master");}
            else{Serial.print("[-] Failed to initialized Master");return false;}
        }
};