import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import numpy as np
import os
import serial
import pylab
from tkinter import *

root = Tk()
b1 = Button(root, text="Неравномерное движение", width=30, height=3)
b2 = Button(root, text="Равномерное движение", width=30, height=3)
b3 = Button(root, text="Только построение графика", width=30, height=3)
fig, ax1 = pylab.subplots()
xval2 = []
yval2 = []
xval = []
yval = []
p = [0.0]

def graph_display():
    ax1.set_title('График пройденного расстояния от времени')
    ax1.set_ylabel('Расстояние в сантиметрах до камеры')
    ax1.set_xlabel('Пройденное время в секундах')

def button_initialization(btn, function):
    btn.config(command = function)
    btn.pack()
    
def refresh(i):
    ser = serial.Serial('COM5', 9600)
    print("connected to: " + ser.portstr)
    ser.flushInput()
    s = ser.readline().decode('utf-8')
    t = ''
    for i in s:
        if i.isdigit():
            t += i
    if t == '':
        return
    xval.append(p[0])
    yval.append(int(t))
    p[0] += 0.3
    ax1.clear()
    ax1.plot(xval2, yval2)
    ax1.plot(xval, yval)
    graph_display()
    pylab.legend(("заданный пример", "график реального движения"))

def uneven_test():
    file = open("test_uneven_movement.txt", "r")
    address = "tests_uneven\\" + file.readline() + ".txt"
    if(not os.path.exists(address)):
        print("Такого пути файла " + address + " в папке tests_uneven не существует")
        exit(0)
    data_from_generator = open(address, "r").read()
    lines = data_from_generator.split("\n")
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xval2.append(int(x))
            yval2.append(int(y))
    ax1.plot(xval2, yval2)
    graph_display()
    ani = animation.FuncAnimation(fig, refresh, interval=300)
    plt.show()

def even_test():
    file = open("test_even_movement.txt", "r")
    address = "tests_even\\" + file.readline() + ".txt"
    if(not os.path.exists(address)):
        print("Такого пути файла " + address + " в папке tests_even не существует")
        exit(0)
    data_from_generator = open(address, "r").read()
    lines = data_from_generator.split("\n")
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xval2.append(int(x))
            yval2.append(int(y))
    ax1.plot(xval2, yval2)
    graph_display()
    ani = animation.FuncAnimation(fig, refresh, interval=300)
    plt.show()

def only_one():
    ani = animation.FuncAnimation(fig, refresh, interval=300)
    plt.show()
    
def main():
    button_initialization(b1, uneven_test)
    button_initialization(b2, even_test)
    button_initialization(b3, only_one)
    root.mainloop()
main()
