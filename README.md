# PWM-Modulation-on-Raspberry-PI

 PWM veya Pulse Width Modulation Tekniği , frekansı sabit bir sinyalin 
 bir periyodu boyunca lojik-1(High) süresinin toplam periyoda 
 oranıyla verilerin iletildiği bir modülasyon tekniğidir. 
 PWM tekniğinde en önemli parametre Duty Cycle'dır.
 Duty Cycle =(lojik-1/period)100 olarak ifade edilir. Duty Cycle ile veri iletimi gerçekleşir.  _ | |_| duty Cycle=(2/4)100= %50
 
 |   |_| Duty Cycle(3/4)*100=%75
 PWM işleminde bir periyot sonundaki ortalama
 DC gerilim seviyesi lojik-1*duty cycle olaraak elde edilir.
 Örneğin elimizde lojik-1 3.3V olan %50 Duty Cycle sahip bir 
 sinyal olsun ortalama gerilim  1.65 V olur.
 Raspberry Pi'de PWM sinyallerin üretildiği iki kanal vardır.
 Her iki kanalında kendilerine bağlı ikişer pini vardır.
 Bu 4 pin
 GPIO12-->PWM0 32.pin
 GPIO18-->PWM0 12.pin
 GPIO13-->PWM1 33.pin
 GPIO19-->PWM1 35.pin
 Raspberry pi'de kullanılacak maksimum PWM frekansı 19.2 MHz'dir. 
 Projenin Videosu :
 [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://youtu.be/xHKdVIES5BU)
 
