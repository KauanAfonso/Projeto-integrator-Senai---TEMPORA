#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "HTTPSRedirect.h"

const char* ssid     = "MODESTO";
const char* password = "a1234567";
//KauanAfonso

const char *GScriptId = ""; //coloque aqui sua chave

String payload_base =  "{\"command\": \"insert_row\", \"sheet_name\": \"Sheet1\", \"values\": ";
String payload = "";

const char* host = "script.google.com";   
const int httpsPort = 443;                
const char* fingerprint = "";             
String url = String("/macros/s/") + GScriptId + "/exec";   
HTTPSRedirect* client = nullptr;   

// Variáveis que representam dados a serem enviados
int esteira1 = 0;  
int esteira2 = 0; 
int esteira3 = 0;  

void setup() {
  Serial.begin(9600);        
  delay(10);
  Serial.println('\n');

  WiFi.begin(ssid, password);             
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());

  client = new HTTPSRedirect(httpsPort);
  client->setInsecure();    
  client->setPrintResponseBody(true);   
  client->setContentTypeHeader("application/json");   
  
  Serial.print("Connecting to ");
  Serial.println(host);

  bool flag = false;
  for (int i = 0; i < 5; i++) {
    int retval = client->connect(host, httpsPort);
    if (retval == 1) {
      flag = true;
      Serial.println("Connected");
      break;
    } else {
      Serial.println("Connection failed. Retrying...");
    }
  }
  
  if (!flag) {
    Serial.print("Could not connect to server: ");
    Serial.println(host);
    return;
  }
}

void loop() {

  esteira1++;        
  esteira2 = random(0, 1000);  
  esteira3 = random(0, 100000);  

  if (client != nullptr) {
    if (!client->connected()) {
      Serial.println("Reconnecting...");
      client->connect(host, httpsPort);
    }
  } else {
    Serial.println("Error creating client object!");
  }

  payload = payload_base + "\"" + esteira1 + "," + esteira2 + "," + esteira3 + "\"}";

  Serial.println("Carregando dados para o Gsheet...");
  Serial.println(payload);


  if (client->POST(url, host, payload)) { 
    Serial.println("Dados enviados com sucesso!");
  } else {
    Serial.println("Erro ao conectar ou enviar os dados");
  }
  delay(5000);
}
