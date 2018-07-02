import curses
import random
import time

stdscr = curses.initscr()
key = curses.KEY_RIGHT
score = 0
curses.curs_set(0)

y, x = stdscr.getmaxyx()

screen = curses.newwin(y, x, 0, 0)
screen.border(0)
screen.nodelay(1)
screen.keypad(True)


screen.addstr(0, 2, 'Score : ' + str(score) + ' ')  # Printing 'Score' and
screen.addstr(0, 27, ' SNAKErino by Camal')

snake_x = x / 4
snake_y = y / 4

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

screen.timeout(150 - (len(snake)/5 + len(snake)/10)%120)

food = [y / 2, x / 2]

screen.addch(food[0], food[1], '*')

while True:
    olderkey = key

    next_key = screen.getch()

    key = key if next_key == -1 else next_key

    if snake[0][0] in [1, y - 2] or snake[0][1] in [1, x - 2] or snake[0] in snake[1:]:

        stdscr.addstr(y / 2, x / 8, 'YOU LOSS! Press R to Retry or another key to Quit, then press Enter!')

        desire = stdscr.getstr(3 * y / 4, x / 2)

        if desire == 'r' or desire == 'R':
            pass
            snake = [
                [snake_y, snake_x],
                [snake_y, snake_x - 1],
                [snake_y, snake_x - 2]
            ]
            score = 0
            key = curses.KEY_RIGHT
            screen.erase()
            screen.border(0)
            screen.addch(y / 2, x / 2, '*')
            screen.addstr(0, 2, 'Score : ' + str(score) + ' ')
            screen.addstr(0, 27, ' SNAKErino by Camal')
            screen.timeout(150 - (len(snake) / 5 + len(snake) / 10) % 120)

            food = [y / 2, x / 2]

        else:
            curses.endwin()
            break

    head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        head[0] += 1
    if key == curses.KEY_UP:
        head[0] -= 1
    if key == curses.KEY_LEFT:
        head[1] -= 1
    if key == curses.KEY_RIGHT:
        head[1] += 1

    if head != snake[1]:
        snake.insert(0, head)

        if snake[0] == food:
            food = None
            score += 1
            screen.addstr(0, 2, 'Score : ' + str(score) + ' ')

            while food is None:
                new_food = [
                    random.randint(2, y - 3),
                    random.randint(1, x - 2)
                ]
                food = new_food if new_food not in snake else None
            screen.addch(food[0], food[1], '*')

        else:
            tail = snake.pop()
            screen.addch(tail[0], tail[1], ' ')

        screen.addch(snake[0][0], snake[0][1], '#')
    else:
        key = olderkey
