import random
import curses
class Snake:
    x = 0
    y = 0
    body = []
    def __init__(self, scrnHeight, scrnWidth, k):
        x = scrnWidth//4
        y = scrnHeight//2
        #body = [ [y, x],[y, x-1],[y, x-2] ]
        self.key = k        
        self.body = [
            [y, x],
            [y, x-1],
            [y, x-2]
        ]

    def set_key(self, k):
        self.key = k

    def get_body(self):
        return self.body
    def move(self):
        new_head = [self.body[0][0], self.body[0][1]]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        self.body.insert(0, new_head)
        

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

key = curses.KEY_RIGHT

snk_x = sw//4
snk_y = sh//2
bod = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
snake = Snake(snk_x, snk_y, key)
food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)



while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    # print(snake.body)
    # quit()
    # print(snake.body[0][0])
    if snake.body[0][0] in [0, sh] or snake.body[0][1]  in [0, sw] or snake.body[0] in snake.body[1:]:
        curses.endwin()
        quit()
    # if bod[0][0] in [0, sh] or bod[0][1]  in [0, sw] or bod[0] in bod[1:]:
    #     curses.endwin()
    #     quit()

    snake.set_key(key)
    # new_head = [snake[0][0], snake[0][1]]

    # if key == curses.KEY_DOWN:
    #     new_head[0] += 1
    # if key == curses.KEY_UP:
    #     new_head[0] -= 1
    # if key == curses.KEY_LEFT:
    #     new_head[1] -= 1
    # if key == curses.KEY_RIGHT:
    #     new_head[1] += 1

    # snake.insert(0, new_head)
    snake.move()

    if snake.body[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake.body else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.body.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake.body[0][0], snake.body[0][1], curses.ACS_CKBOARD)
