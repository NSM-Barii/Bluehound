#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <Adafruit_NeoPixel.h>

#define LED_PIN 5
#define LED_COUNT 60

const char* ssid = "";
const char* password = "";

bool emergency = false;
bool flashState = false;
unsigned long lastFlash = 0;
uint32_t currentColor = 0;

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
WebServer server(80);

// ----------- COLOR HANDLER -----------

void handleRoot() {

    if (server.hasArg("color")) {

        String color = server.arg("color");
        emergency = false;  // reset unless flash selected

        if (color == "green")
            currentColor = strip.Color(0, 255, 0);

        else if (color == "yellow")
            currentColor = strip.Color(255, 255, 0);

        else if (color == "orange")
            currentColor = strip.Color(255, 80, 0);

        else if (color == "red")
            currentColor = strip.Color(255, 0, 0);

        else if (color == "white")
            currentColor = strip.Color(255, 255, 255);

        else if (color == "off")
            currentColor = strip.Color(0, 0, 0);

        else if (color == "flash") {
            emergency = true;
        }

        if (!emergency) {
            strip.fill(currentColor);
            strip.show();
        }

        server.send(200, "text/plain", "Color changed to " + color);
    }
    else {
        server.send(200, "text/plain",
                    "Add ?color=green/yellow/orange/red/flash/white/off");
    }
}

// ----------- SETUP -----------

void setup() {

    Serial.begin(115200);

    strip.begin();
    strip.clear();
    strip.show();

    WiFi.begin(ssid, password);

    Serial.print("Connecting to WiFi");

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nConnected!");
    Serial.println(WiFi.localIP());

    server.on("/", handleRoot);
    server.begin();
}

// ----------- LOOP -----------

void loop() {

    server.handleClient();

    if (emergency) {

        unsigned long now = millis();

        if (now - lastFlash >= 300) {
            lastFlash = now;
            flashState = !flashState;

            if (flashState)
                strip.fill(strip.Color(255, 0, 0));
            else
                strip.fill(strip.Color(0, 0, 0));

            strip.show();
        }
    }
}
