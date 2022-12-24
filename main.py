from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
time=''

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(time)
    
    '''timer reset to zero'''
    canvas.itemconfig(timer_text,text='00:00')
    '''timer label to say timer again'''
    timer.config(text='TIMER')
    '''reset check marks'''
    check_marks.config(text='')
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    reps+=1
    
    if reps%2!=0:
        count_down(work_sec)
        timer.config(text='WORK',font=(FONT_NAME,24,'bold'),fg=RED,bg=GREEN)
    elif reps%8==0:
        count_down(long_break_sec)
        timer.config(text='LONG BREAK',font=(FONT_NAME,24,'bold'),fg=PINK,bg=GREEN)
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text='SHORT BREAK',font=(FONT_NAME,24,'bold'),fg=YELLOW,bg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    min=count//60
    second=count%60
    if second<=9:
        second='0'+str(second)
    canvas.itemconfig(timer_text,text=f'{min}:{second}')
    if count>0:
        global time
        time=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=''
        work_sessions=reps//2
        for _ in range(work_sessions):
            mark+='✓'
        check_marks.config(text=mark)
        


    


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('pomodoro')
window.config(padx=100,pady=50,bg=GREEN)


#-----------CANVAS------------------#
canvas=Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
tomoto_img=PhotoImage(file='C:\\Python310\\codes\\projects\\pomodoro\\tomato.png')
canvas.create_image(100,112,image=tomoto_img)
timer_text=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)


#------ LABEL----------#
timer=Label(text='TIMER',font=(FONT_NAME,24,'bold'),fg=YELLOW,bg=GREEN)
timer.grid(column=1,row=0)
timer.config(padx=5,pady=5)

check_marks=Label(font=(FONT_NAME,24,'bold'),fg=YELLOW,bg=GREEN)
check_marks.grid(column=1,row=3)

#-------BUTTON--------#
start=Button(text='Start',bg=GREEN,fg=RED,highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset=Button(text='Reset',bg=GREEN,fg=RED,highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)




window.mainloop()
