from ursina import *

app = Ursina()

window.borderless = False  # lets the user move the window
window.color = color._20  # makes the background color black

page = 'Home'  # page variable is set as 'Home'
page_text = Text(text=page, origin=(0, 0), y=0.4, scale=2, background=True)


def change_page(goto_page):
    global page
    page = goto_page


class Button_Class:  # making a button class
    def __init__(self, x, y, size, color, text, goto_page, page_condition):  # defining everything inside this button class
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.text = text
        self.goto_page = goto_page
        self.page_condition = page_condition
        self.button = Button(text=self.text, color=self.color, scale=self.size, origin=(0, 0), x=10000, y=self.y, on_click=lambda: change_page(self.goto_page))

    def actions(self):
        global page
        if page in self.page_condition:
            self.button.x = self.x
        else:
            self.button.x = 10000


Home_Button = Button_Class(-0.7, 0.4, 0.15, color.blue, 'Home', 'Home', ['Calculator', 'Math Problem Solver', 'Simultaneous Equations', 'Quadratic Equations', 'Sorting Algorithm', 'Clicking Game'])  # define Home button
Math_Button = Button_Class(-0.3, 0, 0.2, color.orange, 'Math Problem\nSolver', 'Math Problem Solver', ['Home', 'Calculator', 'Simultaneous Equations', 'Quadratic Equations'])  # define Math Problem Solver button
Calculator_Button = Button_Class(-0.3, 0, 0.2, color.orange, 'Calculator', 'Calculator', ['Math Problem Solver'])  # define Calculator button
Simultaneous_Button = Button_Class(0, 0, 0.2, color.orange, 'Simultaneous\nEquations', 'Simultaneous Equations', ['Math Problem Solver'])  # define Simultaneous equation button
Quadratic_Button = Button_Class(0.3, 0, 0.2, color.orange, 'Quadratic\nEquations', 'Quadratic Equations', ['Math Problem Solver'])  # define Quadratic equation button
Sort_Button = Button_Class(0, 0, 0.2, color.green, 'Sorting\nAlgorithm', 'Sorting Algorithm', ['Home'])  # define Sorting Algorithm button
Game_Button = Button_Class(0.3, 0, 0.2, color.red, 'Clicking Game', 'Clicking Game', ['Home'])


def update():  # repeats every frame
    global page_text
    global page
    page_text.text = page
    Home_Button.actions()
    Calculator_Button.actions()
    Simultaneous_Button.actions()
    Quadratic_Button.actions()
    Sort_Button.actions()
    Game_Button.actions()
    if page in ['Calculator', 'Simultaneous Equations', 'Quadratic Equations']:
        Math_Button.button.x = -0.5
        Math_Button.button.y = 0.4
        Math_Button.button.scale = 0.15
    elif page == 'Home':
        Math_Button.button.x = -0.3
        Math_Button.button.y = 0
        Math_Button.button.scale = 0.2
    else:
        Math_Button.actions()


app.run()  # needed to run the program
