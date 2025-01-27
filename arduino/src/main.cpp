#include <Arduino.h>
#include <ArduinoJson.h>
#include <cstdint>
#include <string>
#include <array>

struct PlayerData
{
  uint16_t id;
  uint16_t distance;
  uint16_t speed;
};

static bool running = false;

static std::array<PlayerData, 2> players = {
    PlayerData{.id = 0, .distance = 0, .speed = 0},
    PlayerData{.id = 1, .distance = 0, .speed = 0}};

void handleClear()
{
  for (auto& player : players)
  {
    player.distance = 0;
  }
}

void handleStart()
{
  running = true;
}

void handleStop()
{
  running = false;
}

void handleCommand(const String& command) {
  if (command == "start") {
    handleStart();
  } else if (command == "stop") {
    handleStop();
  } else if (command == "clear") {
    handleClear();
  } else {
    Serial.println("Unknown command");
  }
}

void handleSerialInput()
{
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    JsonDocument doc;
    DeserializationError error = deserializeJson(doc, input);

    if (error) {
      Serial.println("Invalid JSON received");
    } else {
      const char* command = doc["command"];
      if (command != nullptr) {
        handleCommand(String(command));
      }
    }
  }
}

String serializePlayerData(std::array<PlayerData, 2> players)
{
  JsonDocument doc;
  JsonArray playersArray = doc["players"].to<JsonArray>();

  for (const auto& player : players)
  {
    JsonObject playerObject = playersArray.add<JsonObject>();
    playerObject["id"] = player.id;
    playerObject["distance"] = player.distance;
  }
  String output;

  doc.shrinkToFit();

  serializeJson(doc, output);
  return output;
}


void setup() {
  Serial.begin(115200);
}

void loop() {
  handleSerialInput();

  if (running)
  {
    players[0].distance+=1;
    players[1].distance+=2;

    String jsonString = serializePlayerData(players);
    Serial.println(jsonString);
  }


  delay(100);
}
