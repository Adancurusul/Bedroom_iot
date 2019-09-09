# main.py -- put your code here!
from machine import Pin, Timer
import machine
p7 = Pin('X7',Pin.IN,Pin.PULL_UP)
p8 = Pin('X8',Pin.IN,Pin.PULL_UP)
p9= Pin('Y9',Pin.IN)
check_p =3
check_p1 = 3
i = 7.5    # 20ms内的0.5-2.5换成百分比形式就是2.5%-12.5%。7.5即为中间。
sw = pyb.Switch()    # 用板子上的按键控制
#tm2 = Timer(2, freq=100)
tm3 = Timer(5, freq=50)    # 选择定时器5，频率50hz
#led3 = tm2.channel(1, Timer.PWM, pin=Pin.cpu.A15)
#led3.pulse_width_percent(50)
a4 = tm3.channel(1, Timer.PWM, pin=Pin.cpu.A0)  # 选择通道1和定时器5对应引脚A0 X1
def check(t):
    global p7,p8,check_p,check_p1
    if (p7.value()==1 and p8.value()==0)or p9.value()==1 :
        check_p = 1
    elif p7.value()==0  :
        check_p =3

    #elif p9.value()==0:
    #    check_p1 =1
    #elif p9.value()==1 and check_p ==1:
    #    check_p1=3


tim = Timer(4)
#tim.init(period=200, mode=Timer.PERIODIC, callback=check)
tim.init(freq = 100, callback=check)



while True:
    sw_state = sw()

    if check_p ==1  :
        i += 0.01
        pyb.udelay(500)    # 延时500us，减点速
        if i > 12.0:
            i = 12.0



    elif check_p ==3 :
        i -= 0.01
        pyb.udelay(500)
        if i < 3.0:
            i = 3.0



    a4.pulse_width_percent(i)   # 控制占空比，20ms内0.5-2.5ms的百分比(不给满)