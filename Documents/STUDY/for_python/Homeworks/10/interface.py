import api
from dateutil.parser import parse
from tkinter import *
from tkinter.ttk import Combobox
import database


def get_combo_values():
    if orig_curr_combo.get() == 'Белорусский рубль':
        orig_curr_value = 'BYN'
    elif orig_curr_combo.get() == 'Доллар США':
        orig_curr_value = 'USD'
    elif orig_curr_combo.get() == 'Евро':
        orig_curr_value = 'EUR'
    elif orig_curr_combo.get() == 'Китайский юань':
        orig_curr_value = 'CNY'
    elif orig_curr_combo.get() == 'Казахстанский тенге':
        orig_curr_value = 'KZT'
    elif orig_curr_combo.get() == 'Польский злотый':
        orig_curr_value = 'PLN'
    elif orig_curr_combo.get() == 'Российский рубль':
        orig_curr_value = 'RUB'
    elif orig_curr_combo.get() == 'Турецкая лира':
        orig_curr_value = 'TRY'
    elif orig_curr_combo.get() == 'Украинская гривна':
        orig_curr_value = 'UAN'
    elif orig_curr_combo.get() == 'Швейцарский франк':
        orig_curr_value = 'CHF'
    if transf_curr_combo.get() == 'Белорусский рубль':
        transf_curr_value = 'BYN'
    elif transf_curr_combo.get() == 'Доллар США':
        transf_curr_value = 'USD'
    elif transf_curr_combo.get() == 'Евро':
        transf_curr_value = 'EUR'
    elif transf_curr_combo.get() == 'Китайский юань':
        transf_curr_value = 'CNY'
    elif transf_curr_combo.get() == 'Казахстанский тенге':
        transf_curr_value = 'KZT'
    elif transf_curr_combo.get() == 'Польский злотый':
        transf_curr_value = 'PLN'
    elif transf_curr_combo.get() == 'Российский рубль':
        transf_curr_value = 'RUB'
    elif transf_curr_combo.get() == 'Турецкая лира':
        transf_curr_value = 'TRY'
    elif transf_curr_combo.get() == 'Украинская гривна':
        transf_curr_value = 'UAN'
    elif transf_curr_combo.get() == 'Швейцарский франк':
        transf_curr_value = 'CHF'
    return orig_curr_value, transf_curr_value

def get_curr_value():
    return float(entry_field.get())

def clicked():
    orig_curr_value = get_combo_values()[0]
    transf_curr_value = get_combo_values()[1] 
    amount = get_curr_value()
    result_lbl.configure(text=f"{amount} {orig_curr_value} = {api.convert_currency(orig_curr_value, transf_curr_value, amount)} {transf_curr_value}")
    result_lbl.configure(bg = 'dark slate gray', fg = 'white')
    database.dbrefresh(orig_curr_value, transf_curr_value)
    grade_lbl.configure(text = database.dbsort().head(3)[['pairs', 'quantity']])
    time_upd_lbl.configure(text = f'Последнее обновление данных: {api.get_update_time()}')


    
window = Tk()  
window.configure(bg='dark slate gray')
window.title("Конвертер валют")  
window.geometry('600x200')  
orig_curr_lbl = Label(window, text="Исходная валюта", bg='dark slate gray', fg='white', font=("Bahnschrift SemiBold Condensed", 14))  
orig_curr_lbl.place(x=10, y=5)
orig_curr_combo = Combobox(window)
orig_curr_combo['values'] = ('Белорусский рубль', 'Доллар США', 'Евро', 'Китайский юань', 'Казахстанский тенге', 'Польский злотый', 'Российский рубль', 'Турецкая лира', 'Украинская гривна', 'Швейцарский франк')  
orig_curr_combo.place(x=10, y=30)
transf_curr_lbl = Label(window, text="Валюта перевода", bg='dark slate gray', fg='white', font=("Bahnschrift SemiBold Condensed", 14), padx = 20)  
transf_curr_lbl.place(x=180, y=5)
transf_curr_combo = Combobox(window)
transf_curr_combo['values'] = ('Белорусский рубль', 'Доллар США', 'Евро', 'Китайский юань', 'Казахстанский тенге', 'Польский злотый', 'Российский рубль', 'Турецкая лира', 'Украинская гривна', 'Швейцарский франк')
transf_curr_combo.place(x=200, y=30)
amount_orig_lbl = Label(window, text="Количество", bg='dark slate gray', fg='white', font=("Bahnschrift SemiBold Condensed", 14))  
amount_orig_lbl.place(x=10, y= 50)
entry_field = Entry(fg="black", bg="white", width=20)
entry_field.place(x=10, y=75)
btn = Button(window, text="Перевести", command=clicked)  
btn.place(x=10, y=100)
result_lbl = Label(window, text="", bg='dark slate gray', fg='dark slate gray', font=("Bahnschrift SemiBold Condensed", 14))  
result_lbl.place(x=200, y=70)
top_lbl = Label(window, text='Самые частые запросы', bg = 'dark slate gray', fg = 'white')
top_lbl.place(x=450, y=10)
grade_lbl = Label(window, text = database.dbsort().head(3)[['pairs', 'quantity']], bg = 'dark slate gray', fg = 'white')
grade_lbl.place(x=450, y = 30)
time_upd_lbl = Label(window, text = f'Последнее обновление данных: {api.get_update_time()}', bg = 'dark slate gray', fg = 'white')
time_upd_lbl.place(x=10, y=170)
author_lbl = Label(window, text='by Korsounn', bg = 'dark slate gray', fg = 'white')
author_lbl.place(x=500, y=170)
window.mainloop()