--coding:utf-8--
 '''
 PWM 
 PWM veya Pulse Width Modulation Tekniği , frekansı sabit bir sinyalin 
 bir periyodu boyunca lojik-1(High) süresinin toplam periyoda 
 oranıyla verilerin iletildiği bir modülasyon tekniğidir. 
 PWM tekniğinde en önemli parametre Duty Cycle'dır.
 Duty Cycle =(lojik-1/period)100 olarak ifade edilir. Duty Cycle ile veri iletimi gerçekleşir.  _ |  |_| duty Cycle=(2/4)100= %50
 
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
 '''
 import RPi.GPIO as GPIO
 import time
 GPIO.setwarnings(False)
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(32,GPIO.OUT)
 pwm_32 = GPIO.PWM(32,1500) 
 32 pinde 1.5KHz frekansa sahip pwm tanımlandı
 ChangeFrequency(frequency) komutu ile pwm frekansı(Hz) değiştirebiliriz.
 pwm_32.start(0)#%0 Duty Cycle ile pwm başlatıldı.
 time.sleep(1)#1 sn beklenir.
 while True:
     #pwm duty Cycle oranı  0'dan 100'e kadar 10ar 10ar arttırılır.
     for duty in range(0,100,10):
         pwm_32.ChangeDutyCycle(duty) 
         time.sleep(0.5)
     time.sleep(2)
     #pwm duty Cycle oranı 100'den 0'a kadar 10ar 10ar azalttık.
     for duty in range(100,0,-10):
         pwm_32.ChangeDutyCycle(duty)
         time.sleep(0.5)
     time.sleep(2)  
