// THIS MODULE WILL BE RESPONSIBLE FOR SENDING DATA TO MASTER NODE
#pragma once

// IMPORTS
#include <esp_now.h>
#include <WiFi.h>
#include <Arduino.h>


// NSM IMPORTS
#include <nsm_vars.h>




class ESP_Pusher{

    /*
    👉 char[] = perfect
    👉 String = not safe here
    char	one character
    char[]	fixed-size string buffer
    String	dynamic string object
    buffer = [] <- space allocated for string
    */


    private:
        uint8_t receiverAddress[6];


        struct Packet{
            int count;
            int packetindex;
            int totalpackets;
            Data devices[10];

        };
       
        

    public:
        
        void setReceiver(const uint8_t addr[6]){
            // SET RECEIVER MAC ADDRESS 


            // 6 * 2 = 12 Chars within a MAC Address!
            for (int i = 0; i < 6; i++){
                receiverAddress[i] = addr[i];
            }

        }

        
        bool setup(){
            
            WiFi.mode(WIFI_STA);
            
            if (esp_now_init() != ESP_OK){Serial.println("[-] Failed to initialized Master");return false;};
            
            
            esp_now_peer_info_t peerinfo = {};
            memcpy(peerinfo.peer_addr, receiverAddress, 6);
            peerinfo.channel = 0;
            peerinfo.encrypt = false;
            
            
            esp_now_add_peer(&peerinfo);
            
            Serial.println("[+] ESP-NOW Ready!"); return true;
            
        }


        Data createData(int rssi, String mac, String name, const char* manuf_data){
            // THIS METHOD WILL BE USED TO STORE PACKETS
    
    
            // CREATE OBJECT & ASSIGN VARIABLES
            Data data;
    
            
    
            // USE THIS TO STORE THE RECEIVED VAR AND COPY IT INTO THE STRUCT 
            // WE USE strcpy BECAUSE ITS A BUFFER
            /*  strcpy(dest, src) copies strings
                dest = char[] buffer
                src = char* (often from .c_str())
                used because char[] can’t be assigned directly
            */ 
    
    
            data.rssi = rssi;
            strcpy(data.mac, mac.c_str());
            strcpy(data.name, name.c_str());
            strcpy(data.manuf_data, manuf_data);
    
            //esp_now_send(receiverAddress, (uint8_t*)&data, sizeof(data));
            //Serial.println("[+] Successfully pushed data to master!");
            return data;
        }


        void sendBatch(Data devices[], int devicecount){
            // THIS METHOD WILL BE USED TO DIRECTLY PUSH DATA TO MASTER

            int totalpackets = (devicecount + 9) / 10;


            for (int i = 0; i < devicecount; i += 10){

                Packet packet;

                packet.count = 0;
                packet.packetindex = i / 10;
                packet.totalpackets = totalpackets;


                for (int j = 0; j < 10 && (i + j) < devicecount; j++){

                    packet.devices[j] = devices[i + j];
                    packet.count++;
                };


                esp_now_send(receiverAddress, (uint8_t*)&packet, sizeof(packet));
                delay(5);

            };


        }
    };


