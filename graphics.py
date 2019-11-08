from physics import*

class gr_ball(ball):

    balls = []

    def __init__(self, canv, x=40, y=450, vx=0, vy=0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        super().__init__(x,y,vx,vy)
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        gr_ball.balls += [self]
        self.canv = canv

    def set_coords(self):
        self.canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if super().move() == 0:
            self.disappear()
        self.set_coords()
        

    def disappear(self):
        self.canv.delete(self.id)
        gr_ball.balls.remove(self)



class gr_gun(gun):

    guns = []
    
    def __init__(self, canv, root, x, y):
        """"""
        super().__init__(x,y)
        self.id = canv.create_line(x, y, x+30, y-30, width=7)
        gr_gun.guns += [self]
        self.canv = canv
        self.root = root

    def fire2_start(self, event):
        super().fire2_start(event)
        self.targetting()

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global gr_ball
        super().fire2_end(event)
        gr_ball.balls += [gr_ball(self.canv, self.x + max(20, gun.f2_power) * math.cos(self.an),self.y + max(20, gun.f2_power) * math.sin(self.an),
                       0.5*gun.f2_power * math.cos(self.an), 0.5*gun.f2_power * math.sin(self.an))]
        self.targetting()
    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        super().targetting(event)
        if gun.f2_on:
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')
        self.canv.coords(self.id, self.x, self.y,
                    self.x + max(20, gun.f2_power) * math.cos(self.an),
                    self.y + max(20, gun.f2_power) * math.sin(self.an)
                    )

    def power_up(self):
        super().power_up()
        if gun.f2_on:
            self.canv.itemconfig(self.id, fill='orange')
            self.targetting()
            self.root.after(5, self.power_up)
        else:
            self.canv.itemconfig(self.id, fill='black')


class gr_target(target):

    points = 0
    targets = []
    
    def __init__(self, canv, root):
        super().__init__()
        self.id = canv.create_oval(0,0,0,0)
        self.canv = canv
        self.root = root
        self.new_target()
        if not gr_target.targets:
            self.id_points = canv.create_text(30,30,text = "0",font = '28')
        gr_target.targets += [self]
        self.move()

    def new_target(self):
        """ Инициализация новой цели. """
        super().new_target()
        x = self.x
        y = self.y
        r = self.r
        color = self.color = 'red'
        self.canv.coords(self.id, x-r, y-r, x+r, y+r)
        self.canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        self.canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )


    def move(self):
        if self.live:
            super().move()
            self.set_coords()
            self.root.after(50, self.move)
        

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.canv.coords(self.id, -10, -10, -10, -10)
        gr_target.points += points
        self.canv.itemconfig(gr_target.targets[0].id_points, text=gr_target.points)



