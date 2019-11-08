from random import randrange as rnd, choice
import tkinter as tk
import math
import time


class ball():

    balls = []

    def __init__(self, x=40, y=450, vx=0, vy=0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        vx - начальная скорость по горизонтали
        vy - начальная скорость по горизонтали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = vx
        self.vy = vy
        self.live = 7

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        l = 1
        self.vy += 1
        if self.y + self.r > 600:
            self.vy = -abs(self.vy)
            self.vy*=0.7
            self.vx*=0.8
            self.live -= 1
        
        self.x += self.vx
        self.y += self.vy
        if self.live <= 0 or self.x > 850:
            self.live = 0
            l = 0
        return l
        

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False




class gun():
    
    f2_on = 0
    f2_power = 10
    bullet = 0
    
    def __init__(self, x, y):
        self.an = 1
        self.x = x
        self.y = y

    def fire2_start(self, event):
        gun.f2_on = 1
        self.power_up()

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        gun.bullet += 1
        gun.f2_on = 0
        del_y = event.y-self.y
        del_x = event.x-self.x
        self.an = math.asin(del_y / (del_y**2 + del_x**2)**0.5)
        
    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.asin((event.y-self.y) / ((event.x-self.x)**2 + (event.y-self.y)**2)**0.5)
            
    def power_up(self):
        if gun.f2_on:
            if gun.f2_power < 100:
                gun.f2_power += 1
        else:
            gun.f2_power = 10



class target():

    def __init__(self):
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.v = rnd(100, 500)/100


    def move(self):
        if self.live:
            self.y += self.v
            if self.y + self.r > 600:
                self.v = -abs(self.v)
            if self.y < self.r:
                self.v = abs(self.v)
        



