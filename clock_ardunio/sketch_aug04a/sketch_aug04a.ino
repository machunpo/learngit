#include "TM1637.h"

#define CLK 2
#define DIO 3

#define CLK2 5
#define DIO2 6

TM1637 tm1637(CLK, DIO);
TM1637 tm1637_second(CLK2, DIO2);

int8_t TimeDisp[] = {0x08, 0x08, 0x08, 0x08};
int8_t Year = 20;
int8_t Moon = 8;
int8_t Day = 2;
int8_t Hour = 12;
int8_t Min = 34;
int8_t Sec = 0;
String inputString = "";
int ledPin = 13;

int8_t TimeDisp_second[] = {0x08, 0x08, 0x08, 0x08};
int temperature = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  pinMode(4,OUTPUT);
  Serial.println("Serial interface between PC and chipKIT");

  tm1637.init();
  tm1637.set(BRIGHT_DARKEST); //BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7
  tm1637.point(POINT_ON);
  tm1637.display(TimeDisp);
  
  digitalWrite(4,HIGH);
  delay(2500);
  tm1637.point(POINT_OFF);
  tm1637.clearDisplay();
  digitalWrite(4,LOW);
  delay(2500);
  
  
  tm1637_second.init();
  tm1637_second.set(BRIGHT_DARKEST); //BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7
  tm1637_second.point(POINT_ON);
  tm1637_second.display(TimeDisp_second);

  digitalWrite(4,HIGH);
  delay(2500);
  tm1637_second.point(POINT_OFF);
  tm1637_second.clearDisplay();
  digitalWrite(4,LOW);
  delay(2500);
  
  
  
  
  
  
   digitalWrite(1,LOW);
   digitalWrite(2,LOW);
   digitalWrite(3,LOW);
   digitalWrite(5,LOW);
   digitalWrite(6,LOW);
   digitalWrite(7,LOW);
   digitalWrite(8,LOW);
   digitalWrite(11,LOW);
   digitalWrite(12,LOW);
   digitalWrite(13,LOW);
   digitalWrite(15,LOW);
   digitalWrite(16,LOW);
   digitalWrite(17,LOW);
   digitalWrite(18,LOW);
         
  
}

void loop()
{
  digitalWrite(ledPin,LOW);
  digitalWrite(4,HIGH);

  while (Serial.available())       //判断是否接收到数据
  {
    inputString = inputString + char(Serial.read());
    delay(2);
  }
   

  if (inputString!="")    //如果收到数据  显示之
   {                         
    int brry = inputString.toInt();
    Hour = brry / 100;
    Min  = brry % 100;
    Sec  =  0;
    Serial.print("input number is:");
    Serial.println(brry);
    inputString = "";
  }
  
  Sec++;
  if (Sec == 60) {
    Sec = 0;
    Min++;
    //Serial.println(TimeDisp);     //看看能不能打印出来
    String d="";
    for(int i=0;i<4;i++){
      d = d + TimeDisp[i];
    }
    Serial.println(d);
    //end
    if (Min == 60) {
      Min = 0;
      Hour++;
     // Serial.println('zhen dian bao shi ');
      if (Hour == 24) {
        Hour = 0;
        Sec = 2;
        //delay(1)
      }
    }
  }

  TimeDisp[0] = Hour / 10;
  TimeDisp[1] = Hour % 10;
  TimeDisp[2] = Min / 10;
  TimeDisp[3] = Min % 10;
  tm1637.point(POINT_ON);
  tm1637.display(TimeDisp);
  delay(499);
  tm1637.point(POINT_OFF);
  tm1637.display(TimeDisp);
  digitalWrite(4,LOW);
  delay(499);            //这个用来调整时间精度


    TimeDisp_second[0]=Sec / 10;
    TimeDisp_second[1]=Sec % 10;
    TimeDisp_second[2]=Sec / 10;
    TimeDisp_second[3]=Sec % 10;


  tm1637_second.display(TimeDisp_second);

  
  
  

 
  
}
