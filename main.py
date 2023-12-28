# git add main.py
# git commit -m "seventh commit"
# git push origin master

# git pull origin master (기존 commit 해놓은 코드 가져오기)

from ursina import *  # meaning that you import Ursina and you don't have to type Ursina.name of the function every time
# you want to use a function in Ursina. e.g. window.size = (1580, 720)

import random  # meaning that you import an internal library named random, and you have to type random.name of the
# function every time to use the function. e.g. random.randint(1, 15)

app = Ursina()

window.borderless = False  # lets the user move the window
window.color = color.dark_gray  # makes the background color dark gray
window.size = (1080, 720)  # size of window

home_text = Text(text="Due to lack of my programming skills, this program doesn't accept decimals or fractions: "
                      "only integers. ", origin=(0, 0), y=0.25)
page = 'Home'
page_text = Text(text=page, origin=(0, 0), y=0.4, scale=2)  # current page

sort_text = Text(text='', origin=(0, 0), y=15, wordwrap=10, scale=1)  # answer of sort
sort_explanation_text = Text(text='1. Type in any sets of integers, and click any sorting method.     \n2. The program '
                                  'will sort the numbers in ascending order.          \n3. Type a comma in between '
                                  "numbers, and don't put in letters.\nEx) 4, 1, -2, 4, 0", origin=(0, 0), y=15)

symbol = 'Select symbol'
symbol_text = Text(text=symbol, origin=(0, 0), y=15, scale=1)  # text showing the current symbol (calculator)
calculator_text = Text(text='', origin=(0, 0), y=15, scale=1)  # answer of calculator

simultaneous_equation_text = Text(text='', origin=(0, 0), y=15, scale=1)  # answer of simultaneous equation
simultaneous_equation_equation_text = Text(text='       x +        y =        \n\n\n       x +        y =        ',
                                           origin=(0, 0), y=15, scale=2)

quadratic_equation_text = Text(text='', origin=(0, 0), y=15, scale=1)  # answer of quadratic equation
quadratic_equation_equation_text = Text(text='       x² +        x =        ', origin=(0, 0), y=15, scale=2)


def change_page(goto_page):  # changing page function
    global page
    page = goto_page


def make_number_2dp(inp):  # rounding every number to its 2nd decimal place or less
    if inp == int(inp):
        inp = str(format(inp, '.0f'))
    elif inp * 10 == int(inp * 10):
        inp = str(format(inp, '.1f'))
    else:
        inp = str(format(inp, '.2f'))
    return inp


def bubble_sort(given_list):  # bubble sort function
    global page
    if given_list == 'Type here':
        sort_text.text = "Click on the black button and type a number set"
        page = 'Sort Result'
        return
    try:
        given_list = [int(x) for x in given_list.split(',')]
    except ValueError:
        sort_text.text = 'Error'
        page = 'Sort Result'
        Sort_input_number.text = 'Type here'
        return
    l = len(given_list) - 1
    for i in range(l):
        for j in range(l):
            if given_list[j] > given_list[j + 1]:
                temp = given_list[j]
                given_list[j] = given_list[j + 1]
                given_list[j + 1] = temp

    sort_text.text = 'Result: ' + str(given_list)
    page = 'Sort Result'


def quick_sort_func(given_list):  # actual quick sort function
    if len(given_list) <= 1:
        return given_list

    pivot = random.choice(given_list)
    small = []
    equal = []
    big = []
    for x in given_list:
        if x < pivot:
            small.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            big.append(x)

    return quick_sort_func(small) + equal + quick_sort_func(big)


def quick_sort(given_list):
    global page
    if given_list == 'Type here':
        sort_text.text = "Click on the black button and type a number set"
        page = 'Sort Result'
        return
    try:
        given_list = [int(x) for x in given_list.split(',')]
    except ValueError:
        sort_text.text = 'Error'
        page = 'Sort Result'
        Sort_input_number.text = 'Type here'
        return

    result_list = quick_sort_func(given_list)

    sort_text.text = 'Result: ' + str(result_list)
    page = 'Sort Result'


def counting_sort(given_list):  # counting sort function
    global page
    if given_list == 'Type here':
        sort_text.text = "Click on the black button and type a number set"
        page = 'Sort Result'
        return
    try:
        given_list = [int(x) for x in given_list.split(',')]
    except ValueError:
        sort_text.text = 'Error'
        page = 'Sort Result'
        Sort_input_number.text = 'Type here'
        return

    m = min(given_list)
    M = max(given_list)
    if M-m >= 5000000:
        sort_text.text = ('Error - given range of numbers might be too big to be\nsorted using counting sort method.'
                          '\nTry another sorting method.')
        page = 'Sort Result'
        return
    index_list = list(range(m, M+1))
    result_list = []
    n_list = [0]*len(index_list)
    for n in given_list:
        ind = index_list.index(n)
        n_list[ind] += 1
    for i in range(len(n_list)):
        for j in range(n_list[i]):
            result_list.append(i+m)

    sort_text.text = 'Result: ' + str(result_list)
    page = 'Sort Result'


def calculator_symbol_selection(symb):
    global symbol
    symbol = symb


def calculator(given):
    global symbol
    x, y = given
    answer = 0
    if symbol == 'Select symbol':
        calculator_text.text = 'Click an operation to select that operation.'
        calculator_text.y = -0.3
        return

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        calculator_text.text = 'Click the black buttons and type in a number to calculate.'
        calculator_text.y = -0.3
        return

    if symbol == '+':
        answer = x+y
    elif symbol == '-':
        answer = x-y
    elif symbol == '×':
        answer = x*y
    elif symbol == '÷':
        answer = x/y
    elif symbol == 'x^y':
        answer = x**y

    calculator_text.text = str(make_number_2dp(answer))
    calculator_text.y = -0.3
    return


def simultaneous_equation(given):
    a, b, c, d, e, f = given  # ax + by = c, dx + ey = f
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
    except ValueError:
        simultaneous_equation_text.text = 'Click the black empty buttons and put in a number to calculate.'
        simultaneous_equation_text.y = -0.3
        return
    if a == 0 and d == 0:
        simultaneous_equation_text.text = 'Variable x is undefined'
        simultaneous_equation_text.y = -0.3
        return
    elif b == 0 and e == 0:
        simultaneous_equation_text.text = 'Variable y is undefined'
        simultaneous_equation_text.y = -0.3
        return

    # ax + by = c, dx + ey = f
    #  adx + bdy = cd, adx + aey = af
    #  (bd-ae)y = cd-af
    #  y = (cd-af)/(bd-ae)

    if b*d-a*e != 0:
        y = (c*d-a*f)/(b*d-a*e)
    elif c*d-a*f == 0:  # and b*d-a*e == 0
        simultaneous_equation_text.text = 'There are infinitely many solutions'
        simultaneous_equation_text.y = -0.3
        return
    else:  # if c*d-a*f != 0 and b*d-a*e == 0
        simultaneous_equation_text.text = 'There are no solutions'
        simultaneous_equation_text.y = -0.3
        return

    #  ax = c-by, x=(c-by)/a

    if a != 0:
        x = (c-b*y)/a
    else:
        x = (f-e*y)/d

    x = make_number_2dp(x)

    y = make_number_2dp(y)

    simultaneous_equation_text.text = f'x = {x}, y = {y}'
    simultaneous_equation_text.y = -0.3


def quadratic_equation(given):  # rounded to 2dp
    a, b, c = given
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        quadratic_equation_text.text = 'Click the black empty buttons and put in a number to calculate.'
        quadratic_equation_text.y = -0.3
        return
    if a == 0:
        if b != 0:
            x = make_number_2dp(c/b)
            quadratic_equation_text.text = f'Not a quadratic equation. x = {x}'
            quadratic_equation_text.y = -0.3
            return  # not a quadratic equation
        else:
            quadratic_equation_text.text = 'Cannot solve for x.'
            quadratic_equation_text.y = -0.3
            return
    if b*b < 4*a*c:
        quadratic_equation_text.text = 'No real solution'
        quadratic_equation_text.y = -0.3
        return  # no real solution
    if b*b == 4*a*c:
        x = make_number_2dp(-b/(2*a))
        quadratic_equation_text.text = f'x = {x} (multiple root)'
        quadratic_equation_text.y = -0.3
        return  # one solution
    x1 = make_number_2dp((-b + (b*b - 4*a*c) ** 0.5) / (2 * a))
    x2 = make_number_2dp((-b - (b*b - 4*a*c) ** 0.5) / (2 * a))
    if x1 < x2:
        temp = x1
        x1 = x2
        x2 = temp

    quadratic_equation_text.text = f'x = {x1}, x = {x2}'
    quadratic_equation_text.y = -0.3
    return  # two solutions


class Normal_Button:
    def __init__(self, x, y, size, color, text, page_condition):  # defining everything inside this button class
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.text = text
        self.page_condition = page_condition
        self.button = Button(text=self.text, color=self.color, scale=self.size, origin=(0, 0), x=15, y=self.y)

    def actions(self):
        global page
        if page in self.page_condition:
            self.button.x = self.x
        else:
            self.button.x = 15


class Page_Button(Normal_Button):  # making a button class
    def __init__(self, x, y, size, color, text, goto_page, page_condition):
        super().__init__(x, y, size, color, text, page_condition)
        self.goto_page = goto_page
        self.button.on_click = lambda: change_page(self.goto_page)


class Function_Button(Normal_Button):
    def __init__(self, x, y, size, color, text, page_condition, inp, func):
        super().__init__(x, y, size, color, text, page_condition)
        self.function = func
        self.input = inp
        self.button.on_click = lambda: self.function(self.input)


Home_Button = Page_Button(-0.6, 0.4, 0.15, color.blue, 'Home', 'Home',
                          ['Calculator', 'Math Problem Solver', 'Simultaneous Equations',
                           'Quadratic Equations', 'Sorting Algorithm', 'Clicking Game', 'Sort Result'])
Math_Button = Page_Button(-0.3, 0, 0.2, color.orange, 'Math Problem\nSolver',
                          'Math Problem Solver', ['Home', 'Calculator', 'Simultaneous Equations',
                                                  'Quadratic Equations'])
Calculator_Button = Page_Button(-0.3, 0, 0.2, color.orange, 'Calculator', 'Calculator',
                                ['Math Problem Solver'])
Simultaneous_Button = Page_Button(0, 0, 0.2, color.orange, 'Simultaneous\nEquations',
                                  'Simultaneous Equations', ['Math Problem Solver'])
Quadratic_Button = Page_Button(0.3, 0, 0.2, color.orange, 'Quadratic\nEquations',
                               'Quadratic Equations', ['Math Problem Solver'])
Sort_Button = Page_Button(0, 0, 0.2, color.gray, 'Sorting\nAlgorithm', 'Sorting Algorithm',
                          ['Home'])
Game_Button = Page_Button(0.3, 0, 0.2, color.red, 'Clicking Game', 'Clicking Game',
                          ['Home'])

Sort_input_number = InputField(world_position=(15, 15, 15), enabled=True, max_lines=5, character_limit=100000,
                               limit_content_to='1234567890- ,')

Bubble_Sort_Button = Function_Button(-0.25, 0.05, 0.15, color.gray, 'Bubble\nSort',
                                     'Sorting Algorithm', Sort_input_number.text, bubble_sort)
Quick_Sort_Button = Function_Button(0, 0.05, 0.15, color.gray, 'Quick\nSort',
                                    'Sorting Algorithm', Sort_input_number.text, quick_sort)
Counting_Sort_Button = Function_Button(0.25, 0.05, 0.15, color.gray, 'Counting\nSort',
                                       'Sorting Algorithm', Sort_input_number.text, counting_sort)

Calculator_x_input_number = InputField(world_position=(15, 15, 15,), enabled=True, origin_y=-0.1,
                                       limit_content_to='1234567890-', scale=0.1)
Calculator_y_input_number = InputField(world_position=(15, 15, 15,), enabled=True, origin_y=-0.1,
                                       limit_content_to='1234567890-', scale=0.1)

Calculator_Addition_Button = Function_Button(-0.15, 0.2, 0.075, color.peach, '+', 'Calculator',
                                             '+', calculator_symbol_selection)
Calculator_Addition_Button.button.text_color = color.black
Calculator_Subtraction_Button = Function_Button(0, 0.2, 0.075, color.peach, '-',
                                                'Calculator', '-', calculator_symbol_selection)
Calculator_Subtraction_Button.button.text_color = color.black
Calculator_Multiplication_Button = Function_Button(0.15, 0.2, 0.075, color.peach, '×',
                                                   'Calculator', '×', calculator_symbol_selection)
Calculator_Multiplication_Button.button.text_color = color.black
Calculator_Division_Button = Function_Button(-0.075, 0.1, 0.075, color.peach, '÷', 'Calculator',
                                             '÷', calculator_symbol_selection)
Calculator_Division_Button.button.text_color = color.black
Calculator_Power_Button = Function_Button(0.075, 0.1, 0.075, color.peach, 'x^y',
                                          'Calculator', 'x^y', calculator_symbol_selection)
Calculator_Power_Button.button.text_color = color.black
Calculator_Calculate_Button = Function_Button(0, -0.1, 0.15, color.orange, 'Calculate!\n\n(rounded\nto 2dp)',
                                              'Calculator', (Calculator_x_input_number.text,
                                                             Calculator_y_input_number.text), calculator)

Simultaneous_a_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
                                         limit_content_to='1234567890-', scale=0.075)
Simultaneous_b_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
                                         limit_content_to='1234567890-', scale=0.075)
Simultaneous_c_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
                                         limit_content_to='1234567890-', scale=0.075)
Simultaneous_d_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
                                         limit_content_to='1234567890-', scale=0.075)
Simultaneous_e_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
                                         limit_content_to='1234567890-', scale=0.075)
Simultaneous_f_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
                                         limit_content_to='1234567890-', scale=0.075)

Simultaneous_Solve_Button = Function_Button(0, -0.05, 0.20, color.orange, 'Solve for\nx and y',
                                            'Simultaneous Equations',
                                            (Simultaneous_a_input_number.text, Simultaneous_b_input_number.text,
                                             Simultaneous_c_input_number.text, Simultaneous_d_input_number.text,
                                             Simultaneous_e_input_number.text, Simultaneous_f_input_number.text),
                                            simultaneous_equation)

Quadratic_a_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=0,
                                      limit_content_to='1234567890-', scale=0.075)
Quadratic_b_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=0,
                                      limit_content_to='1234567890-', scale=0.075)
Quadratic_c_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=0,
                                      limit_content_to='1234567890-', scale=0.075)

Quadratic_Solve_Button = Function_Button(0, -0.05, 0.2, color.orange, 'Solve for x',
                                         'Quadratic Equations', ('a', 'b', 'c'), quadratic_equation)


def update():  # repeats every frame
    global page_text
    global page
    global symbol
    page_text.text = page
    Home_Button.actions()
    Calculator_Button.actions()
    Simultaneous_Button.actions()
    Quadratic_Button.actions()
    Sort_Button.actions()
    Game_Button.actions()
    Bubble_Sort_Button.actions()
    Quick_Sort_Button.actions()
    Counting_Sort_Button.actions()
    Calculator_Addition_Button.actions()
    Calculator_Subtraction_Button.actions()
    Calculator_Multiplication_Button.actions()
    Calculator_Division_Button.actions()
    Calculator_Power_Button.actions()
    Calculator_Calculate_Button.actions()
    Simultaneous_Solve_Button.actions()
    Quadratic_Solve_Button.actions()

    if page == 'Home':
        home_text.y = 0.25
    else:
        home_text.y = 15

    if page in ['Calculator', 'Simultaneous Equations', 'Quadratic Equations']:
        Math_Button.button.x = -0.4
        Math_Button.button.y = 0.4
        Math_Button.button.scale = 0.15
    elif page == 'Home':
        Math_Button.button.x = Math_Button.x
        Math_Button.button.y = Math_Button.y
        Math_Button.button.scale = Math_Button.size
    else:
        Math_Button.actions()

    if page == 'Sort Result':
        Sort_Button.button.x = -0.4
        Sort_Button.button.y = 0.4
        Sort_Button.button.scale = 0.15
        sort_text.y = 0
    elif page == 'Home':
        Sort_Button.button.x = Sort_Button.x
        Sort_Button.button.y = Sort_Button.y
        Sort_Button.button.scale = Sort_Button.size
        sort_text.y = 15
    else:
        Sort_Button.actions()
        sort_text.y = 15
    
    if page == 'Sorting Algorithm':
        sort_explanation_text.y = 0.25
        Sort_input_number.world_position = (0, -5, 0)
        Bubble_Sort_Button.input = Sort_input_number.text
        Quick_Sort_Button.input = Sort_input_number.text
        Counting_Sort_Button.input = Sort_input_number.text
    else:
        sort_explanation_text.y = 15
        Sort_input_number.world_position = (15, 15, 15)

    if page not in ['Sorting Algorithm', 'Sort Result']:
        Sort_input_number.text = 'Type here'

    if page == 'Calculator':
        symbol_text.text = symbol
        symbol_text.y = 0.3
        Calculator_x_input_number.world_position = (-6, -3, 0)
        Calculator_y_input_number.world_position = (6, -3, 0)
        Calculator_Calculate_Button.input = (Calculator_x_input_number.text, Calculator_y_input_number.text)
    else:
        Calculator_x_input_number.text = 'x'
        Calculator_y_input_number.text = 'y'
        Calculator_x_input_number.world_position = (15, 15, 15)
        Calculator_y_input_number.world_position = (15, 15, 15)
        symbol_text.y = 15
        calculator_text.y = 15
        symbol_text.text = 'Select symbol'

    if page == 'Simultaneous Equations':
        simultaneous_equation_equation_text.y = 0.2
        Simultaneous_a_input_number.world_position = (-3.5, 5.5, 0)
        Simultaneous_b_input_number.world_position = (0, 5.5, 0)
        Simultaneous_c_input_number.world_position = (3.5, 5.5, 0)
        Simultaneous_d_input_number.world_position = (-3.5, 2.5, 0)
        Simultaneous_e_input_number.world_position = (0, 2.5, 0)
        Simultaneous_f_input_number.world_position = (3.5, 2.5, 0)
        Simultaneous_Solve_Button.input = (Simultaneous_a_input_number.text, Simultaneous_b_input_number.text,
                                           Simultaneous_c_input_number.text, Simultaneous_d_input_number.text,
                                           Simultaneous_e_input_number.text, Simultaneous_f_input_number.text)
    else:
        simultaneous_equation_equation_text.y = 15
        simultaneous_equation_text.y = 15
        Simultaneous_a_input_number.world_position = (15, 15, 15)
        Simultaneous_b_input_number.world_position = (15, 15, 15)
        Simultaneous_c_input_number.world_position = (15, 15, 15)
        Simultaneous_d_input_number.world_position = (15, 15, 15)
        Simultaneous_e_input_number.world_position = (15, 15, 15)
        Simultaneous_f_input_number.world_position = (15, 15, 15)

    if page == 'Quadratic Equations':
        quadratic_equation_equation_text.y = 0.2
        Quadratic_a_input_number.world_position = (-3.7, 4, 0)
        Quadratic_b_input_number.world_position = (0.1, 4, 0)
        Quadratic_c_input_number.world_position = (3.5, 4, 0)
        Quadratic_Solve_Button.input = (Quadratic_a_input_number.text, Quadratic_b_input_number.text,
                                        Quadratic_c_input_number.text)
    else:
        quadratic_equation_equation_text.y = 15
        quadratic_equation_text.y = 15
        Quadratic_a_input_number.world_position = (15, 15, 15)
        Quadratic_b_input_number.world_position = (15, 15, 15)
        Quadratic_c_input_number.world_position = (15, 15, 15)


app.run()  # needed to run the program
