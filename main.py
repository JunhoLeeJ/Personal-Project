# git add main.py
# git commit -m "fourth commit"
# git push origin master

# git pull origin master (기존 commit 해놓은 코드 가져오기)


from ursina import *  # meaning that you import Ursina and you don't have to type Ursina.name of the function every time
# you want to use a function in Ursina. e.g. window.size = (1580, 720)
import random  # meaning that you import an internal library named random and you have to type random.name of the
# function every time to use the function. e.g. random.randint(1, 15)

app = Ursina()

window.borderless = False  # lets the user move the window
window.color = color.black  # makes the background color black
window.size = (1080, 720)

page = 'Home'  # page variable is set as 'Home'
page_text = Text(text=page, origin=(0, 0), y=0.4, scale=2)
sort_text = Text(text='', origin=(0, 0), y=15, scale=2)
sort_explanation_text = Text(text='1. Type in any sets of integers, and click any sorting method.     \n2. The program will '
                                  'sort the numbers in ascending order.          \n3. Type a comma in between numbers, and '
                                  "don't put in letters.\nEx) 4, 1, -2, 4, 0",
                             origin=(0, 0), y=15, scale=1.15)


def change_page(goto_page):  # changing page function
    global page
    page = goto_page


def bubble_sort(given_list):  # bubble sort function
    global page
    if given_list == 'Type here':
        sort_text.text = "Click on the button 'Type here' and type a number set"
        page = 'Sort Result'
        return
    try:
        given_list = [int(x) for x in given_list.split(',')]
    except ValueError:
        sort_text.text = 'Error'
        page = 'Sort Result'
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


def quick_sort_function(given_list):
    pivot = random.choice(given_list)
    n = 0
    small_list = []
    pivot_list = [pivot]
    big_list = []
    for i in given_list:
        if i < pivot:
            small_list.append(i)
        elif i == pivot:
            n += 1
        else:
            big_list.append(i)

    pivot_list.append(n)
    if len(small_list) == 1:
        small_list = small_list[0]
    if len(big_list) == 1:
        big_list = big_list[0]
    return small_list, pivot_list, big_list


def quick_sort(given_list):
    global page
    if given_list == 'Type here':
        sort_text.text = "Click on the button 'Type here' and type a number set"
        page = 'Sort Result'
        return
    try:
        given_list = [int(x) for x in given_list.split(',')]
    except ValueError:
        sort_text.text = 'Error'
        page = 'Sort Result'
        return
    result_list = [given_list]
    while len(result_list) < len(given_list):
        for i in result_list:
            if isinstance(i, list):
                (small, pivot, big) = quick_sort_function(i)
                ind = result_list.index(i)
                result_list.pop(ind)
                if big:
                    result_list.insert(ind, big)
                for j in range(pivot[1]):
                    result_list.insert(ind, pivot[0])
                if small:
                    result_list.insert(ind, small)

    sort_text.text = 'Result: ' + str(result_list)
    page = 'Sort Result'


def counting_sort(given_list):  # [4, 1, -2, 4, 0]
    global page
    if given_list == 'Type here':
        sort_text.text = "Click on the button 'Type here' and type a number set"
        page = 'Sort Result'
        return
    try:
        given_list = [int(x) for x in given_list.split(',')]
    except ValueError:
        sort_text.text = 'Error'
        page = 'Sort Result'
        return

    m = min(given_list)  # -2
    M = max(given_list)  # 4
    try:
        index_list = list(range(m, M+1))  # [-2, -1, 0, 1, 2, 3, 4]
    except:  # if the number is too big an error occurs.
        sort_text.text = 'Error - given set is too big to be\nsorted using counting sort method.\nTry another sorting method.'
        page = 'Sort Result'
        return
    result_list = []
    n_list = [0]*len(index_list)  # [0, 0, 0, 0, 0, 0, 0]  >>  [1, 0, 1, 1, 0, 0, 2]
    for n in given_list:  # 4, 1, -2, 4, 0
        ind = index_list.index(n)  # 6, 3, 0, 6, 2
        n_list[ind] += 1
    for i in range(len(n_list)):  # 0, 1, 2, 3, 4, 5, 6
        for j in range(n_list[i]):  # 1번, 0번, 1번, 1번, 0번, 0번, 2번
            result_list.append(i+m)  # -2, 0, 1, 4, 4

    sort_text.text = 'Result: ' + str(result_list)
    page = 'Sort Result'


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
    def __init__(self, x, y, size, color, text, goto_page, page_condition):  # defining everything inside this button class
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
Math_Button = Page_Button(-0.3, 0, 0.2, color.orange, 'Math Problem\nSolver', 'Math Problem Solver',
                          ['Home', 'Calculator', 'Simultaneous Equations', 'Quadratic Equations'])
Calculator_Button = Page_Button(-0.3, 0, 0.2, color.orange, 'Calculator', 'Calculator',
                                ['Math Problem Solver'])
Simultaneous_Button = Page_Button(0, 0, 0.2, color.orange, 'Simultaneous\nEquations',
                                  'Simultaneous Equations', ['Math Problem Solver'])
Quadratic_Button = Page_Button(0.3, 0, 0.2, color.orange, 'Quadratic\nEquations',
                               'Quadratic Equations', ['Math Problem Solver'])
Sort_Button = Page_Button(0, 0, 0.2, color.dark_gray, 'Sorting\nAlgorithm', 'Sorting Algorithm',
                          ['Home'])
Game_Button = Page_Button(0.3, 0, 0.2, color.red, 'Clicking Game', 'Clicking Game', ['Home'])
Input_number = InputField(world_position=(0, 15, 0), enabled=True)
Bubble_Sort_Button = Function_Button(-0.25, 0, 0.15, color.gray, 'Bubble\nSort', 'Sorting Algorithm',
                                     Input_number.text, bubble_sort)
Quick_Sort_Button = Function_Button(0, 0, 0.15, color.gray, 'Quick\nSort', 'Sorting Algorithm',
                                    Input_number.text, quick_sort)
Counting_Sort_Button = Function_Button(0.25, 0, 0.15, color.gray, 'Counting\nSort', 'Sorting Algorithm',
                                       Input_number.text, counting_sort)


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
    Bubble_Sort_Button.actions()
    Quick_Sort_Button.actions()
    Counting_Sort_Button.actions()
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
        sort_text.y = -0.3
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
        Input_number.world_position = (0, 2.5, 0)
        Bubble_Sort_Button.input = Input_number.text
        Quick_Sort_Button.input = Input_number.text
        Counting_Sort_Button.input = Input_number.text
    else:
        sort_explanation_text.y = 15
        Input_number.world_position = (0, 15, 0)

    if page not in ['Sorting Algorithm', 'Sort Result']:
        Input_number.text = 'Type here'


app.run()  # needed to run the program
