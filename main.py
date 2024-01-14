# git add main.py
# git commit -m "eleventh commit"
# git push origin master

# git pull origin master (기존 commit 해놓은 코드 가져오기)

# exe file location
# D:\Hojun\PycharmProject\Personal_Project\Personal_Project_Program\output\main

from ursina import *
import random
import time
import webbrowser

app = Ursina()

window.borderless = False  # lets the user move the window
window.color = color.dark_gray  # makes the background color dark gray
window.size = (1080, 720)  # size of window

home_text = Text(text="Due to lack of my programming skills, this program doesn't accept decimals or fractions: "
                      "only integers. ", origin=(0, 0), scale=1.1)

# home_math_text = Text(text="This section consists of:\n\nA simple calculator which can\ncalculate simple operations\n\n"
#                            "A function which can solve\nsimultaneous equations easily\n\nA function which can solve\n"
#                            "quadratic equations easily", origin=(0, 0), x=-0.475)  # y=-0.3
# home_sort_text = Text(text="This section consists of:\n\n3 different ways to sort a\nnumber set in ascending\norder, "
#                            "which are:\n\nBubble sort\n\nQuick sort\n\nCounting sort", origin=(0, 0))  # y=-0.3125
# home_game_text = Text(text="In this section, you can play a\n\nsimple game in which you have\n\nto click a button "
#                            "multiple times\n\nin 5 seconds", origin=(0, 0), x=0.475)  # y=-0.225

page = 'Home'
page_text = Text(text=page, origin=(0, 0), y=0.4, scale=2)  # current page

sort_text = Text(text='', origin=(0, 0), wordwrap=10)  # answer of sort
sort_explanation_text = Text(text='1. Type in any sets of integers, and click any sorting method.     \n2. The program '
                                  'will sort the numbers in ascending order.          \n3. Type a comma in between '
                                  "numbers, and don't put in letters.\nEx) 4, 1, -2, 4, 0", origin=(0, 0))
sort_number_set_text = Text(text='Type in your number set here', origin=(0, 0), scale=1.5)  # y=-0.075

symbol = 'Select symbol'
symbol_text = Text(text=symbol, origin=(0, 0), scale=2)  # text showing the current symbol (calculator)
calculator_text = Text(origin=(0, 0), scale=1.2)  # answer of calculator

simultaneous_equation_text = Text(origin=(0, 0))  # answer of simultaneous equation
simultaneous_equation_equation_text = Text(text='       x +        y =        \n\n\n       x +        y =        ',
                                           origin=(0, 0), scale=2)

quadratic_equation_text = Text(origin=(0, 0))  # answer of quadratic equation
quadratic_equation_equation_text = Text(text='       x² +        x =        ', origin=(0, 0), scale=2)


math_calculator_text = Text(text='A simple calculator which can\ncalculate simple operations', origin=(0, 0), x=-0.475)
math_simultaneous_text = Text(text='A function which can solve\nsimultaneous equations easily', origin=(0, 0))
math_quadratic_text = Text(text='A function which can solve\nquadratic equations easily', origin=(0, 0), x=0.475)


click_number = 0  # how many clicks
click_number_text = Text(text='0 clicks', origin=(0, 0), scale=1.2)  # text of how many clicks
click_time_text = Text(text='5 seconds', origin=(0, 0), scale=1.2)  # time left
click_result_text = Text(origin=(0, 0), scale=1.2)  # final text + clicks + comment
clicking_game_explanation_text = Text(text='How many times can you click the button in 5 seconds?', origin=(0, 0),
                                      scale=1.5)
clicking_game_reaction_text = Text(origin=(0, 0), scale=5, color=color.gold)

finishing_time = 5

levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5', 'Level 6', 'Level 7', 'Level 8', 'Level 9', 'Level 10']


def change_page(goto_page):  # changing page function
    global page
    page = goto_page


def make_number_2dp(inp):  # rounding every number to its 2nd decimal place or less
    if inp == int(inp):
        inp = str(round(inp))
    elif inp * 10 == int(inp * 10):
        inp = str(format(inp, '.1f'))
    else:
        inp = str(format(inp, '.2f'))
    return inp


def return_texts(inp):
    for i in range(len(inp)):
        inp[i] = inp[i].text
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
    length = len(given_list) - 1
    for i in range(length):
        for j in range(length):
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

    minimum = min(given_list)
    maximum = max(given_list)
    if maximum - minimum >= 5000000:
        sort_text.text = ('Error - given range of numbers might be too big to be\nsorted using counting sort method.'
                          '\nTry another sorting method.')
        page = 'Sort Result'
        return
    index_list = list(range(minimum, maximum + 1))
    result_list = []
    n_list = [0] * len(index_list)
    for n in given_list:
        ind = index_list.index(n)
        n_list[ind] += 1
    for i in range(len(n_list)):
        for j in range(n_list[i]):
            result_list.append(i + minimum)

    sort_text.text = 'Result: ' + str(result_list)
    page = 'Sort Result'


def go_to_youtube(link):
    webbrowser.open(link)


def calculator_symbol_selection(given_symbol):
    global symbol
    symbol = given_symbol


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
        answer = x + y
    elif symbol == '-':
        answer = x - y
    elif symbol == '×':
        answer = x * y
    elif symbol == '÷':
        if y != 0:
            answer = x / y
        else:
            calculator_text.text = 'Cannot divide by 0'
            calculator_text.y = -0.3
            return
    elif symbol == 'x^y':
        answer = x ** y

    calculator_text.text = str(make_number_2dp(answer))
    calculator_text.y = -0.3


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

    if b * d - a * e != 0:
        y = (c * d - a * f) / (b * d - a * e)
    elif c * d - a * f == 0:  # and b*d-a*e == 0
        simultaneous_equation_text.text = 'There are infinitely many solutions'
        simultaneous_equation_text.y = -0.3
        return
    else:  # if c*d-a*f != 0 and b*d-a*e == 0
        simultaneous_equation_text.text = 'There are no solutions'
        simultaneous_equation_text.y = -0.3
        return

    #  ax = c-by, x=(c-by)/a

    if a != 0:
        x = (c - b * y) / a
    else:
        x = (f - e * y) / d

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
            x = make_number_2dp(c / b)
            quadratic_equation_text.text = f'This is a linear equation, not a quadratic equation. x = {x}'
            quadratic_equation_text.y = -0.3
            return  # not a quadratic equation
        else:
            quadratic_equation_text.text = 'Cannot solve for x.'
            quadratic_equation_text.y = -0.3
            return
    if b * b < 4 * a * c:
        quadratic_equation_text.text = 'No real solution'
        quadratic_equation_text.y = -0.3
        return  # no real solution
    if b * b == 4 * a * c:
        x = make_number_2dp(-b / (2 * a))
        quadratic_equation_text.text = f'x = {x} (multiple root)'
        quadratic_equation_text.y = -0.3
        return  # one solution
    x1 = make_number_2dp((-b + (b * b - 4 * a * c) ** 0.5) / (2 * a))
    x2 = make_number_2dp((-b - (b * b - 4 * a * c) ** 0.5) / (2 * a))
    if x1 < x2:
        temp = x1
        x1 = x2
        x2 = temp

    quadratic_equation_text.text = f'x = {x1}, x = {x2}'
    quadratic_equation_text.y = -0.3
    return  # two solutions


def click_add_1():
    global click_number
    click_number = click_number + 1
    return click_number


def clicking_game(lvl):
    global click_number
    global finishing_time
    global page
    if finishing_time != 5:  # when clicking started
        if time.time() <= finishing_time:
            click_time_text.text = str(make_number_2dp(finishing_time - time.time())) + ' seconds'
            click_number_text.text = f'{click_number}/{lvl} clicks'
        else:
            page = 'Result'
            if click_number >= lvl:
                click_result_text.text = (f'You clicked the button {click_number} times in 5 seconds! '
                                          f'(aim: {lvl} times)')
                clicking_game_reaction_text.text = 'Congratulations!'
                finishing_time = 5
                Clicking_Game_Click_Button_list[int((lvl - 15) / 5 - 1)].button.color = color.green
                Clicking_Game_Click_Button_list[int((lvl - 15) / 5 - 1)].button.text_color = color.black

            else:
                click_result_text.text = (
                    f'You clicked the button {click_number} times, which is {lvl - click_number} times '
                    f'less than your aim ({lvl} times) :(')
                clicking_game_reaction_text.text = 'Try again :('
                finishing_time = 5


class NormalButton:
    def __init__(self, x, y, size, clr, txt, page_condition):  # defining everything inside this button class
        self.x = x
        self.y = y
        self.size = size
        self.color = clr
        self.text = txt
        self.page_condition = page_condition
        self.button = Button(text=self.text, color=self.color, scale=self.size, origin=(0, 0), x=15, y=self.y)

    def actions(self):
        global page
        if page in self.page_condition:
            self.button.x = self.x
        else:
            self.button.x = 15


class PageButton(NormalButton):  # making a button class
    def __init__(self, x, y, size, clr, txt, goto_page, page_condition):
        super().__init__(x, y, size, clr, txt, page_condition)
        self.goto_page = goto_page
        self.button.on_click = lambda: change_page(self.goto_page)


class FunctionButton(NormalButton):
    def __init__(self, x, y, size, clr, txt, page_condition, inp, func):
        super().__init__(x, y, size, clr, txt, page_condition)
        self.function = func
        self.input = inp
        self.button.on_click = lambda: self.function(self.input)


Home_Button = PageButton(-0.6, 0.4, 0.15, color.blue, 'Home', 'Home',
                         ['Calculator', 'Math Problem Solver', 'Simultaneous Equations', 'Quadratic Equations',
                          'Sorting Algorithm', 'Clicking Game', 'Sort Result', 'Result'] + levels)
Math_Button = PageButton(-0.4, 0, 0.2, color.orange, 'Math Problem\nSolver', 'Math Problem Solver',
                         ['Home', 'Calculator', 'Simultaneous Equations', 'Quadratic Equations'])
Calculator_Button = PageButton(-0.4, 0, 0.2, color.orange, 'Calculator', 'Calculator',
                               ['Math Problem Solver'])
Simultaneous_Button = PageButton(0, 0, 0.2, color.orange, 'Simultaneous\nEquations',
                                 'Simultaneous Equations', ['Math Problem Solver'])
Quadratic_Button = PageButton(0.4, 0, 0.2, color.orange, 'Quadratic\nEquations',
                              'Quadratic Equations', ['Math Problem Solver'])
Sort_Button = PageButton(0, 0, 0.2, color.gray, 'Sorting\nAlgorithm', 'Sorting Algorithm',
                         ['Home'])
Clicking_Game_Button = PageButton(0.4, 0, 0.2, color.red, 'Clicking Game', 'Clicking Game',
                                  ['Result'] + levels)

Sort_input_number = InputField(world_position=(15, 15, 15), enabled=True, max_lines=5, character_limit=100000,
                               limit_content_to='1234567890- ,')

Bubble_Sort_Button = FunctionButton(-0.25, 0.05, 0.15, color.gray, 'Bubble\nSort',
                                    'Sorting Algorithm', Sort_input_number.text, bubble_sort)
Quick_Sort_Button = FunctionButton(0, 0.05, 0.15, color.gray, 'Quick\nSort',
                                   'Sorting Algorithm', Sort_input_number.text, quick_sort)
Counting_Sort_Button = FunctionButton(0.25, 0.05, 0.15, color.gray, 'Counting\nSort',
                                      'Sorting Algorithm', Sort_input_number.text, counting_sort)

Bubble_Sort_Explanation_Button = FunctionButton(0.5, 0.2, 0.13, color.gray, 'What is a\nbubble\nsort?',
                                                'Sorting Algorithm',
                                                'https://youtu.be/H-3CSiV76PI', go_to_youtube)
Quick_Sort_Explanation_Button = FunctionButton(0.5, 0, 0.12, color.gray, 'What is a\nquick\nsort?',
                                               'Sorting Algorithm',
                                               'https://youtu.be/HyEmmSaVw9A', go_to_youtube)
Counting_Sort_Explanation_Button = FunctionButton(0.5, -0.2, 0.12, color.gray, 'What is a\ncounting\nsort?',
                                                  'Sorting Algorithm',
                                                  'https://youtu.be/VE2Cakzuhu0', go_to_youtube)


Calculator_x_input_number = InputField(world_position=(15, 15, 15,), enabled=True, origin_y=-0.1,
                                       limit_content_to='1234567890-', scale=0.1)
Calculator_y_input_number = InputField(world_position=(15, 15, 15,), enabled=True, origin_y=-0.1,
                                       limit_content_to='1234567890-', scale=0.1)


Calculator_Buttons_list = []
symbol_list = ['+', '÷', '-', 'x^y', '×']

for cal in range(5):
    Calculator_Buttons_list.append(FunctionButton(0.075 * cal - 0.15, 0.1 * ((cal + 1) % 2 + 1), 0.075,
                                                  color.peach, symbol_list[cal], 'Calculator',
                                                  symbol_list[cal], calculator_symbol_selection))
    Calculator_Buttons_list[cal].button.text_color = color.black
    Calculator_Buttons_list[cal].button.text_size = 1.25


Calculator_Calculate_Button = FunctionButton(0, -0.1, 0.15, color.orange, 'Calculate!\n\n(rounded\nto 2dp)',
                                             'Calculator', (Calculator_x_input_number.text,
                                                            Calculator_y_input_number.text), calculator)


# for sim in range(6):
#     Simultaneous_input_list.append(InputField(world_position=(15, 15, 15), enabled=True, origin_y=-0.1,
#                                               limit_content_to='1234567890-', scale=0.075))

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

Simultaneous_input_list = [Simultaneous_a_input_number, Simultaneous_b_input_number, Simultaneous_c_input_number,
                           Simultaneous_d_input_number, Simultaneous_e_input_number, Simultaneous_f_input_number]

Simultaneous_Solve_Button = FunctionButton(0, -0.05, 0.20, color.orange, 'Solve for\nx and y',
                                           'Simultaneous Equations', return_texts(Simultaneous_input_list),
                                           simultaneous_equation)

Quadratic_a_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=0,
                                      limit_content_to='1234567890-', scale=0.075)
Quadratic_b_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=0,
                                      limit_content_to='1234567890-', scale=0.075)
Quadratic_c_input_number = InputField(world_position=(15, 15, 15), enabled=True, origin_y=0,
                                      limit_content_to='1234567890-', scale=0.075)

Quadratic_Solve_Button = FunctionButton(0, -0.05, 0.2, color.orange, 'Solve for x',
                                        'Quadratic Equations', ('a', 'b', 'c'), quadratic_equation)

Clicking_Game_Click_Button_list = []

for cli in range(10):
    Clicking_Game_Click_Button_list.append(PageButton((cli % 5) * 0.25 - 0.5, round((cli + 1) / 11) * -0.3, 0.2,
                                                      color.red, f'{levels[cli]}\n\n{cli * 5 + 20} clicks',
                                                      levels[cli], 'Clicking Game'))

Clicking_Game_Click_Button = NormalButton(0, 0, 0.3, color.yellow, 'Click this Button!', levels)
Clicking_Game_Click_Button.button.text_color = color.black


def update():  # repeats every frame
    global page_text
    global page
    global symbol
    global click_number
    global finishing_time
    page_text.text = page
    Home_Button.actions()
    Calculator_Button.actions()
    Simultaneous_Button.actions()
    Quadratic_Button.actions()
    Sort_Button.actions()
    Bubble_Sort_Button.actions()
    Quick_Sort_Button.actions()
    Counting_Sort_Button.actions()
    Calculator_Calculate_Button.actions()
    Bubble_Sort_Explanation_Button.actions()
    Quick_Sort_Explanation_Button.actions()
    Counting_Sort_Explanation_Button.actions()
    for calculator_buttons in Calculator_Buttons_list:
        calculator_buttons.actions()
    Simultaneous_Solve_Button.actions()
    Quadratic_Solve_Button.actions()
    Clicking_Game_Click_Button.actions()
    for clicking_buttons in Clicking_Game_Click_Button_list:
        clicking_buttons.actions()

    if page == 'Home':
        home_text.y = 0.225
        # home_math_text.y = -0.3
        # home_sort_text.y = -0.3125
        # home_game_text.y = -0.2625
        Math_Button.button.x = Math_Button.x
        Math_Button.button.y = Math_Button.y
        Math_Button.button.scale = Math_Button.size
    else:
        home_text.y = 15
        # home_math_text.y = 15
        # home_sort_text.y = 15
        # home_game_text.y = 15

    if page == 'Math Problem Solver':
        math_calculator_text.y = -0.225
        math_simultaneous_text.y = -0.225
        math_quadratic_text.y = -0.225
    else:
        math_calculator_text.y = 15
        math_simultaneous_text.y = 15
        math_quadratic_text.y = 15

    if page in ['Calculator', 'Simultaneous Equations', 'Quadratic Equations']:
        Math_Button.button.x = -0.4
        Math_Button.button.y = 0.4
        Math_Button.button.scale = 0.15
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
        sort_number_set_text.y = -0.075
        Sort_input_number.world_position = (0, -5, 0)
        Bubble_Sort_Button.input = Sort_input_number.text
        Quick_Sort_Button.input = Sort_input_number.text
        Counting_Sort_Button.input = Sort_input_number.text
    else:
        sort_explanation_text.y = 15
        sort_number_set_text.y = 15
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

    if page in ['Result'] + levels:
        Clicking_Game_Button.button.x = -0.4
        Clicking_Game_Button.button.y = 0.4
        Clicking_Game_Button.button.scale = 0.15
    elif page == 'Home':
        Clicking_Game_Button.button.x = Clicking_Game_Button.x
        Clicking_Game_Button.button.y = Clicking_Game_Button.y
        Clicking_Game_Button.button.scale = Clicking_Game_Button.size
    else:
        Clicking_Game_Button.actions()

    if click_number > 0 and finishing_time == 0:
        finishing_time = time.time() + 5  # giving the player 5 seconds right after the click

    if page == 'Clicking Game':
        clicking_game_explanation_text.y = 0.25
    else:
        clicking_game_explanation_text.y = 15

    if page in levels:
        Clicking_Game_Click_Button.button.on_click = click_add_1
        if click_number > 0 and finishing_time == 5:
            finishing_time = time.time() + 5  # giving the player 5 seconds right after the click

        click_time_text.y = -0.25
        click_number_text.y = 0.25
        for level in levels:
            if page == level:
                clicking_game(20 + levels.index(level) * 5)

    else:
        if page == 'Result':
            clicking_game_reaction_text.y = 0
            click_result_text.y = -0.2
        else:
            clicking_game_reaction_text.y = 15
            click_result_text.y = 15
        click_number = 0
        click_number_text.text = '0 clicks'
        click_number_text.y = 15
        click_time_text.text = '5 seconds'
        click_time_text.y = 15
        finishing_time = 5


app.run()  # needed to run the program
