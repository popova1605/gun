from graphics import*

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class game():
    targets = [gr_target(canv, root), gr_target(canv, root)]
    g = gr_gun(canv, root, 20, 450)
    screen1 = canv.create_text(400, 300, text='', font='28')
    def __init__(self):
        self.new_t()
        canv.itemconfig(game.screen1, text='')
        canv.bind('<Button-1>', game.g.fire2_start)
        canv.bind('<ButtonRelease-1>', game.g.fire2_end)
        canv.bind('<Motion>', game.g.targetting)
    def new_t(self):
        game.targets[0].new_target()
        game.targets[1].new_target()
        game.targets[0].live = 1
        game.targets[1].live = 1
        game.targets[0].move()
        game.targets[1].move()

    def show_balls(self):
        return gr_ball.balls

    def clean_score(self):
        gun.bullet = 0

    def end(self):
        canv.itemconfig(game.screen1, text='Вы уничтожили цели за ' + str(gun.bullet) + ' выстрелов')
        canv.bind('<Button-1>', '')
        canv.bind('<ButtonRelease-1>', '')
    
def new_game(event=''):
    w = game()
    ball_list = w.show_balls()
    while game.targets[0].live or game.targets[1].live or ball_list:
        for b in ball_list:
            b.move()
            if b.hittest(game.targets[0]) and game.targets[0].live:
                game.targets[0].live = 0
                game.targets[0].hit()
            if b.hittest(game.targets[1]) and game.targets[1].live:
                game.targets[1].live = 0
                game.targets[1].hit()
            if game.targets[1].live == 0 and game.targets[0].live == 0:
                w.end()
        ball_list = w.show_balls()
        canv.update()
        time.sleep(0.03)
    
    canv.delete(gr_gun)
    w.clean_score()
    root.after(3000, new_game)

new_game()

root.mainloop()
