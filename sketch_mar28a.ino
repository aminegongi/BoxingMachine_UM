#include "HX711.h"

#define calibration_factor -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

#define LOADCELL_DOUT_PIN_1  2
#define LOADCELL_SCK_PIN_1  3

#define LOADCELL_DOUT_PIN_2  4
#define LOADCELL_SCK_PIN_2  5

#define LOADCELL_DOUT_PIN_3  6
#define LOADCELL_SCK_PIN_3  7

#define LOADCELL_DOUT_PIN_4  8
#define LOADCELL_SCK_PIN_4  9

HX711 scale_1;

HX711 scale_2;

HX711 scale_3;

HX711 scale_4;

int w =0;
char action = 'x';

int val_test =5;

void setup() {
  Serial.begin(9600);
  scale_1.begin(LOADCELL_DOUT_PIN_1, LOADCELL_SCK_PIN_1);
  scale_1.set_scale(calibration_factor); 
  scale_1.tare();
  //Scale2
  scale_2.begin(LOADCELL_DOUT_PIN_2, LOADCELL_SCK_PIN_2);
  scale_2.set_scale(calibration_factor); 
  scale_2.tare();
  //Scale3
  scale_3.begin(LOADCELL_DOUT_PIN_3, LOADCELL_SCK_PIN_3);
  scale_3.set_scale(calibration_factor); 
  scale_3.tare();
  //Scale4
  scale_4.begin(LOADCELL_DOUT_PIN_4, LOADCELL_SCK_PIN_4);
  scale_4.set_scale(calibration_factor); 
  scale_4.tare();
  
}

void loop() {
  if (Serial.available() > 0) {
    action = Serial.read();
    if(action == 'x'){
      w = -1;
    }
    else{
      if(action == 'c'){
        w = 0;
      }
    }
  }
  if(w==0){
    if(abs(scale_1.get_units())>val_test){
      Serial.println(scale_1.get_units());
    }
    else if(abs(scale_2.get_units())>val_test){
      Serial.println(scale_2.get_units());
    }
    else if(abs(scale_3.get_units())>val_test){
      Serial.println(scale_3.get_units());
    }
    else if(abs(scale_4.get_units())>val_test){
      Serial.println(scale_4.get_units());
    }
    else{
      Serial.println("0");
    }
  }

}
