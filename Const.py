import pygame as pg


class Const():
    def __init__(self):
        self.size = 500
        self.step = round(self.size / 3)
        self.screen = pg.display.set_mode((self.size, self.size))
        self.what_to_draw = "x"
        self.matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]


    def change(self, i, j, letter):
        self.matrix[i][j] = letter


    def analizing(self, i, j):
        if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2]:
            pg.draw.line(
                        self.screen, (255, 0, 0), 
                        (self.step * i + self.step // 2, 0), 
                        (self.step * i + self.step // 2, self.size), 10
                        )


        elif self.matrix[0][j] == self.matrix[1][j] == self.matrix[2][j]:
            pg.draw.line(
                        self.screen, (255, 0, 0), 
                        (0, self.step * j + self.step // 2), 
                        (self.size, self.step * j + self.step // 2), 10
                        )


        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]:
            pg.draw.line(
                        self.screen, (255, 0, 0),
                        (0, 0), (self.size, self.size), 10
                        )


        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]:
            pg.draw.line(
                        self.screen, (255, 0, 0),
                        (0, self.size), (self.size, 0), 10
                        )


    def drowing_field(self):
        for i in range(1, 3):
            pg.draw.line(self.screen, (0, 0, 0), (0, self.step * i), (self.size, self.step * i), 3)
            pg.draw.line(self.screen, (0, 0, 0), (self.step * i, 0), (self.step * i, self.size), 3)


    def game_process(self):
        x, y = pg.mouse.get_pos()


        x = self.step * (x // self.step)
        y = self.step * (y // self.step)


        if self.what_to_draw == "o":
            pg.draw.circle(self.screen, (0, 0, 0), (x + self.step // 2, y + self.step // 2), self.step // 2 - 12, 5)


            x //= self.step
            y //= self.step


            self.change(x, y, self.what_to_draw)
            self.analizing(x, y)


            self.what_to_draw = "x"


        else:
            pg.draw.line(self.screen, (0, 0, 0), (x + 12, y + 12), (x + self.step - 12, y + self.step - 12), 5)
            pg.draw.line(self.screen, (0, 0, 0), (x + 12, y + self.step - 12), (x + self.step - 12, y + 12), 5)


            x //= self.step
            y //= self.step


            self.change(x, y, self.what_to_draw)
            self.analizing(x, y)

            
            self.what_to_draw = "o"




figure = Const()