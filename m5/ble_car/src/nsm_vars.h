#pragma once




struct Data{
    int rssi;
    char mac[18];  // YOU MAKE THESE A ARRAY SO strcpy CAN
    char name[32];
    char manuf_data[100];
};