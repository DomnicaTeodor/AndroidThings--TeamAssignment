# AndroidThings – Team Assignment

As part of an Arduino-based electronics team assignment, my team and I designed and built an interactive unlocking mechanism for a real-world escape room. The system used a motion detecting proximity sensor as a puzzle element—when motion was detected within a specific range, it triggered an actuator to simulate unlocking, enhancing the immersive gameplay experience.

---

## Schematics Plan – Electronics and Connectivity

![Image](https://github.com/user-attachments/assets/6467da7a-d5a5-44fe-a594-289c8cf81333)

Our setup centered around an ESP8266 (NodeMCU) microcontroller powered by a battery pack, connected to a dual motion-detecting proximity sensor. When movement is detected near both sensors in the correct sequence or time window, the system triggers an output signal to activate an actuator, such as a servo or indicator light, simulating the effect of a lock being opened.

---

## Pre-requisites – Hardware Components

To build this project, you'll need the following components:

- 1x [ESP8266 NodeMCU board](https://www.robofun.ro/platforme-de-dezvoltare/nodemcu-esp8266)
- 2x [IR or ultrasonic proximity sensors](https://www.optimusdigital.ro/ro/senzori-de-distanta/331-senzor-de-proximitate-cu-infrarosu.html)
- 1x Battery pack (e.g., Li-ion or AA holder) or portable USB power bank
- jumper wires
- [Fritzing](https://fritzing.org) (for schematics)

---

## Setup and Build Plan

The setup for this project involved wiring the two motion-detecting proximity sensors to the ESP8266, using digital I/O pins for signal reading. Power was supplied through a battery pack connected to the microcontroller’s VIN and GND pins, enabling full mobility and standalone operation.

Each sensor was strategically positioned to detect motion in specific zones, forming part of the escape room's puzzle logic. The microcontroller was programmed to monitor both sensors and check for a condition—such as both sensors being triggered within a certain time frame or in a specific order. Once this condition was satisfied, the system would trigger an actuator, such as rotating a servo or flashing an LED, to simulate an unlocking event.

The entire system was prototyped on a breadboard and powered independently for testing. The interaction was designed to feel seamless and reactive, increasing immersion for escape room participants.

---

## Demo Video 🎥

[https://github.com/user-attachments/assets/9f660308-482a-440b-ba12-34e50ae86625](https://github.com/user-attachments/assets/69fc50b3-0084-4844-9e61-4eeb5a6d8617)

---
