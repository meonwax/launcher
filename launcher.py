import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import curses
import pygame


def init() -> bool:
    pygame.init()
    if pygame.joystick.get_count() < 1:
        print("No joystick/gamepad found")
        return False
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return True


message: str = "-"


# def print_message(stdscr):
#     if message:
#         stdscr.addstr(8, 0, message)


if init():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    menu = ["Entry 1", "Entry 2", "Entry 3", "Entry 4", "Entry 5"]
    selected = 0

    clock = pygame.time.Clock()
    while True:
        stdscr.clear()
        # print_message(stdscr)
        for i, entry in enumerate(menu):
            if i == selected:
                stdscr.addstr(i, 0, entry, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, entry)

        events = pygame.event.get()
        message = str(len(events))
        if len(events) > 0:
            event = events[0]
            if event.type == pygame.JOYBUTTONDOWN and event.button == 0:
                # print("a")
                break
            elif event.type == pygame.JOYAXISMOTION and event.axis == 1:
                if event.value < -0.5:
                    # print("up")
                    selected = (selected - 1) % len(menu)
                elif event.value > 0.5:
                    # print("down")
                    selected = (selected + 1) % len(menu)

        stdscr.refresh()
        clock.tick(25)

    print(f"You selected: {menu[selected]}")

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

pygame.quit()
