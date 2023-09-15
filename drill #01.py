import turtle
import keyboard

def move_forward():
    turtle.setheading(90)
    turtle.forward(50)

def move_backward():
    turtle.setheading(270)
    turtle.forward(50)

def move_left():
    turtle.setheading(180)
    turtle.forward(50)

def move_right():
    turtle.setheading(0)
    turtle.forward(50)

def reset_turtle():
    turtle.reset()

def main():
    turtle.shape('turtle')
    keyboard.add_hotkey('w', move_forward)
    keyboard.add_hotkey('s', move_backward)
    keyboard.add_hotkey('a', move_left)
    keyboard.add_hotkey('d', move_right)
    keyboard.add_hotkey('esc', reset_turtle)
    
    turtle.mainloop()

if __name__ == "__main__":
    main()

