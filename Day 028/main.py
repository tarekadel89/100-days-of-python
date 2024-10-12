import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
SECONDS_PER_MINUTE = 60

# ---------------------------- Global Variables ------------------------------- #
timer = None
current_round = 0
reset_flag = False
# ---------------------------- DOWN COUNTER ------------------------------- #

def down_counter(counter):
    global timer, current_round, reset_flag
    
    if reset_flag:
        return  # Stop the countdown if reset flag is True
    
    if counter >= 0:
        minutes, seconds = divmod(counter, 60)
        canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
        timer = my_window.after(1000, down_counter, counter - 1)
    else:
        # Timer has finished
        if timer_label.cget("text") == "Working":
            current_round += 1
            draw_checkmark(current_round)
            if current_round % 4 == 0:
                round_of_rest(LONG_BREAK_MIN)
            else:
                round_of_rest(SHORT_BREAK_MIN)
        else:
            if current_round % 4 == 0:
                # Clear checkmarks after a long break
                draw_checkmark(0)
            round_of_work()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def round_of_work():
    timer_label.config(text="Working")
    countdown = WORK_MIN * SECONDS_PER_MINUTE  # Convert minutes to seconds
    down_counter(countdown)
        
def round_of_rest(break_duration):
    timer_label.config(text="Resting")
    countdown = break_duration * SECONDS_PER_MINUTE  # Convert minutes to seconds
    down_counter(countdown)

# ---------------------------- UI SETUP ------------------------------- #
my_window = tk.Tk()
my_window.title("Pomodoro Timer")
my_window.config(padx=100, pady=50, bg=YELLOW)

### Timer label ###
timer_label = tk.Label()
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

### tomato canvas ###
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="Day 028/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

### start button ###
def start_button_clicked():
    global reset_flag, current_round
    if timer is not None:
        my_window.after_cancel(timer)  # Cancel any existing timer
    current_round = 0
    reset_flag = False
    round_of_work()

start_button = tk.Button()
start_button.config(text="Start", command=start_button_clicked, font=(FONT_NAME, 15, "bold"))
start_button.grid(row=2, column=0)

### reset button ###
def reset_button_clicked():
    global current_round, reset_flag, timer
    if timer is not None:
        my_window.after_cancel(timer)  # Cancel the timer
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(timer_text, fill="white")
    checkmarks_label.config(text="")
    timer_label.config(text="Timer")
    current_round = 0
    reset_flag = True

reset_button = tk.Button()
reset_button.config(text="Reset", command=reset_button_clicked, font=(FONT_NAME, 15, "bold"))
reset_button.grid(row=2, column=2)

### checkmark label ###
def draw_checkmark(round):
    checkmarks_str = ""
    for _ in range(round % 4):
        checkmarks_str += "✓"
    if round % 4 == 0 and round != 0:
        checkmarks_str += "✓✓✓✓"
    checkmarks_label.config(text=checkmarks_str, fg=GREEN, font=(FONT_NAME, 25, "normal"))   
        
checkmarks_label = tk.Label()
checkmarks_label.config(text="", fg=GREEN, font=(FONT_NAME, 25, "normal"))
checkmarks_label.grid(row=3, column=1)

my_window.mainloop()
