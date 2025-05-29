#include "TM1637.h"

#define CLK 2  //定义时钟引脚
#define DIO 3  //定义数据引脚

// 如果需要第二个显示模块，可以取消下面的注释并定义引脚
// #define CLK2 5
// #define DIO2 6

TM1637 tm1637(CLK, DIO);  //初始化TM1637显示模块

// 如果需要第二个显示模块，可以取消下面的注释并定义引脚
// TM1637 tm1637_second(CLK2, DIO2);

int8_t TimeDisp[] = {0x08, 0x08, 0x08, 0x08};   //时钟显示数组
int8_t Year = 25;  //年份
int8_t Moon = 1;  //月份
int8_t Day = 10;  //日期
int8_t Hour = 12;  //小时
int8_t Min = 34;  //分钟
int8_t Sec = 0;   //秒钟
int ledPin = 13;   //LED引脚定义
String inputString = "";    //用于存储从串口接收到的输入字符串


// int temperature = 15; //设置默认温度为十五度
// int8_t TemperatureDisp[] = {0x00, 0x00, 0x08, 0x08};    //温度显示数组，0x08表示小数点


void setup()
{
  Serial.begin(9600);   //初始化串口通信，波特率为9600
  pinMode(ledPin, OUTPUT);    //设置LED引脚为输出模式
  pinMode(4, OUTPUT);   //设置引脚4为输出模式
  Serial.println("Serial interface between PC and chipKIT");    //打印提示信息到串口

  tm1637.init();    //初始化TM1637显示模块
  tm1637.set(BRIGHT_DARKEST);       //BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7  `BRIGHT_DARKEST` 是一个标识符，通常用于表示亮度的最低级别（最暗）。


  tm1637.point(POINT_ON);       //开启小数点显示   
  tm1637.display(TimeDisp);     //显示初始时间

  digitalWrite(4, HIGH);    //设置引脚4为高电平

  delay(2500);    //延时2.5秒
  tm1637.point(POINT_OFF);    //关闭小数点显示
  tm1637.clearDisplay();      //清除显示内容
  digitalWrite(4, LOW);       //设置引脚4为低电平
  delay(2500);              //延时2.5秒

  // tm1637_second.init();
  // tm1637_second.set(BRIGHT_DARKEST); //BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7
  // tm1637_second.point(POINT_ON);
  // tm1637_second.display(TimeDisp_second);

  // digitalWrite(4,HIGH);
  // delay(2500);
  // tm1637_second.point(POINT_OFF);
  // tm1637_second.clearDisplay();
  // digitalWrite(4,LOW);
  // delay(2500);

  digitalWrite(1, LOW);   //设置引脚1为低电平
  digitalWrite(2, LOW);   //设置引脚2为低电平
  digitalWrite(3, LOW);   //设置引脚3为低电平
  digitalWrite(5, LOW);   //设置引脚5为低电平
  digitalWrite(6, LOW);   //设置引脚6为低电平
  digitalWrite(7, LOW);   //设置引脚7为低电平
  digitalWrite(8, LOW);   //设置引脚8为低电平
  digitalWrite(11, LOW);    //设置引脚11为低电平
  digitalWrite(12, LOW);    //设置引脚12为低电平
  digitalWrite(13, LOW);    //设置引脚13为低电平
  digitalWrite(15, LOW);    //设置引脚15为低电平
  digitalWrite(16, LOW);    //设置引脚16为低电平
  digitalWrite(17, LOW);    //设置引脚17为低电平
  digitalWrite(18, LOW);    //设置引脚18为低电平
}



void loop()
{
  digitalWrite(ledPin, LOW);    //将LED引脚设置为低电平，关闭LED
  digitalWrite(4, HIGH);    //将引脚4设置为高电平

  while (Serial.available()) //判断是否接收到数据
  {
    inputString = inputString + char(Serial.read());  //读取串口数据并添加到inputString中
    delay(2);
  }

  if (inputString != "") //如果收到数据  显示之
  {
    int brry = inputString.toInt();   //将输入字符串转换为整数
    Hour = brry / 100;    //计算小时
    Min = brry % 100;     //计算分钟
    Sec = 0;              //秒钟重置为0
    Serial.print("input number is:");   //打印输入的数字
    Serial.println(brry);   //打印输入的数字
    inputString = "";   //清空输入字符串
  }

  Sec++;    //每次循环增加秒钟计数

  if (Sec == 55) //给温度显示5秒
  {
    Sec = 0;    //秒钟归零
    Min++;    //分钟增加1

    TemperatureDisp[0] = 0;   //温度显示数组的第一个元素设置为0
    TemperatureDisp[1] = 0;   //温度显示数组的第二个元素设置为0
    TemperatureDisp[2] = temperature / 10;    //温度显示数组的第三个元素设置为温度的十位数
    TemperatureDisp[3] = temperature % 10;    //温度显示数组的第四个元素设置为温度的个位数
    tm1637.display(TemperatureDisp);    //显示温度
    tm1637.point(POINT_OFF);    //关闭小数点显示
    delay(5000);                                //显示五秒钟的温度

    //Serial.println(TimeDisp);    

    if (Min == 60)    
    {
      Min = 0;    //分钟归零
      Sec = 0;    //秒钟归零
      Hour++;     //小时增加1
      
      Serial.print("现在是北京时间: ");     //打印当前时间
      Serial.print(Hour);     //打印小时
      Serial.println(" 点整");          //整点报时
      
      if (Hour == 24)
      {
        Hour = 0;   //小时归零
        Sec = 0;    //秒钟归零
      }
    }
  }

  TimeDisp[0] = Hour / 10;    //将小时的十位数存入TimeDisp数组
  TimeDisp[1] = Hour % 10;      //将小时的个位数存入TimeDisp数组
  TimeDisp[2] = Min / 10;   //将分钟的十位数存入TimeDisp数组
  TimeDisp[3] = Min % 10;   //将分钟的个位数存入TimeDisp数组
  tm1637.point(POINT_ON);   //开启小数点显示
  tm1637.display(TimeDisp);   //显示时间
  delay(499); //这个用来调整时间精度
  tm1637.point(POINT_OFF);    //关闭小数点显示
  tm1637.display(TimeDisp);   //再次显示时间
  digitalWrite(4, LOW);   //将引脚4设置为低电平
  
  delay(498.5); //这个用来调整时间精度




}
