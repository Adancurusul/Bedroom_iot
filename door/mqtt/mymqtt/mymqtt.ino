#include<WiFi.h>
#include<PubSubClient.h>
const char* ssid ="adan";
const char*password =  "1122334455";
const char*mqttServer = "113.224.53.24";
const int Port =1883;
const char*User = "whatever";
const char*Password = "nothing";
const char*TOPIC = "opendoor"
const char*TOPIC_R = "state"
int door_pin = 5
WiFiClientespClient;
PubSubClientclient(espClient);
pinMode(door_pin, OUTPUT);
digitalWrite(door_pin,0);
void callback(char*topic, byte* payload, unsigned int length) 
{
    if((char)payload == 'open')
  {
      digitalWrite(door_pin,1);
      delay(1000);
       client.publish(TOPIC_R, "door_open" );
      digitalWrite(door_pin,0);
    }
void setup() 
    {  
      Serial.begin(115200);
      WiFi.begin(ssid,password);
      while (WiFi.status()!= WL_CONNECTED) 
      {
        delay(500);
  
        }  
       Serial.println("wifi connected");
       client.setServer(Server,mqttPort);
       client.setCallback(callback);
       while (!client.connected())
       {
        if (client.connect("Client",User, Password ))
        {
          Serial.println("mqtt connected");
          }
        else 
         {
            Serial.print("error ");
            Serial.print(client.state());
            delay(2000);
      }
}
client.subscribe(TOPIC);
}
void loop() 
{  
  client.loop()
  }
