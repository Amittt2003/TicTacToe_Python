# Import and initialize the pygame library
import random
import time
import pygame
from Rectangle import Rectangle

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
RECT_HEIGHT = 100
GAME_SCREEN_HEIGHT = SCREEN_HEIGHT - RECT_HEIGHT
xCordLine = SCREEN_WIDTH / 3
yCordLine = GAME_SCREEN_HEIGHT / 3

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Tic Tac Toe")

# loading the images as python object
initiating_window = pygame.image.load(r"C:\Users\Amit\PycharmProjects\Amit\TicTacToe\files\launch_screen.png")
launch_window = pygame.image.load(r"C:\Users\Amit\PycharmProjects\Amit\TicTacToe\files\start_screen.jpg")
x_img = pygame.image.load(r"C:\Users\Amit\PycharmProjects\Amit\TicTacToe\files\x_img.png")
y_img = pygame.image.load(r"C:\Users\Amit\PycharmProjects\Amit\TicTacToe\files\o_img.png")

# resizing images
initiating_window = pygame.transform.scale(initiating_window, (SCREEN_WIDTH, SCREEN_HEIGHT))
launch_window = pygame.transform.scale(launch_window, (SCREEN_WIDTH, SCREEN_HEIGHT))
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(y_img, (80, 80))

# Define variables
rectangles = []
XO = 'X'
winner = None
font = pygame.font.SysFont('Zen Loop', 40)
btn_play_again = None
btn_main_menu = None
game_over = False
count = 0
game_mode = None
play_again = False
main_menu = False
running = True
btn_2players = None
btn_1players = None
player1 = False
player2 = False


def rectangles_initialize():
    # First row
    rectangles.append(Rectangle(0, 0, xCordLine, yCordLine, None))
    rectangles.append(Rectangle(xCordLine, 0, xCordLine, yCordLine, None))
    rectangles.append(Rectangle(2 * xCordLine, 0, xCordLine, yCordLine, None))

    # Second row
    rectangles.append(Rectangle(0, yCordLine, xCordLine, yCordLine, None))
    rectangles.append(Rectangle(xCordLine, yCordLine, xCordLine, yCordLine, None))
    rectangles.append(Rectangle(2 * xCordLine, yCordLine, xCordLine, yCordLine, None))

    # Third row
    rectangles.append(Rectangle(0, 2 * yCordLine, xCordLine, yCordLine, None))
    rectangles.append(Rectangle(xCordLine, 2 * yCordLine, xCordLine, yCordLine, None))
    rectangles.append(Rectangle(2 * xCordLine, 2 * yCordLine, xCordLine, yCordLine, None))


def display_buttons():
    global btn_play_again, btn_main_menu

    x_btn = SCREEN_WIDTH / 6
    y_btn = yCordLine + (yCordLine / 4)
    width_btn = 4 * (SCREEN_WIDTH / 6)
    height_btn = yCordLine / 2
    y_main_menu_btn = y_btn + height_btn + 50

    btn_play_again = Rectangle(x_btn, y_btn, width_btn, height_btn, None)
    btn_main_menu = Rectangle(x_btn, y_main_menu_btn, width_btn, height_btn, None)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x_btn, y_btn, width_btn, height_btn))
    screen.fill(pygame.Color("black"), (x_btn, y_btn, width_btn, height_btn))
    screen.blit(font.render("Play Again", True, (255, 255, 255)),
                (xCordLine, y_btn + (height_btn / 4), width_btn, height_btn))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x_btn, y_main_menu_btn, width_btn, height_btn))
    screen.fill(pygame.Color("black"), (x_btn, y_main_menu_btn, width_btn, height_btn))
    screen.blit(font.render("Main Menu", True, (255, 255, 255)),
                (xCordLine, y_main_menu_btn + (height_btn / 3), width_btn, height_btn))

    pygame.display.update()


def handle_buttons_click(mouse_x, mouse_y):
    global btn_play_again, btn_main_menu, play_again, main_menu, running, game_over

    if btn_play_again.is_inside_rectangle(mouse_x, mouse_y):
        play_again = True
        running = False
    elif btn_main_menu.is_inside_rectangle(mouse_x, mouse_y):
        main_menu = True
        running = False


def draw():
    pygame.draw.line(screen, (0, 0, 0), (xCordLine, 0), (xCordLine, GAME_SCREEN_HEIGHT), 7)
    pygame.draw.line(screen, (0, 0, 0), (2 * xCordLine, 0), (2 * xCordLine, GAME_SCREEN_HEIGHT), 7)
    pygame.draw.line(screen, (0, 0, 0), (0, yCordLine), (SCREEN_WIDTH, yCordLine), 7)
    pygame.draw.line(screen, (0, 0, 0), (0, 2 * yCordLine), (SCREEN_WIDTH, 2 * yCordLine), 7)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, GAME_SCREEN_HEIGHT, SCREEN_WIDTH, RECT_HEIGHT))


def draw_win(row):
    if row == 1:
        pygame.draw.line(screen, (0, 0, 0), (xCordLine / 3, yCordLine / 2),
                         (SCREEN_WIDTH - (xCordLine / 3), yCordLine / 2), 8)
        pygame.display.update()

    elif row == 2:
        pygame.draw.line(screen, (0, 0, 0), (xCordLine / 3, 3 * (yCordLine / 2)),
                         (SCREEN_WIDTH - (xCordLine / 3), 3 * (yCordLine / 2)), 8)
        pygame.display.update()

    elif row == 3:
        pygame.draw.line(screen, (0, 0, 0), (xCordLine / 3, GAME_SCREEN_HEIGHT - (yCordLine / 2)),
                         (SCREEN_WIDTH - (xCordLine / 3), GAME_SCREEN_HEIGHT - (yCordLine / 2)), 8)
        pygame.display.update()

    elif row == 4:
        pygame.draw.line(screen, (0, 0, 0), (xCordLine / 2, yCordLine / 3),
                         (xCordLine / 2, GAME_SCREEN_HEIGHT - (yCordLine / 3)), 8)
        pygame.display.update()

    elif row == 5:
        pygame.draw.line(screen, (0, 0, 0), (3 * (xCordLine / 2), yCordLine / 3),
                         (3 * (xCordLine / 2), GAME_SCREEN_HEIGHT - (yCordLine / 3)), 8)
        pygame.display.update()

    elif row == 6:
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH - (xCordLine / 2), yCordLine / 3),
                         (SCREEN_WIDTH - (xCordLine / 2), GAME_SCREEN_HEIGHT - (yCordLine / 3)), 8)
        pygame.display.update()

    elif row == 7:
        pygame.draw.line(screen, (0, 0, 0), (xCordLine / 3, yCordLine / 3),
                         (SCREEN_WIDTH - (xCordLine / 3), GAME_SCREEN_HEIGHT - (yCordLine / 3)), 8)
        pygame.display.update()

    elif row == 8:
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH - (xCordLine / 3), yCordLine / 3),
                         (xCordLine / 3, GAME_SCREEN_HEIGHT - (yCordLine / 3)), 8)
        pygame.display.update()


def display_turn():
    screen.fill(pygame.Color("black"), (0, GAME_SCREEN_HEIGHT, SCREEN_WIDTH, RECT_HEIGHT))
    screen.blit(font.render('{}` turn'.format(XO), True, (255, 255, 255)),
                (xCordLine + (xCordLine / 4), GAME_SCREEN_HEIGHT + (RECT_HEIGHT / 3)))
    pygame.display.update()


def display_winner():
    screen.fill(pygame.Color("black"), (0, GAME_SCREEN_HEIGHT, SCREEN_WIDTH, RECT_HEIGHT))
    screen.blit(font.render("{} Won!".format(winner), True, (255, 255, 255)),
                (xCordLine + (xCordLine / 4), GAME_SCREEN_HEIGHT + (RECT_HEIGHT / 3)))
    pygame.display.update()


def display_draw():
    screen.fill(pygame.Color("black"), (0, GAME_SCREEN_HEIGHT, SCREEN_WIDTH, RECT_HEIGHT))
    screen.blit(font.render("Draw!", True, (255, 255, 255)),
                (xCordLine + (xCordLine / 4), GAME_SCREEN_HEIGHT + (RECT_HEIGHT / 3)))
    pygame.display.update()


def handle_1player():
    global XO, count

    square = random.randint(0, 8)

    while rectangles[square].inside is not None:
        square = random.randint(0, 8)

    XO = 'X'
    count += 1
    x, y = rectangles[square].img_place()
    screen.blit(o_img, (x, y))
    rectangles[square].o_inside()
    display_turn()
    pygame.display.update()


def handle_mouse_click(mouse_x, mouse_y):
    global XO, count

    for rect in rectangles:
        if rect.is_inside_rectangle(mouse_x, mouse_y):
            x, y = rect.img_place()
            if XO == 'X' and rect.inside is None:
                XO = 'O'
                count += 1
                screen.blit(x_img, (x, y))
                rect.x_inside()
                display_turn()

            elif XO == 'O' and rect.inside is None:
                if player1:
                    pass
                else:
                    XO = 'X'
                    count += 1
                    screen.blit(o_img, (x, y))
                    rect.o_inside()
                    display_turn()

    pygame.display.update()


def check_winner():
    global winner

    if rectangles[0].inside is not None and rectangles[0].inside == rectangles[1].inside == rectangles[2].inside:
        if rectangles[0].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(1)
        return True

    elif rectangles[3].inside is not None and rectangles[3].inside == rectangles[4].inside == rectangles[5].inside:
        if rectangles[3].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(2)
        return True

    elif rectangles[6].inside is not None and rectangles[6].inside == rectangles[7].inside == rectangles[8].inside:
        if rectangles[6].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(3)
        return True

    elif rectangles[0].inside is not None and rectangles[0].inside == rectangles[3].inside == rectangles[6].inside:
        if rectangles[0].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(4)
        return True

    elif rectangles[1].inside is not None and rectangles[1].inside == rectangles[4].inside == rectangles[7].inside:
        if rectangles[1].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(5)
        return True

    elif rectangles[2].inside is not None and rectangles[2].inside == rectangles[5].inside == rectangles[8].inside:
        if rectangles[2].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(6)
        return True

    elif rectangles[0].inside is not None and rectangles[0].inside == rectangles[4].inside == rectangles[8].inside:
        if rectangles[0].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(7)
        return True

    elif rectangles[2].inside is not None and rectangles[2].inside == rectangles[4].inside == rectangles[6].inside:
        if rectangles[2].inside == 'x':
            winner = 'X'
        else:
            winner = 'O'

        display_winner()
        draw_win(8)
        return True

    else:
        return False


def draw_players_btn():
    global btn_2players, btn_1players

    x_1players_btn = SCREEN_WIDTH / 6
    y_1players_btn = SCREEN_HEIGHT / 5
    width_1players_btn = 4 * x_1players_btn
    height_1players_btn = y_1players_btn
    y_2players_btn = 3 * y_1players_btn

    btn_1players = Rectangle(x_1players_btn, y_1players_btn, width_1players_btn, height_1players_btn, None)
    btn_2players = Rectangle(x_1players_btn, y_2players_btn, width_1players_btn, height_1players_btn, None)

    # 1 Player Button
    pygame.draw.rect(screen, (153, 0, 153), pygame.Rect(x_1players_btn, y_1players_btn,
                                                        width_1players_btn, height_1players_btn))

    screen.fill(pygame.Color(153, 0, 153), (x_1players_btn, y_1players_btn, width_1players_btn, height_1players_btn))
    screen.blit(font.render("1 Player", True, (255, 255, 255)),
                (x_1players_btn + (width_1players_btn / 4), y_1players_btn + (height_1players_btn / 3),
                 width_1players_btn, height_1players_btn))

    # 2 Player Button
    pygame.draw.rect(screen, (153, 0, 153), pygame.Rect(x_1players_btn, y_2players_btn,
                                                        width_1players_btn, height_1players_btn))

    screen.fill(pygame.Color(153, 0, 153), (x_1players_btn, y_2players_btn, width_1players_btn, height_1players_btn))
    screen.blit(font.render("2 Players", True, (255, 255, 255)),
                (x_1players_btn + (width_1players_btn / 4), y_2players_btn + (height_1players_btn / 3),
                 width_1players_btn, height_1players_btn))


def handle_mouse_click2(mouse_x, mouse_y):
    global player1, player2, running

    if btn_1players.is_inside_rectangle(mouse_x, mouse_y):
        player1 = True
        running = False

    elif btn_2players.is_inside_rectangle(mouse_x, mouse_y):
        player2 = True
        running = False


def start_window():
    # Fill the background with white
    screen.fill((255, 255, 255))

    # displaying over the screen
    screen.blit(launch_window, (0, 0))

    draw_players_btn()

    pygame.display.update()

    pygame.display.flip()


def start_window_loop():
    global running, player1, player2

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    handle_mouse_click2(mouse_x, mouse_y)

    if player1 or player2:
        main()
    else:
        pygame.quit()


def start_screen():
    global player1, player2

    player1 = False
    player2 = False

    start_window()
    start_window_loop()


def game_window():
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    # displaying over the screen
    screen.blit(initiating_window, (0, 0))

    # updating the display
    pygame.display.update()

    time.sleep(1)

    # Fill the background with white
    screen.fill((255, 255, 255))

    draw()
    display_turn()

    # Flip the display
    pygame.display.flip()


def game():
    global game_over, count, running

    pygame.event.set_allowed(pygame.MOUSEMOTION)

    # Run until the user asks to quit
    game_over = False
    running = True
    while running:

        if count == 9 and game_over is False:
            display_draw()
            game_over = True

        if game_over:
            display_buttons()

        if player1 and XO == "O" and game_over is False:
            handle_1player()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running, game_over = False, False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if not game_over:
                        handle_mouse_click(mouse_x, mouse_y)
                        game_over = check_winner()
                    else:
                        handle_buttons_click(mouse_x, mouse_y)

    if game_over:
        if play_again:
            restart()
            main()
        elif main_menu:
            restart()
            start_screen()
    else:
        pygame.quit()


def restart():
    global winner, XO, rectangles, count, play_again, main_menu

    winner = None
    XO = 'X'
    rectangles = []
    count = 0

    play_again = False
    main_menu = False


def main():
    rectangles_initialize()
    game_window()
    game()


if __name__ == "__main__":
    start_screen()


class Game:
    def __init__(self, gameMode):
        global game_mode
        game_mode = gameMode
        main()
