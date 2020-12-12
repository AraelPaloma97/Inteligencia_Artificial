// LUNA GONZALES ROCIO
//MARTINEZ GARCIA ISABEL
//PALOMA VICTORIANO ARAEL
//ROBLES PADILLA OSWALDO
//librerias 
#include <Servo.h>

//objetos
Servo moviVer;
Servo moviHor;

//variables
int pHor = 90;
int pVer = 90;
int dato = 0;

//metodos 
void setup() {
  Serial.begin(9600);
  moviHor.attach(8);//servo posicio horizontal(ejey)
  moviVer.attach(7); //servo posicio vertical (ejex)
  
// mover servo
 moviHor.write(pHor); 
 moviVer.write(pVer); 
 
}

void loop() {
  if (Serial.available() >= 1){
    dato = Serial.read();
  }
  if (dato == 'p')
  {
    pHor = pHor +1;
    moviHor.write(pHor);
    delay(500);   
  }
   if (dato == 'i')
  {
    pHor = pHor - 1;
    moviHor.write(pHor);
    delay(500);   
  }
   if (dato == 'n')
  {
    pVer = pVer +1;
    moviVer.write(pVer);
    delay(500);   
  }
   if (dato == 'r')
  {
    pVer = pVer - 1;
    moviVer.write(pVer);
    delay(500);   
  }
}
