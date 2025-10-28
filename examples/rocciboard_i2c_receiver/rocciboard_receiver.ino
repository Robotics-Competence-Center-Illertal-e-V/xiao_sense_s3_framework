/**
 * RocciBoard Compass-Sensor Default Example
 * 
 * AUTHOR: Jonas Biener (<jonas.biener@rocci.net>) for the Robotics Competence Center Illertal e. V. (<https://rocci.net>) 
 * COPYRIGHT: Copyright (c) 2023 Robotics Competence Center Illertal e. V.
 * VERSION: 1.0 [09-2023] First release
 * 
 * This example demonstrates the use of the RocciBoard-Compass-Sensor. (BNO055)
 * The compass-sensor must be connected to one of the multiplexed sensor-ports of the RocciBoard.
 * Initialization is performed through the RocciBoard with initRBSensor(compass) which injects the multiplexer in the sensor.
 * All other RBSensors are also compatible with this schema and can be used accordingly.
 */

#include "rocciboard.h"     // Include the RocciBoard Library

RocciBoard rb;


void setup() {

    Serial.begin(9600);     // Establish Serial Connection with the PC
    rb.init();              // Initialize RocciBoard  
    Serial.println("hello world")  ;
  }

void loop() {
    rb.openSensorPort(0);
    Wire.requestFrom(0x55, 1);    // request 6 bytes from slave device 55

    while(Wire.available()){   // slave may send less than requested
      char c = Wire.read();    // receive a byte as character
      Serial.println((int)c);         // print the character
    }
    rb.closeSensorPort(0);
    // Delay to keep values readable
    delay(1000);
}