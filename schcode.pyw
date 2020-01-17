import tkinter as tk
from tkinter import *
import sys, os
import wx

class WizardLikeApp(tk.Tk):
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        no_caption = (wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR | wx.MINIMIZE_BOX)
        wx.Frame.__init__(self, None, size=(470, 510), style=no_caption)
        panel = MainPanel(self)
        self.Center()


        self.frames = {}

        for F in (DIDA_OTVET_6_1, DIDA_OTVET_6, DIDA_OTVET_4_2, PYTHON_2_1, PYTHON_2_2, PYTHON_2_3, PASCAL_2_1, PASCAL_2_2, PASCAL_2_3, PASCAL_2_4, DIDA_2_1, DIDA_OTVET_1, DIDA_OTVET_2, DIDA_OTVET_3, DIDA_OTVET_4, DIDA_OTVET_5, DIDA_1_1, DIDA_1_2, DIDA_1_3, DIDA_1_4, DIDA_1_5, PAGE_DIDA_1, PAGE_DIDA_2, PAGE_MAIN_MENU, PAGE_GO_LEAN, PASCAL_1_0, PASCAL_1_1, PASCAL_1_2, PASCAL_1_3, PASCAL_1_4, PASCAL_1_5, PASCAL_1_6, PASCAL_1_7,PASCAL_1_8, PYTHON_1_0, PYTHON_1_1, PYTHON_1_2, PYTHON_1_3, PYTHON_1_4, PYTHON_1_5):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(PAGE_MAIN_MENU)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PAGE_MAIN_MENU (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_MAIN_MENU = "SCHCode - интерактивный учебник для изучения\n" \
                         "языков программирования на уровне школьной\n" \
                         "программы. Здесь ты сможешь научиться основам\n" \
                         "написания кода на языках Pascal и Python, а также\n" \
                         "закрепить полученнные знания прорешав задачи\n" \
                         "в отделе 'Дидактические материалы' (нажав на    \n" \
                         "специальную кнопку внизу экрана после изучения\n" \
                         "определенной темы или напрямиг).\n" \
                         "Автор надеется, что это поможет тебе лучше понять\n" \
                         "подаваемый в школе материал, соответственно\n" \
                         "повысить свою успеваемость, а может и просто\n" \
                         "обучиться основам прораммирования на данных\n" \
                         "языках, самообразовываясь и пробуя себя в роли\n" \
                         "разработчика небольших проектов.                        \n" \
                         "\n" \
                         "                          Удачи в изучении!\n"

        label_TEXT_MM = tk.Label(self, text=text_MAIN_MENU, width=50, justify=LEFT)
        label_TEXT_MM.place(relx=.450, rely=.20)

        button_GO_LEAN = tk.Button(self, text="УЧИТЬ ЯЗЫКИ", pady="10", padx="77",
                           command=lambda: controller.show_frame(PAGE_GO_LEAN))
        button_GO_LEAN.place(x=20, y=95)

        button_DIDA = Button(self, text="ДИДАКТИЧЕСКИЕ МАТЕРИАЛЫ", pady="10", padx="30",
                                 command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_DIDA.place(x=20, y=190)

        button_EXIT = Button(self, text ="ВЫХОД", pady="10", padx="97",command=quit)
        button_EXIT.place(x=20, y=285)


class PAGE_GO_LEAN (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        button_PASCAL_1 = tk.Button(self, text="PASCAL - ПЕРВЫЙ ЭТАП", pady="10", padx="50",
                                           command=lambda: controller.show_frame(PASCAL_1_0))
        button_PASCAL_1.place(x=20, y=80)

        button_PASCAL_2 = tk.Button(self, text="PASCAL - ВТОРОЙ ЭТАП", pady="10", padx="50",
                                           command=lambda: controller.show_frame(PASCAL_2_1))
        button_PASCAL_2.place(x=20, y=160)

        button_PYTHON_1 = tk.Button(self, text="PYTHON - ПЕРВЫЙ ЭТАП", pady="10", padx="48",
                                           command=lambda: controller.show_frame(PYTHON_1_0))
        button_PYTHON_1.place(x=20, y=240)

        button_PYTHON_2 = tk.Button(self, text="PYTHON - ВТОРОЙ ЭТАП", pady="10", padx="48",
                                           command=lambda: controller.show_frame(PYTHON_2_1))
        button_PYTHON_2.place(x=20, y=320)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                           command=lambda: controller.show_frame(PAGE_MAIN_MENU))
        button_NAZAD.place(x=555, y=400)


#

#


class PASCAL_1_0(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_0 = "Pascal - один из языков программирования, который помогает писать «структурированные»\n" \
                          "программы в таком виде, в котором структура программы должна непосредственно\n" \
                          "отражать структуру задачи. Эта особенность языка Pascal, а также его достаточная простота\n" \
                          "из-за интуитивной понятийности его конструкций, позволила языку завоевать прочное место\n" \
                          "среди языков программирования. Современным достижением программирования является\n" \
                          "признание преимущества структурированных программ. Вот почему Pascal широко\n" \
                          "используется инженерами и научными работниками, является официальным языком\n" \
                          "международных олимпиад по информатике. Первую версию Pascal разработал и предложил\n" \
                          "в 1968 году известный швейцарский ученый Никлаус Вирт. Этот язык являлся развитием языка\n" \
                          "Algol 60 и был задуман для обучения студентов основам программирования.\n"


        label_PASCAL_1_0 = tk.Label(self, text=text_PASCAL_1_0, justify=LEFT)
        label_PASCAL_1_0.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                 command=lambda: controller.show_frame(PASCAL_1_1))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                           command=lambda: controller.show_frame(PAGE_GO_LEAN))
        button_NAZAD.place(x=555, y=400)


class PASCAL_1_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_1 = "1. ТИПЫ ДАННЫХ\n" \
                          "\n" \
                          "Любая программа, написанная на любом языке программирования, по большому счету \n" \
                          "предназначена для обработки данных. В качестве данных могут выступать числа, тексты,\n" \
                          "графика, звук и др. Одни данные являются исходными, другие – результатом, который\n" \
                          "получается путем обработки исходных данных программой. Данные хранятся в памяти\n" \
                          "компьютера. Программа обращается к ним с помощью имен переменных, связанных с\n" \
                          "участками памяти, где хранятся данные. Переменные описываются до основного кода\n" \
                          "программы. Здесь указываются имена переменных и тип хранимых в них данных. В языке\n" \
                          "программирования Паскаль достаточно много типов данных. Кроме того, сам пользователь\n" \
                          "может определять свои типы. Тип переменной определяет, какие данные можно хранить в\n" \
                          "связанной с ней ячейке памяти.                                                                                          \n" \
                          "\n" \
                          "\n" \
                          "НАЗВАНИЕ                    -          ОБОЗНАЧЕНИЯ          -          ДОПУСТИМЫЕ ЗНАЧЕНИЯ\n" \
                          "ЦЕЛОЧИСЛЕННЫЙ     -          integer                           -          - 32768 .. 32767\n" \
                          "ВЕЩЕСТВЕННЫЙ         -          real                                 -          +-(2.9 * 10 (-39 степень) .. 1.7 * 10(+38 степень))\n" \
                          "СИМВОЛЬНЫЙ            -          char                                -          произвольный символ алфавита \n" \
                          "СТРОКОВОЙ                -           string                             -          некоторое кол - во символов до 255\n" \
                          "ЛОГИЧЕСКИЙ              -           boolean                        -          true или false\n"

        label_PASCAL_1_1 = tk.Label(self, text=text_PASCAL_1_1, justify=LEFT)
        label_PASCAL_1_1.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                 command=lambda: controller.show_frame(PASCAL_1_2))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                           command=lambda: controller.show_frame(PASCAL_1_0))
        button_NAZAD.place(x=555, y=400)


class PASCAL_1_2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_2 = "2. СТРУКТУРА ПРОГРАММЫ\n" \
                          "\n" \
                          "Текст программы, написанной на языке программирования Pascal имеет жесткую структуру.\n" \
                          "В простейшем случае программа имеет следующий вид:\n" \
                          "\n" \
                          "Program <имя программы>;  (заголовок программы, имя программы выбирается составителем\n" \
                          "самостоятельно)\n" \
                          "Const <имя константы>=<значение константы> ;   (раздел описания констант)\n" \
                          "Var\n" \
                          "<имя переменной1, имя переменной2, … >: <Тип1 переменных>;\n" \
                          "<имя переменной1, имя переменной2, … >: <Тип2 переменных>;\n" \
                          "(раздел описания переменных, необязательный в случае, если программа не использует\n" \
                          "никаких переменных)\n" \
                          "Begin  (начало программы)\n" \
                          "<тело программы>  (последовательность команд (операторов), разделенных знаком “;”)\n" \
                          "End.  (конец программы)\n" \
                          "\n" \
                          "В разделе описания переменных перечисляются все переменные, используемые в программе,\n" \
                          "и их тип (целочисленные, дробные, символьные…). Имена переменных не должны совпадать\n" \
                          "с  названиями операторов, типов переменных, именем программы. Служебные слова BEGIN\n" \
                          "и END называют операторными скобками, между ними записывается последовательность\n" \
                          "команд, которые программа должна выполнить. Эти команды называют операторами. Все\n" \
                          "операторы отделяются друг от друга точкой с запятой.\n" \


        label_PASCAL_1_2 = tk.Label(self, text=text_PASCAL_1_2, justify=LEFT)
        label_PASCAL_1_2.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_1_3))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_1))
        button_NAZAD.place(x=555, y=400)


class PASCAL_1_3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_3 = "3. ОПЕРАТОР ПРИСВАИВАНИЯ И СПЕЦИАЛЬНЫЕ СИМВОЛЫ\n" \
                          "\n" \
                          "Оператор присваивания имеет следующую структуру:\n" \
                          "\n" \
                          "<Переменная> := <Выражение> ;\n" \
                          "\n" \
                          "Теперь рассмотрим некоторые специальные символы:\n" \
                          "\n" \
                          "+ - сложение\n" \
                          "- - вычитание\n" \
                          "* - умножение\n" \
                          "/ - деление\n" \
                          "= - равно\n" \
                          "> - больше; < - меньше; >= - больше или равно; <= - меньше или равно; <> - не равно\n" \
                          "^ - возведение в степень\n" \
                          "// - однострочный комментарий\n" \
                          "mod - статок от деления\n" \
                          "div - целочисленное деление\n" \

        label_PASCAL_1_3 = tk.Label(self, text=text_PASCAL_1_3, justify=LEFT)
        label_PASCAL_1_3.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_1_4))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_2))
        button_NAZAD.place(x=555, y=400)


class PASCAL_1_4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_4 = "4. ОРГАНИЗАЦИЯ ВВОДА И ВЫВОДА ДАННЫХ\n" \
                          "\n" \
                          "Любой язык программирования должен иметь инструменты как для ввода данных, так и их\n" \
                          "вывода. В Pascal ввод осуществляется с помощью процедур read() и readln(), а вывод -\n" \
                          "- благодаря write() и writeln(). Процедуры, которые имеют окончание ln, после своего\n" \
                          "выполнения переводят указатель на новую строку. Рассмотрим пример программы,\n" \
                          "вычисляющей сумму введенных пользователемдвух чисел: \n" \
                          "\n" \
                          "program test;\n" \
                          "var\n" \
                          "        a,b,sum: integer;\n" \
                          "begin\n" \
                          "write('Введите первое число: ');\n" \
                          "readln(a);\n" \
                          "write('Введите второе число: ');\n" \
                          "readln(b);\n" \
                          "sum:= a+b;\n" \
                          "writeln('Сумма чисел: ',sum);\n" \
                          "end.\n"

        label_PASCAL_1_4 = tk.Label(self, text=text_PASCAL_1_4, justify=LEFT)
        label_PASCAL_1_4.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_1_5))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_3))
        button_NAZAD.place(x=555, y=400)

        button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_1))
        button_DIDA.place(x=327, y=400)


class PASCAL_1_5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_5 = "5. УСЛОВНЫЙ ОПЕРАТОР\n" \
                          "\n" \
                          "Бывает, что в процессе выполнения программы требуется реализовать разный набор команд\n" \
                          "в зависимости от произошедших до этого событий. Это достигается с помощью специальных\n" \
                          "конструкций – условных операторов. Чаще всего в качестве условного оператора в языках\n" \
                          "программирования используется конструкция if-then-else (если-то-иначе) или ее сокращенный\n" \
                          "вариант if-then, где оператор обязательно прописывается после отступа в 4 пробела. Для лучшего\n" \
                          "понимания рассмотрим пример программы, проверяющей, больше ли введенное число 16-ти:\n" \
                          "\n" \
                          "var\n" \
                          "        а: integer;\n" \
                          "begin\n" \
                          "write ('Введите целое число: ');\n" \
                          "readln (a);\n" \
                          "if a>16 then begin\n" \
                          "        write ('Число больше 16-ти.');\n" \
                          "end\n" \
                          "else\n" \
                          "        write ('Число меньше 16-ти.');\n" \
                          "end.\n" \
                          "\n" \



        label_PASCAL_1_5 = tk.Label(self, text=text_PASCAL_1_5, justify=LEFT)
        label_PASCAL_1_5.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_1_6))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_4))
        button_NAZAD.place(x=555, y=400)

        button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_2))
        button_DIDA.place(x=327, y=400)


class PASCAL_1_6(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_6 = "6. ЦИКЛ С ЗАДАННЫМ УСЛОВИЕМ ПРОДОЛЖЕНИЯ РАБОТЫ\n" \
                          "\n" \
                          "Оператором, отвечающим за данный вид цикла в Pascal, является while-do. Cтоит смотреть\n" \
                          "на это так: пока истинно условие, стоящее между while и do, выполняется оператор после do.\n" \
                          "Перед каждым заходом в цикл проверяется условие: если оно истинно, то выполняется оператор,\n" \
                          "если ложно, то автоматически осуществляется выход из цикла. Рассмотрим программу, которая\n" \
                          "определяет, сколько слагаемых должно быть в сумме последовательных чётных чисел (2+4+6+8+...),\n" \
                          "чтобы эта сумма оказалась больше некоторого заданного натурального числа n(n>=2),и выводит\n" \
                          "на экран результат - количество слагаемых.\n" \
                          "\n" \
                          "var\n" \
                          "        i, sum, n, x: integer; \n" \
                          "begin\n" \
                          "write ('n= ');\n" \
                          "readln (n)\n" \
                          "x:=2;\n" \
                          "sum:=2;\n" \
                          "i:=1;\n" \
                          "while sum <=n do begin\n" \
                          "x:=x+2;\n" \
                          "i:=i+1;\n" \
                          "sum:=sum+x;\n" \
                          "end;\n" \
                          "writeln(i,' слагаемых'); \n" \
                          "end.\n"

        label_PASCAL_1_6 = tk.Label(self, text=text_PASCAL_1_6, justify=LEFT)
        label_PASCAL_1_6.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_1_7))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_5))
        button_NAZAD.place(x=555, y=400)

        button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_3))
        button_DIDA.place(x=327, y=400)


class PASCAL_1_7(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_7 = "7. ЦИКЛ С ЗАДАННЫМ УСЛОВИЕМ ОКОНЧАНИЯ РАБОТЫ\n" \
                          "\n" \
                          "Цикл с постусловием — цикл, в котором условие проверяется после выполнения тела цикла.\n" \
                          "Отсюда следует, что тело всегда выполняется хотя бы один раз. В языке Паскаль этот цикл\n" \
                          "реализует оператор repeat..until. В отличие от цикла while, условие вычисляется после\n" \
                          "очередной итерации цикла, и если оно истинно, то происходит выход из цикла. Обычно оператор\n" \
                          "Обычно оператор repeat используют в ситуациях, где условие нельзя проверить, не выполнив\n" \
                          "тело цикла. Рассмотрим пример, где мы будем вводить с клавиатуры числа, и подсчитывать их\n" \
                          "сумму, но лишь до того момента, пока вводимые числа больше нуля:\n" \
                          "\n" \
                          "uses crt;\n" \
                          "var\n" \
                          "         sum, a:real;\n" \
                          "begin\n" \
                          "clrscr;\n" \
                          "sum:=0;\n" \
                          "a:=0;\n" \
                          "repeat\n" \
                          "sum:=sum+A;\n" \
                          "write ('Ведите число:');\n" \
                          "readln (a);\n" \
                          "until A<0;\n" \
                          "writeln (‘Сумма чисел = ’,sum:5:3);\n" \
                          "end.\n" \


        label_PASCAL_1_7 = tk.Label(self, text=text_PASCAL_1_7, justify=LEFT)
        label_PASCAL_1_7.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_1_8))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_6))
        button_NAZAD.place(x=555, y=400)

        button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_4))
        button_DIDA.place(x=327, y=400)


class PASCAL_1_8(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PASCAL_1_8 = "8. ЦИКЛ С ЗАДАННЫМ ЧИСЛОМ ПОВТОРЕНИЙ\n" \
                                  "\n" \
                                  "Цикл с заданным числом повторений программируется в Pascal с помощью оператора for.\n" \
                                  "Его общий вид:\n" \
                                  "\n" \
                                  "for <параметр>:=<начальное_значение> to <конечное_значение> do <оператор>\n" \
                                  "\n" \
                                  "Где <параметр> — переменная целого типа; <начальное_значение> и <конечное_значение> -\n" \
                                  "- выражения того же типа, что и параметр, вычисляемые перед началом цикла; При выполнении\n" \
                                  "этого оператора после каждого выполнения тела цикла происходит увеличение на единицу\n" \
                                  "параметра цикла; условием выхода из цикла является превышение параметром конечного\n" \
                                  "значения. Рассмотрим пример, в котором на консоль выводится число 20 10 раз:\n" \
                                  "\n" \
                                  "var \n" \
                                  "        i: byte;\n" \
                                  "begin\n" \
                                  "for i:=1 to 10 do write(20,' ');\n" \
                                  "end.\n"

                label_PASCAL_1_8 = tk.Label(self, text=text_PASCAL_1_8, justify=LEFT)
                label_PASCAL_1_8.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PAGE_GO_LEAN))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_1_7))
                button_NAZAD.place(x=555, y=400)

                button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_5))
                button_DIDA.place(x=327, y=400)


# ЗАКОНЧИЛАСЬ ПЕРВАЯ ЧАСТЬ ПАСКАЛЯ.

# НАЧИНАЕТСЯ ВТОРАЯ ЧАСТЬ ПАСКАЛЯ.


class PASCAL_2_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_1 = "1. ОПИСАНИЕ ОДНОМЕРНЫХ МАССИВОВ\n" \
                          "\n" \
                          "Массив - именованный набор однотипных переменных, расположенных в памяти друг за\n" \
                          "другом, доступ к которым осуществляется по индексу. Индекс массива -  целое число\n" \
                          "указывающее на конкретный элемент. Массив описывается в том же разделе, что и переменные;\n" \
                          "в var. Для описания массива сначала пишется его имя, после двоеточия пишется array,\n" \
                          " затем в квадратных скобках указывается размерность массива (его индексы). Например -\n" \
                          "- [1..10] — То есть индексы элементов с первого, по 10. Затем указывается тип элементов\n" \
                          "массива при помощи частицы of и, через пробел, сам тип элемента массива. Рассмотрим\n" \
                          "общий вид:\n" \
                          "\n" \
                          "var\n" \
                          "<имя массива>: array[<первый индекс> .. <последний индекс>] of <тип элементов>\n"

        label_PASCAL_2_1 = tk.Label(self, text=text_PASCAL_1_1, justify=LEFT)
        label_PASCAL_2_1.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                 command=lambda: controller.show_frame(PASCAL_2_2))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                           command=lambda: controller.show_frame(PAGE_GO_LEAN))
        button_NAZAD.place(x=555, y=400)


class PASCAL_2_2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_2_2 = "2. ЗАПОЛНЕНИЕ ОДНОМЕРНЫХ МАССИВОВ\n" \
                          "\n" \
                          "Заполнение и вывод массива можно осуществить только поэлементно, то есть можно сначала\n" \
                          "присвоить значение первому элементу, затем второму и так далее. Рассмотрим пример:\n" \
                          "\n" \
                          "a[1]:=5\n" \
                          "\n" \
                          "Массив можно заполнить случайными числами используя при этом модуль random. Для лучшего\n" \
                          "понимания рассмотрим пример программы, в которой массив из 10-ти элементов заполняется\n" \
                          "случайными числами:\n" \
                          "\n" \
                          "var\n" \
                          "        a: array [1..10] of integer;\n" \
                          "begin\n" \
                          "randomize();\n" \
                          "for i:=1 to 10 do\n" \
                          "begin\n" \
                          "a[i]:=random(<диапазон случайных чисел>);\n" \
                          "end;\n" \
                          "end.\n"


        label_PASCAL_2_2 = tk.Label(self, text=text_PASCAL_2_2, justify=LEFT)
        label_PASCAL_2_2.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_2_3))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_2_1))
        button_NAZAD.place(x=555, y=400)


class PASCAL_2_3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_1_3 = "3. ВЫВОД ОДНОМЕРНЫХ МАССИВОВ\n" \
                          "\n" \
                          "Вывод массива в Паскале осуществляется также поэлементно, в цикле, где параметром \n" \
                          "выступает индекс массива, принимая последовательно все значения от первого до последнего.\n" \
                          "Рассмотрим пример:\n" \
                          "\n" \
                          "var \n" \
                          "        a: array [1..10] of integer;\n" \
                          "        i: integer;\n" \
                          "begin\n" \
                          "for i :=1 to 10 do\n" \
                          "begin\n" \
                          "        write( a [ i ],' ');\n" \
                          "end;\n" \
                          "end.\n" \
                          "\n" \
                          "Для того, чтобы вывести только один определенный элемент можно использовать данную\n" \
                          "конструкцию:\n " \
                          "\n" \
                          "write(a[1]);\n"


        label_PASCAL_1_3 = tk.Label(self, text=text_PASCAL_1_3, justify=LEFT)
        label_PASCAL_1_3.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PASCAL_2_4))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_2_2))
        button_NAZAD.place(x=555, y=400)


class PASCAL_2_4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PASCAL_2_4 = "4. НАХОЖДЕНИЕ МАКСИМАЛЬНОГО И МИНИМАЛЬНОГО ЭЛЕМЕНТА МАССИВА\n" \
                          "\n" \
                          "Алгоритм нахождения максимального, и, по средством смены знака сравнения, минимального\n" \
                          "элемента массива, рассмотрим в примере:\n" \
                          "\n" \
                          "max := а[1];\n" \
                          "for i := 2 to 10 do\n" \
                          "        if a[i]>max then\n" \
                          "                max := a[i];\n" \
                          "\n" \
                          "Б`ольшим назначается первый элемент, далее происходит перебор индексов всех элементов.\n" \
                          "Элемент, назначенный максимальным, сравнивается с каждым из элементов массива, и если\n" \
                          "попадается какой либо со значением больше, чем у первого, он становится максимальным.\n" \


        label_PASCAL_2_4 = tk.Label(self, text=text_PASCAL_2_4, justify=LEFT)
        label_PASCAL_2_4.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PAGE_GO_LEAN))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PASCAL_2_3))
        button_NAZAD.place(x=555, y=400)

        button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_2_1))
        button_DIDA.place(x=327, y=400)


#

#


class PYTHON_1_0(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PYTHON_1_0 = "Python – это один из наиболее популярных современных языков программирования.\n" \
                                  "Он пригоден для решения разнообразных задач и предлагает те же возможности, что и\n" \
                                  "другие языки программирования: динамичность, поддержку ООП и кросс-платформенность.\n" \
                                  "Разработку Python начал Гвидо Ван Россум (Guido Van Rossum) еще в середине 1990-х\n" \
                                  "годов, поэтому к настоящему времени удалось существенно развить лучшие стороны языка\n" \
                                  "и привлечь множество программистов, использующих Python для реализации своих проектов.\n" \
                                  "\n" \
                                  "\n" \
                                  "\n"

                label_PYTHON_1_0 = tk.Label(self, text=text_PYTHON_1_0, justify=LEFT)
                label_PYTHON_1_0.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PYTHON_1_1))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_GO_LEAN))
                button_NAZAD.place(x=555, y=400)


class PYTHON_1_1(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PYTHON_1_1 = "1. ОПЕРАТОР ПРИСВАИВАНИЯ И СПЕЦИАЛЬНЫЕ СИМВОЛЫ\n" \
                                  "\n" \
                                  "Оператор присваивания имеет следующую структуру:\n" \
                                  "\n" \
                                  "<Переменная> = <Выражение> ;\n" \
                                  "\n" \
                                  "Теперь рассмотрим некоторые специальные символы:\n" \
                                  "\n" \
                                  "+ - сложение\n" \
                                  "- - вычитание\n" \
                                  "* - умножение\n" \
                                  "/ - деление\n" \
                                  "** - возведение в степень\n" \
                                  "== - равно\n" \
                                  "> - больше; < - меньше; >= - больше или равно; <= - меньше или равно; <>, != - не равно\n" \
                                  "// - целочисленное деление\n" \
                                  "% - остаток от деления\n" \


                label_PYTHON_1_1 = tk.Label(self, text=text_PYTHON_1_1, justify=LEFT)
                label_PYTHON_1_1.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PYTHON_1_2))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PYTHON_1_0))
                button_NAZAD.place(x=555, y=400)


class PYTHON_1_2(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PYTHON_1_2 = "2. ОРГАНИЗАЦИЯ ВВОДА И ВЫВОДА ДАННЫХ\n" \
                                  "\n" \
                                  "Любой язык программирования должен иметь инструменты как для ввода данных, так и их\n" \
                                  "вывода. Для вывода значений в Python есть функция print(). Внутри круглых скобок через\n" \
                                  "запятую мы пишем то, что хотим вывести. Для ввода данных в программу мы используем\n" \
                                  "функцию input() в скобках, перед которыми прописывается тип вводимых данных(можете\n" \
                                  "подсмотреть необходимый вам в интернете). Рассмотрим пример, где прогамма вычисляет\n" \
                                  "сумму введенных пользователем чисел(натурального типа; обозначаются как int):\n" \
                                  "\n" \
                                  "print('Введите первое число: ')\n" \
                                  "a=int(input())\n" \
                                  "print('Введите второе число: ')\n" \
                                  "b=int(input())\n" \
                                  "sum=a+b\n" \
                                  "print(sum)\n" \


                label_PYTHON_1_2 = tk.Label(self, text=text_PYTHON_1_2, justify=LEFT)
                label_PYTHON_1_2.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PYTHON_1_3))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PYTHON_1_1))
                button_NAZAD.place(x=555, y=400)

                button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_1))
                button_DIDA.place(x=327, y=400)


class PYTHON_1_3(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PYTHON_1_3 = "3. УСЛОВНЫЙ ОПЕРАТОР\n" \
                                  "\n" \
                                  "Условная инструкция if-else -  основной инструмент выбора в Python. Проще говоря, она\n" \
                                  "выбирает, какое действие следует выполнить, в зависимости от значения переменных в момент\n" \
                                  "проверки условия. Оператор внутри данного алгоритма обязан писаться с 4-мя отступами\n" \
                                  "относительно начала конструкции. Рассмотрим пример, где если пользователь вводит число\n" \
                                  "пять, программа выводит данную цифру буквенной записью, а иначе - говорит, что вы ввели\n" \
                                  "не пять:\n" \
                                  "\n" \
                                  "print('Введите число: ')\n" \
                                  "a=int(input())\n" \
                                  "if a==5:\n" \
                                  "        print('Пять')\n" \
                                  "else:\n" \
                                  "        print('Вы ввели не пять')\n"

                label_PYTHON_1_3 = tk.Label(self, text=text_PYTHON_1_3, justify=LEFT)
                label_PYTHON_1_3.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PYTHON_1_4))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PYTHON_1_2))
                button_NAZAD.place(x=555, y=400)

                button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_2))
                button_DIDA.place(x=327, y=400)


class PYTHON_1_4(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PYTHON_1_4 = "4. ЦИКЛ С ЗАДАННЫМ УСЛОВИЕМ ПРОДОЛЖЕНИЯ РАБОТЫ\n" \
                                  "\n" \
                                  "While - один из самых универсальных циклов в Python, поэтому довольно медленный. Выполняет\n" \
                                  "тело цикла пока условие цикла истинно. Поэтому этот цикл также иногда называют циклом 'пока'.\n" \
                                  "Часто цикл while используется, когда невозможно заранее предсказать, сколько раз необходимо\n" \
                                  "выполнить тело цикла. Рассмотрим пример, где пока введенное пользователем число не станет\n" \
                                  "больше пяти, программа будет прибавлять к нему единицу:\n" \
                                  "\n" \
                                  "print('Введите число: ')\n" \
                                  "a=int(input())\n" \
                                  "while a < 5:\n" \
                                  "        a=a+1\n" \


                label_PYTHON_1_4 = tk.Label(self, text=text_PYTHON_1_4, justify=LEFT)
                label_PYTHON_1_4.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PYTHON_1_5))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PYTHON_1_3))
                button_NAZAD.place(x=555, y=400)

                button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_3))
                button_DIDA.place(x=327, y=400)


class PYTHON_1_5(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)

                text_PYTHON_1_5 = "5. ЦИКЛ С ЗАДАННЫМ ЧИСЛОМ ПОВТОРЕНИЙ\n" \
                                  "\n" \
                                  "Встроенная функция Python под названием range может быть очень полезной, если вам нужно\n" \
                                  "выполнить действие определенное количество раз. Его общий вид:\n" \
                                  "\n" \
                                  "for <параметр> in range (<конечное_значение>):\n" \
                                  "        <оператор>\n" \
                                  "\n" \
                                  "Рассмотрим пример, в котором введенное пользователем число выводится на консоль 10 раз:\n" \
                                  "\n" \
                                  "print('Введите число: ')\n" \
                                  "a=int(input())\n" \
                                  "for 0 in range(10):\n" \
                                  "        print(a)\n"

                label_PYTHON_1_5 = tk.Label(self, text=text_PYTHON_1_5, justify=LEFT)
                label_PYTHON_1_5.place(relx=.120, rely=.10)

                button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PAGE_GO_LEAN))
                button_VPERED.place(x=480, y=400)

                button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PYTHON_1_4))
                button_NAZAD.place(x=555, y=400)

                button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_1_5))
                button_DIDA.place(x=327, y=400)


#

#


class PYTHON_2_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PYTHON_2_1 = "1. ОПИСАНИЕ И ЗАПОЛНЕНИЕ СПИСКА\n" \
                          "\n" \
                          "Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов.\n" \
                          "Описать их можно разным способами. Например, обработать любой итерируемый объект\n" \
                          "(например, строку) встроенной функцией list:\n" \
                          "\n" \
                          "list('<название списка>')\n" \
                          "['первый элемент списка', .. 'последний элемент списка']\n" \
                          "\n" \
                          "Или при помощи цикла, чтобы пользователь мог ввести значения самостоятельно:\n" \
                          "\n" \
                          "а = [0] * int(input())\n" \
                          "for i in range(len(а)):\n" \
                          "        а[i] = int(input())\n"

        label_PYTHON_2_1 = tk.Label(self, text=text_PYTHON_2_1, justify=LEFT)
        label_PYTHON_2_1.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                  command=lambda: controller.show_frame(PYTHON_2_2))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(PAGE_GO_LEAN))
        button_NAZAD.place(x=555, y=400)


class PYTHON_2_2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PYTHON_2_2 = "2. ВЫВОД СПИСКА\n" \
                          "\n" \
                          "Вывести элементы списка 'а' можно одной инструкцией print(а), при этом будут выведены\n" \
                          "квадратные скобки вокруг элементов списка и запятые между элементами списка. Рассмотрим\n" \
                          "первый вариант:\n" \
                          "\n" \
                          "for i in range(len(а)):\n" \
                          "        print(а[i])\n" \
                          "\n" \
                          "В следующем примере элементы списка будут выводиться в одну строку, разделенные пробелом,\n" \
                          "при этом в цикле меняется не индекс элемента списка, а само значение переменной (например,\n" \
                          "в цикле for elem in ['red', 'green', 'blue'] переменная elem будет последовательно принимать\n" \
                          "значения 'red', 'green', 'blue'.\n" \
                          "\n" \
                          "for elem in а:\n" \
                          "       print(elem, end = ' ')\n"

        label_PYTHON_2_2 = tk.Label(self, text=text_PYTHON_2_2, justify=LEFT)
        label_PYTHON_2_2.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                  command=lambda: controller.show_frame(PYTHON_2_3))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(PYTHON_2_1))
        button_NAZAD.place(x=555, y=400)


class PYTHON_2_3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PYTHON_2_3 = "3. ОСНОВНЫЕ ОПЕРАЦИИ СО СПИСКАМИ\n" \
                          "\n" \
                          "Многие манипуляции со списками в Pascal возможно выполнить без использования громоздких\n" \
                          "алгоритмов, а лишь с помощью кратких специальных команд, результат которых можно\n" \
                          "присвоить переменной или просто вывести на экран. Рассмотрим наиболее важные и часто\n" \
                          "используемые из них:\n" \
                          "\n" \
                          "min(a) - минимальный элемент списка 'а'\n" \
                          "\n" \
                          "max(a) - максимальный элемент списка 'а'\n" \
                          "\n" \
                          "x in a - проверка принадлежности элемента 'х' к списку 'а'\n" \
                          "\n" \
                          "a.count(x) - кол - во элемента 'х' к списку 'а'\n" \
                          "\n" \
                          "sorted(a) - сортировка списка 'а' по возрастанию\n" \
                          "\n" \
                          "sorted(a, reverse=1) - сортировка списка 'а' по убыванию\n" \

        label_PYTHON_2_3 = tk.Label(self, text=text_PYTHON_2_3, justify=LEFT)
        label_PYTHON_2_3.place(relx=.120, rely=.10)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                  command=lambda: controller.show_frame(PAGE_GO_LEAN))
        button_VPERED.place(x=480, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(PYTHON_2_2))
        button_NAZAD.place(x=555, y=400)

        button_DIDA = tk.Button(self, text="ЗАДАЧА ПО ТЕМЕ", pady="10", padx="20",
                                         command=lambda: controller.show_frame(DIDA_2_1))
        button_DIDA.place(x=327, y=400)


#

#


class PAGE_DIDA_1 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        button_DIDA_1 = tk.Button(self, text="ОРГАНИЗАЦИЯ ВВОДА И ВЫВОДА ДАННЫХ", pady="10", padx="51",
                                           command=lambda: controller.show_frame(DIDA_1_1))
        button_DIDA_1.place(x=20, y=20)

        button_DIDA_2 = tk.Button(self, text="УСЛОВНЫЙ ОПЕРАТОР", pady="10", padx="108",
                                           command=lambda: controller.show_frame(DIDA_1_2))
        button_DIDA_2.place(x=20, y=100)

        button_DIDA_3 = tk.Button(self, text="ЦИКЛ С ЗАДАННЫМ УСЛОВИЕМ ПРОДОЛЖЕНИЯ РАБОТЫ", pady="10", padx="9",
                                           command=lambda: controller.show_frame(DIDA_1_3))
        button_DIDA_3.place(x=20, y=180)

        button_DIDA_4 = tk.Button(self, text="ЦИКЛ С ЗАДАННЫМ УСЛОВИЕМ ОКОНЧАНИЯ РАБОТЫ", pady="10", padx="17",
                                           command=lambda: controller.show_frame(DIDA_1_4))
        button_DIDA_4.place(x=20, y=260)

        button_DIDA_5 = tk.Button(self, text="ЦИКЛ С ЗАДАННЫМ ЧИСЛОМ ПОВТОРЕНИЙ", pady="10", padx="45",
                                           command=lambda: controller.show_frame(DIDA_1_5))
        button_DIDA_5.place(x=20, y=340)


        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                           command=lambda: controller.show_frame(PAGE_MAIN_MENU))
        button_NAZAD.place(x=555, y=400)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(PAGE_DIDA_2))
        button_VPERED.place(x=480, y=400)


class DIDA_1_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_1_1 = "Напишите программу, вычисляющую площадь прямоугольного треугольника (s = 1/2*a*b) с\n" \
                        "помощью введенных пользователем значений катетов (a, b) и выведите ответ.\n" \


        label_DIDA_1_1 = tk.Label(self, text=text_DIDA_1_1, justify=LEFT)
        label_DIDA_1_1.place(relx=.120, rely=.10)

        button_OTVET = tk.Button(self, text="ПРИМЕР РЕШЕНИЯ", pady="10", padx="20",
                                          command=lambda: controller.show_frame(DIDA_OTVET_1))
        button_OTVET.place(x=397, y=400)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_NAZAD.place(x=555, y=400)


class DIDA_1_2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_1_2 = "Напишите программу, которая, после вводе пользователем возраста, если тот младше 14, просит\n" \
                        "предъявить свидетельство о рождении, иначе - паспорт.\n"

        label_DIDA_1_2 = tk.Label(self, text=text_DIDA_1_2, justify=LEFT)
        label_DIDA_1_2.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_NAZAD.place(x=555, y=400)

        button_OTVET = tk.Button(self, text="ПРИМЕР РЕШЕНИЯ", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_2))
        button_OTVET.place(x=397, y=400)


class DIDA_1_3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_1_3 = "Напишите программу, которая при вводе двух целых чисел находит их наибольший общий\n" \
                        "делитель.\n"

        label_DIDA_1_3 = tk.Label(self, text=text_DIDA_1_3, justify=LEFT)
        label_DIDA_1_3.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_NAZAD.place(x=555, y=400)

        button_OTVET = tk.Button(self, text="ПРИМЕР РЕШЕНИЯ", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_3))
        button_OTVET.place(x=397, y=400)


class DIDA_1_4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_1_4 = "Напишите программу, определяющуе максимальное число в последовательности положительных\n" \
                        "чисел, что заканчивается нулем.\n"

        label_DIDA_1_4 = tk.Label(self, text=text_DIDA_1_4, justify=LEFT)
        label_DIDA_1_4.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_NAZAD.place(x=555, y=400)

        button_OTVET = tk.Button(self, text="ПРИМЕР РЕШЕНИЯ", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_4))
        button_OTVET.place(x=397, y=400)


class DIDA_1_5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_PYTHON_1_5 = "Напишите программу, выводящую стоимость 1.2, 1.4, ..., 2 кг конфет, если известна цена за 1 кг.\n"

        label_PYTHON_1_5 = tk.Label(self, text=text_PYTHON_1_5, justify=LEFT)
        label_PYTHON_1_5.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_NAZAD.place(x=555, y=400)

        button_OTVET = tk.Button(self, text="ПРИМЕР РЕШЕНИЯ", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_5))
        button_OTVET.place(x=397, y=400)


#

#


class PAGE_DIDA_2 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                           command=lambda: controller.show_frame(PAGE_DIDA_1))
        button_NAZAD.place(x=555, y=400)

        button_DIDA_2_1 = tk.Button(self, text="ОПИСАНИЕ И ВЫВОД МАССИВА/СПИСКА", pady="10", padx="55",
                                           command=lambda: controller.show_frame(DIDA_2_1))
        button_DIDA_2_1.place(x=20, y=20)


class DIDA_2_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_2_1 = "Напишите программу, которая станет содержать массив/список, заполненный случайными\n" \
                        "числами, и выведите сумму всех элементов, а также максимальный его элемент.\n"

        label_DIDA_2_1 = tk.Label(self, text=text_DIDA_2_1, justify=LEFT)
        label_DIDA_2_1.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                         command=lambda: controller.show_frame(PAGE_DIDA_2))
        button_NAZAD.place(x=555, y=400)

        button_OTVET = tk.Button(self, text="ПРИМЕР РЕШЕНИЯ", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_6))
        button_OTVET.place(x=397, y=400)

#

#


class DIDA_OTVET_1 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_1 = "PASCAL:\n" \
                            "\n" \
                            "program test;\n" \
                            "var\n" \
                            "        a,b,s: real;\n" \
                            "begin\n" \
                            "writeln('Введите 1-й катет: ');\n" \
                            "read(a);\n" \
                            "writeln('Введите 2-й катет: ');\n" \
                            "read(b);\n" \
                            "s:=a*b*1/2;\n" \
                            "writeln(s);\n" \
                            "end.\n" \
                            "\n" \
                            "PYTHON:\n" \
                            "\n" \
                            "print('Введите 1-й катет: ')\n" \
                            "a=float(input())\n" \
                            "print('Введите 2-й катет: ')\n" \
                            "b=float(input())\n" \
                            "s=a*b*1/2\n" \
                            "print(s)\n"


        label_DIDA_OTVET_1 = tk.Label(self, text=text_DIDA_OTVET_1, justify=LEFT)
        label_DIDA_OTVET_1.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_1_1))
        button_NAZAD.place(x=555, y=400)


class DIDA_OTVET_2 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_2 = "PASCAL:\n" \
                            "\n" \
                            "program test;\n" \
                            "var\n" \
                            "        a,b,s: real;\n" \
                            "begin\n" \
                            "writeln('Введите свой возраст: ');\n" \
                            "read(a);\n" \
                            "if a<14 then begin\n" \
                            "writeln('Предъявите свидетельство о рождении');\n" \
                            "end\n" \
                            "else\n" \
                            "writeln('Предъявите паспорт');\n" \
                            "end. \n" \
                            "\n" \
                            "PYTHON:\n" \
                            "\n" \
                            "print('Введите свой возраст: ')\n" \
                            "a=float(input())\n" \
                            "if a<14:\n" \
                            "        print('Предъявите свидетельство о рождении')\n" \
                            "else:\n" \
                            "        print('Предъявите паспорт')\n"

        label_DIDA_OTVET_2 = tk.Label(self, text=text_DIDA_OTVET_2, justify=LEFT)
        label_DIDA_OTVET_2.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_1_2))
        button_NAZAD.place(x=555, y=400)


class DIDA_OTVET_3 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_3 = "PASCAL:\n" \
                            "\n" \
                            "program test;\n" \
                            "var\n" \
                            "z:real;\n" \
                            "m,i,a,b:integer;\n" \
                            "begin\n" \
                            "writeln('a,b =');\n" \
                            "readln(a,b);\n" \
                            "if a<b then m:=a else m:=b;\n" \
                            "for i:=1 to m do\n" \
                            "if (a mod i = 0) and (b mod i = 0) then z:=i;\n" \
                            "writeln(z:6:2);\n" \
                            "end.\n" \
                            "\n" \
                            "PYTHON:\n" \
                            "\n" \
                            "a = int(input())\n" \
                            "b = int(input())\n" \
                            "while a != 0 and b != 0:\n" \
                            "        if a > b:\n" \
                            "                a %= b\n" \
                            "        else:\n" \
                            "                b %= a\n" \
                            "gcd = a + b\n" \
                            "print(gcd)\n"

        label_DIDA_OTVET_3 = tk.Label(self, text=text_DIDA_OTVET_3, justify=LEFT)
        label_DIDA_OTVET_3.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_1_3))
        button_NAZAD.place(x=555, y=400)


class DIDA_OTVET_4 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_4 = "PASCAL:\n" \
                            "\n" \
                            "var\n" \
                            "        m, max: Integer;\n" \
                            "begin\n" \
                            "writeLn('Введите последовательность целых чисел, оканчивающуюся нулём: ');\n" \
                            "read(max);\n" \
                            "repeat\n" \
                            "        read(m);\n" \
                            "        if m=0 then break\n" \
                            "        else if max<m then max:=m;\n" \
                            "until False;\n" \
                            "writeln('Max = ', max);\n" \
                            "end.\n"

        label_DIDA_OTVET_4 = tk.Label(self, text=text_DIDA_OTVET_4, justify=LEFT)
        label_DIDA_OTVET_4.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_1_4))
        button_NAZAD.place(x=555, y=400)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                          command=lambda: controller.show_frame(DIDA_OTVET_4_2))
        button_VPERED.place(x=480, y=400)


class DIDA_OTVET_4_2 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_4 = "PYTHON:\n" \
                            "\n" \
                            "p = int(input())\n" \
                            "c = 1\n" \
                            "b = 1\n" \
                            "while True:\n" \
                            "        v = int(input())\n" \
                            "        if v == p:\n" \
                            "                if v == 0:\n" \
                            "                        break\n" \
                            "                c += 1\n" \
                            "        else:\n" \
                            "                if c > b:\n" \
                            "                        b = c\n" \
                            "                 p = v\n" \
                            "                 c = 1\n" \
                            "print(b)\n"

        label_DIDA_OTVET_4 = tk.Label(self, text=text_DIDA_OTVET_4, justify=LEFT)
        label_DIDA_OTVET_4.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_4))
        button_NAZAD.place(x=555, y=400)


class DIDA_OTVET_5 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_5 = "PASCAL:\n" \
                            "\n" \
                            "program test;\n" \
                            "var\n" \
                            "        c:real;\n" \
                            "        i:integer;\n" \
                            "begin\n" \
                            "write('Введите стоимость 1 кг конфет: ')\n" \
                            "readln(c);\n" \
                            "for i:=1 to 5 do\n" \
                            "writeln(1+i/5:0:1,' кг=',(1+i/5)*c:0:2);\n" \
                            "end.\n"\
                            "\n" \
                            "PYTHON(стоимость 1 кг случайная):\n" \
                            "\n" \
                            "import random\n" \
                            "price = round(random.uniform(0, 100),2)\n" \
                            "for 1 in range(5):\n" \
                            "print(1+i/5:0:1, '=', (1+i/5)*c:0:2)\n" \
                            "print('Цена 1 кг конфет: ', price)\n" \
                            "print()\n" \
                            "for i in range(0,5):\n" \
                            "x = 1.2 + 0.2*i\n" \
                            "print('Стоимость {0:.1f} кг: {1:.2f}'.format(x, x * price))\n" \
                            "print()\n"

        label_DIDA_OTVET_5 = tk.Label(self, text=text_DIDA_OTVET_5, justify=LEFT)
        label_DIDA_OTVET_5.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_1_5))
        button_NAZAD.place(x=555, y=400)


class DIDA_OTVET_6 (tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_6 = "PASCAL:\n" \
                            "\n" \
                            "program text;\n" \
                            "var \n" \
                            "        f: array[1..10] of integer;\n" \
                            "        i, max:integer;\n" \
                            "begin\n" \
                            "randomize;\n" \
                            "for i:=1 to 10 do\n" \
                            "        begin\n" \
                            "                f[i]:=random(10);\n" \
                            "                write(f[i],' ');\n" \
                            "        end;\n" \
                            "max:= f[1];\n" \
                            "        for i := 2 to 10 do\n" \
                            "                if f[i]>max then max := f[i];\n" \
                            "        writeln('Максимальный Элемент массива = ',max)\n" \
                            "end.\n"

        label_DIDA_OTVET_6 = tk.Label(self, text=text_DIDA_OTVET_6, justify=LEFT)
        label_DIDA_OTVET_6.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_2_1))
        button_NAZAD.place(x=555, y=400)

        button_VPERED = tk.Button(self, text="<---", pady="10", padx="20",
                                 command=lambda: controller.show_frame(DIDA_OTVET_6_1))
        button_VPERED.place(x=480, y=400)


class DIDA_OTVET_6_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        text_DIDA_OTVET_4 = "PYTHON:\n" \
                            "\n" \
                            "import random\n" \
                            "a=[0]*10\n" \
                            "for i in range(10):\n" \
                            "        a[i]=random.randint(0.10)\n" \
                            "b=max(a)\n" \
                            "print(b)\n"

        label_DIDA_OTVET_4 = tk.Label(self, text=text_DIDA_OTVET_4, justify=LEFT)
        label_DIDA_OTVET_4.place(relx=.120, rely=.10)

        button_NAZAD = tk.Button(self, text="НАЗАД", pady="10", padx="20",
                                    command=lambda: controller.show_frame(DIDA_OTVET_6))
        button_NAZAD.place(x=555, y=400)


app = WizardLikeApp()
app.mainloop()