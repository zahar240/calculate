#место для библиотек
from tkinter import *


#раздел функций и классов (математика)

#функционал кнопки
def calculate(Event):
    print('вы нажали первую кнопку')
    try:
        x = float(input_prise1.get())
        y = float(input_prise2.get())     
        output_prise.delete(0, END)
        func=choose_radiobutton.get()
        if func==1:
            output_prise.insert(0, x + y)
        elif func==2:
            output_prise.insert(0, x - y)
        elif func==3:
            output_prise.insert(0, x * ( 1 - y / 100 ))
    except ValueError:
        lebel_error['text'] = "Ошибка ввода: введите число" 

#главное окно
root = Tk()
root.resizable(width=False, height=False)
root.title('Калькулятор скидок \"Орифлейм\"')
root.geometry('400x200')

#часть первая - создание элементов

#надписи
label1=Label(root, text='Цена(Сумма)', font=(None, 15), fg="blue")
label2=Label(root, text='Скидка(Цена)', font=(None, 15), fg="blue")
label3=Label(root, text='Результат', font=(None, 15), fg="blue")
label_version=Label(root, text='Calculate 1.0', fg='#aaaaaa', anchor='w')
label_made=Label(root, text='© NextNet', fg='#aaa999', anchor='w')
lebel_error=Label(root, font=(None, 15), fg="red")

#блоки ввода-вывода
input_prise1 = Entry (root, justify="center", font=(None, 13))
input_prise2 = Entry (root, justify="center", font=(None, 13))
output_prise = Entry (root, justify="center", font=(None, 13))

#кнопка
calculate_button = Button(root, text='Расчет',  font=(None, 12), bg="#fff13c", fg="#b71c1c")
calculate_button.bind('<Button-1>', calculate )

#кнопка выбора
choose_radiobutton = IntVar()
plus_radiobutton = Radiobutton(root, text='Сложить', value=1, variable=choose_radiobutton, anchor='w', font=(None, 13), fg="#f57c00")
minus_radiobutton = Radiobutton(root, text='Вычесть', value=2, variable=choose_radiobutton, anchor='w',font=(None, 13), fg="#f57c55")
discount_radiobutton = Radiobutton(root, text='Скидка', value=3, variable=choose_radiobutton, anchor='w', font=(None, 13), fg="#ff0000")
choose_radiobutton.set(1)

#часть вторая - размещение объектов(созданных в части номер 1)

#надписи
label1.place(width=140, height=20, x=5, y=20)
label2.place(width=140, height=20, x=5, y=60)
label3.place(width=140, height=20, x=5, y=100)
label_version.place(x=1, y=180)
label_made.place(x=330, y=180)
lebel_error.place(x=110, y=145)

#блоки ввода-вывода
input_prise1.place(width=130, height=20, x=150, y=20)
input_prise2.place(width=130, height=20, x=150, y=60)
output_prise.place(width=130, height=20, x=150, y=100)

#кнопка
calculate_button.place(width=100, height=40, x=10, y=140)

#кнопка выбора
plus_radiobutton.place(width=100, height=20, x=300, y=20)
minus_radiobutton.place(width=100, height=20, x=300, y=60)
discount_radiobutton.place(width=100, height=20, x=300, y=100)

root.mainloop()