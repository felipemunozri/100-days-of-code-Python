from game import SnakeGame, Screen
# Exception-free version


def reset(scr):
    scr.clearscreen()
    main()


def main():
    try:
        screen = Screen()
        SnakeGame().play()

        # Restart game
        screen.onkey(lambda: reset(screen), 'Return')  # 'enter' key
        screen.mainloop()

    except Exception as e:
        # print(e)
        pass


if __name__ == '__main__':
    main()
