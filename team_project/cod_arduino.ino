#include <ESP8266WiFi.h>

WiFiServer server(1234);
 
float duration, distance;
void setup()
{

  pinMode(LED_BUILTIN, OUTPUT);
  delay(2000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);

  pinMode(D6, OUTPUT);
  pinMode(D5, INPUT);
  // pinMode(A5, INPUT);

  WiFi.begin("DIGI-hd4T", "barbie123");

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }

  server.begin();

}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  WiFiClient client = server.accept();
  if (client)
  {
    while (client.connected())
    {
      digitalWrite(D6, LOW);
      delayMicroseconds(2);
      digitalWrite(D6, HIGH);
      delayMicroseconds(10);
      digitalWrite(D6, LOW);

      duration = pulseIn(D5, HIGH);
      distance = (duration*.0343)/2;
      String readS = String(distance);

      if ( distance < 10 ) {
        client.print("000" + readS);
      } else if ( distance < 100 ) {
        client.print("00" + readS);
      } else if ( distance < 1000 ) {
        client.print("0" + readS);
      } else {
        client.print(readS);
      }

      delay(100);
    }
    client.stop();
  }

}