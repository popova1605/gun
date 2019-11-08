from graphics import*

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


t1 = gr_target(canv, root)
t2 = gr_target(canv, root)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gr_gun(canv, root, 20, 450)


def new_game(event=''):
    global gr_gun, t1, t2, screen1, ball, canv
    canv.itemconfig(screen1, text='')
    t1.new_target()
    t2.new_target()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    t1.move()
    t2.move()
    while t1.live or gr_ball.balls:
        for b in gr_ball.balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t2.live == 0 and t1.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(gun.bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
    gun.bullet = 0
    canv.delete(gr_gun)
    
    root.after(3000, new_game)

new_game()

root.mainloop()
