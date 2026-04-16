#include <Arduino.h>
#include <SPI.h>

// TEMP: using generic driver just to confirm screen pipeline
// This will likely NOT fully work until we match the panel,
// but we’re forcing hardware validation first.

#define TFT_MOSI 18
#define TFT_SCLK 47
#define TFT_CS   5

void setup() {
    Serial.begin(115200);
    delay(1000);

    Serial.println("[+] Starting display test...");

    SPI.begin(TFT_SCLK, -1, TFT_MOSI, TFT_CS);

    Serial.println("[+] SPI initialized");

    // Manual raw test (IMPORTANT)
    pinMode(TFT_CS, OUTPUT);
    digitalWrite(TFT_CS, LOW);

    SPI.transfer(0xAA);  // dummy data

    digitalWrite(TFT_CS, HIGH);

    Serial.println("[+] SPI signal sent");
}

void loop() {}cj