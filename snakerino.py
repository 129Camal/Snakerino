import curses
import random

stdscr = curses.initscr()
key = curses.KEY_RIGHT
score = 0
curses.curs_set(0)

# buscar o tamanho do terminal
y, x = stdscr.getmaxyx()

# criar a nova janela com os tamanhos obtidos
screen = curses.newwin(y, x, 0, 0)

# ativar o keypad
screen.keypad(True)

# definir timeout
screen.timeout(150)

# posicao inicial da cobrinha
snake_x = x / 4
snake_y = y / 4

# cobrinha toda
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# posicao da primeira comida
food = [y / 2, x / 2]

screen.addch(food[0], food[1], '*')

while True:
    next_key = screen.getch()

    # verificar o que recebeu no getch
    key = key if next_key == -1 else next_key

    # casos de saida do jogo
    if snake[0][0] in [0, y] or snake[0][1] in [0, x] or snake[0] in snake[1:]:
        curses.endwin()
        break

    head = [snake[0][0], snake[0][1]]

    # meter com a cabeca da cobra
    if key == curses.KEY_DOWN:
        head[0] += 1
    if key == curses.KEY_UP:
        head[0] -= 1
    if key == curses.KEY_LEFT:
        head[1] -= 1
    if key == curses.KEY_RIGHT:
        head[1] += 1

    # inserir a nova posicao da cabeca no array
    snake.insert(0, head)

    # se a nova posicao for a posicao da comida, cria uma comida nova, se nao coloca um espaco na ultima posicao da cobra
    if snake[0] == food:
        food = None
        score += 1
        while food is None:
            new_food = [
                random.randint(1, y - 1),
                random.randint(1, x - 1)
            ]
            food = new_food if new_food not in snake else None
        screen.addch(food[0], food[1], '*')

    else:
        tail = snake.pop()
        screen.addch(tail[0], tail[1], ' ')

    screen.addch(snake[0][0], snake[0][1], '#')

print "Score: ", score




