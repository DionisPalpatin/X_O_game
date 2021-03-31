import pygame as pg
import Classes


pg.init()
Classes.start_menu.fill((255, 255, 255))
Classes.field.creat_matrix()


Classes.start_button.creat_button()
Classes.exit_button.creat_button()
pg.display.update()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if not Classes.game_started:
                if Classes.start_button.check():
                    pg.quit()
                    Classes.main_game = pg.display.set_mode(Classes.size_main_game)
                    Classes.main_game.fill((255, 255, 255))
                    Classes.field.creat_a_table()
                    pg.display.update()
                    Classes.game_started = True
                elif Classes.exit_button.check():
                    pg.quit()
                    exit()
            else:
                Classes.field.click()
    

    if not Classes.game_started:
        if Classes.start_button.check() and not Classes.start_button.increase:
            Classes.start_button.increase_sizes()
            Classes.start_button.creat_button()
            pg.display.update()
            Classes.start_button.increase = True
        elif not Classes.start_button.check() and Classes.start_button.increase:
            Classes.start_button.decrease_sizes()
            Classes.start_button.creat_button()
            pg.display.update()
            Classes.start_button.increase = False
        elif Classes.exit_button.check() and not Classes.exit_button.increase:
            Classes.exit_button.increase_sizes()
            Classes.exit_button.creat_button()
            pg.display.update()
            Classes.exit_button.increase = True
        elif not Classes.exit_button.check() and Classes.exit_button.increase:
            Classes.exit_button.decrease_sizes()
            Classes.exit_button.creat_button()
            pg.display.update()
            Classes.exit_button.increase = False
    elif Classes.field.flag_for_work and Classes.field.show_must_go_on:
        Classes.field.main_process()
        Classes.field.check_for_winner()
        pg.display.update()