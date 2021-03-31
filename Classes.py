import pygame as pg


size_main_game = (1000, 700)
size_start_menu = (500, 500)
start_menu = pg.display.set_mode(size_start_menu)
main_game = None
game_started = False
quantity_of_buttons = 2
all_buttons = list()
step = 0


class Field():
    global size_main_game, main_game


    def __init__(self):
        self.flag_for_work, self.show_must_go_on = False, True
        self.quantity = 3
        self.step = round(size_main_game[1] / self.quantity)
        self.what_to_draw = "x"
        self.matrix = list()
        self.space = size_main_game[0] - size_main_game[1]
        self.x, self.y = "none", "none"
    

    def creat_a_table(self):
        for i in range(0, self.quantity + 1):
            pg.draw.line(main_game, (0, 0, 0), 
                        (self.space, self.step * i), 
                        (size_main_game[0], self.step * i), 3
                        )
            pg.draw.line(main_game, (0, 0, 0), 
                        (self.step * i + self.space, 0), 
                        (self.step * i + self.space, size_main_game[1]), 3
                        )


    def creat_matrix(self):
        symbol = 1
        one_line = list()
        for i in range(self.quantity):
            for j in range(self.quantity):
                one_line.append(symbol)
                symbol += 1
            self.matrix.append(one_line)
            one_line = list()


    def click(self):
        self.x, self.y = pg.mouse.get_pos()
        self.flag_for_work = True


    def main_process(self):
        self.x = self.step * ((self.x - self.space) // self.step) + self.space
        self.y = self.step * (self.y // self.step)
        self.flag_for_work = False
        

        if self.what_to_draw == "x":
            pg.draw.line(main_game, 
                        (0, 0, 0), 
                        (self.x + 12, self.y + 12), 
                        (self.x + self.step - 12, self.y + self.step - 12), 5
                        )
            pg.draw.line(main_game, 
                        (0, 0, 0), 
                        (self.x + 12, self.y + self.step - 12), 
                        (self.x + self.step - 12, self.y + 12), 5
                        )
            self.x = (self.x - self.space) // self.step
            self.y //= self.step
            self.matrix[self.y][self.x] = self.what_to_draw
            self.what_to_draw = "o"
        else:
            pg.draw.circle(
                        main_game, (0, 0, 0), 
                        (self.x + self.step // 2, self.y + self.step // 2), 
                        self.step // 2 - 12, 5
                        )
            self.x = (self.x - self.space) // self.step
            self.y //= self.step
            self.matrix[self.y][self.x] = self.what_to_draw
            self.what_to_draw = "x"


    def check_for_winner(self):
        def check_line(matrix, i, quantity):
            if matrix[i].count(matrix[i][0]) == quantity:
                return True
            else:
                return False


        def check_column(matrix, j, quantity):
            flag = True
            for k in range(quantity - 1):
                if matrix[k][j] != matrix[k + 1][j]:
                    flag = False
                    break
            return flag


        def check_main_diag(matrix, quantity):
            flag = True
            for k in range(quantity - 1):
                if matrix[k][k] != matrix[k + 1][k + 1]:
                    flag = False
            return flag


        def check_sec_diag(matrix, quantity):
            flag = True
            for k in range(quantity - 1):
                if matrix[quantity - 1 - k][k] != matrix[quantity - k - 2][k + 1]:
                    flag = False
            return flag


        if check_column(self.matrix, self.x, self.quantity):
            pg.draw.line(
                        main_game, (255, 0, 0), 
                        (self.step * self.x + self.step // 2, 0), 
                        (self.step * self.x + self.step // 2, size_main_game[0]), 10
                        )
            self.show_must_go_on = False
            self.creat_matrix()
        elif check_line(self.matrix, self.y, self.quantity):
            pg.draw.line(
                        main_game, (255, 0, 0), 
                        (self.space, self.step * self.y + self.step // 2), 
                        (size_main_game[0], self.step * self.y + self.step // 2), 10
                        )
            self.show_must_go_on = False
            self.creat_matrix()
        elif check_main_diag(self.matrix, self.quantity):
            pg.draw.line(
                        main_game, (255, 0, 0),
                        (self.space, 0), (size_main_game[0], size_main_game[1]), 10
                        )
            self.show_must_go_on = False
            self.creat_matrix()
        elif check_sec_diag(self.matrix, self.quantity):
            pg.draw.line(
                        main_game, (255, 0, 0),
                        (0, size_main_game[1]), (size_main_game, 0), 10
                        )
            self.show_must_go_on = False
            self.creat_matrix()


class Button():
    global start_menu, size_start_menu, quantity_of_buttons, step, main_game, size_main_game


    def __init__(self, text, sizes):
        self.name = text
        self.size_x, self.size_y = sizes
        self.centerX = (size_start_menu[0] - self.size_x) // 2 + self.size_x // 2
        self.centerY = 0
        self.increase = False
        
        
    def creat_button(self):
        pg.draw.rect(
                    start_menu, (0, 0, 0), 
                    (self.centerX - self.size_x // 2, self.centerY - self.size_y // 2, self.size_x, self.size_y), 5
                    )
        pixels = self.size_y - 2 * 10
        font = pg.font.SysFont(None, pixels)
        text = font.render(self.name, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.centerX, self.centerY))
        start_menu.blit(text, text_rect)


    def increase_sizes(self):
        pg.draw.rect(
                    start_menu, (255, 255, 255),
                    (self.centerX - self.size_x // 2 - 2, self.centerY - self.size_y // 2 - 2, self.size_x + 6, self.size_y + 6)
                    )
        self.size_y = round(self.size_y * 1.1)
        self.size_x = round(self.size_x * 1.1)


    def decrease_sizes(self):
        pg.draw.rect(
                    start_menu, (255, 255, 255),
                    (self.centerX - self.size_x // 2 - 2, self.centerY - self.size_y // 2 - 2, self.size_x + 6, self.size_y + 6)
                    )
        self.size_x = round(self.size_x * 0.90909090)
        self.size_y = round(self.size_y * 0.90909090)


    def check(self):
        x, y = pg.mouse.get_pos()
        if self.centerX - self.size_x // 2 < x < self.centerX + self.size_x // 2:
            if self.centerY - self.size_y // 2 < y < self.centerY + self.size_y // 2:
                return True
            else:
                return False
        else:
            return False




field = Field()


sizes = (200, 100)
start_button = Button("start", sizes)
all_buttons.append(sizes[1])


sizes = (200, 100)
exit_button = Button("exit", sizes)
all_buttons. append(sizes[1])


step = (size_start_menu[1] - sum(all_buttons)) // (quantity_of_buttons + 1)


start_button.centerY = step + start_button.size_y // 2
exit_button.centerY = step * 2 + start_button.size_y + exit_button.size_y // 2


