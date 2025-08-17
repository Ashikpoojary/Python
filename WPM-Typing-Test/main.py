# text-based user interfaces (TUIs) in the terminal. It provides a powerful set of tools to manage terminal screens, handle user input, and create interactive applications
import curses
# safely initializes and cleans up curses environment
from curses import wrapper 
import time
import wonderwords
from wonderwords import RandomSentence

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0, "Welcome to Speed-Type-Test") #(y row, x column, string)
    stdscr.addstr("\n Press any key to begin")
    stdscr.refresh
    stdscr.getkey() # wait for user input

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]  # checks if input is correct
        color = curses.color_pair(1) # if correct apply green text
        if char != correct_char:
            color = curses.color_pair(2) # if wrong apply red text
        stdscr.addstr(0,i, char, color )

def wpm_test(stdscr):
    s = RandomSentence()
    target_text = s.sentence()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (time_elapsed / 60) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Check if 'list' of characters in current_text forms the same string as target_text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
  
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK) #(id, foreground color, background color)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    # stdscr.addstr("Hello World", curses.color_pair(1)) # adding text in the screen
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2,0, "You completed Typing Test! Press any key to continue..." )
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)