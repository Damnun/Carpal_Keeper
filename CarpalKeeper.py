import serial
import matplotlib.pyplot as plt
import numpy as np
import time



ser = serial.Serial(
    port = 'COM4',
    baudrate = 9600,
    )


plt.title("Graphs based on the time the pressure sensor receives")
plt.xlabel("Total time")
plt.ylabel("Pressed gain")

plt.xticks(np.arange(0,120,10)) # x축 눈금 0~600 범위, 20 간격
plt.yticks(np.arange(300,1001,100)) # y축 눈금 0~30범위, 1 간격
plt.xlim(0,120) # x축 값 제한 600
plt.ylim(0,1000) # y축 값 제한 5

continuedTime = 1;


xs = []
ys = []

while continuedTime != 120 :
    if ser.readable():
        res = ser.readline()
        a = (int)(res.decode()[:len(res)-1])
        print("센서값 : ", a, ", 시간 : ", continuedTime)
        xs.append(continuedTime)
        ys.append(a)
        plt.plot(xs, ys)
        plt.pause(0.1)
        #time.sleep(1)
        continuedTime = continuedTime + 1

plt.savefig('result.png')
plt.draw()
plt.show()
    




