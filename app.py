from tkinter import *
import webbrowser

# Создание приложения
app = Tk()
app.title("Поисковая система")
app.configure(bg="#ececec")


# Переменная для записи выбора поисковой системы
search_engine = StringVar()
search_engine.set('Google')


# Поиск информации в интернете
def search(event=True):
    if search_engine.get() == 'Google':
        if text_field.get().strip() != '':
            webbrowser.open('https://www.google.ru/search?q=' + text_field.get())
    else:
        if text_field.get().strip() != '':
            webbrowser.open('https://yandex.ru/search/?text=' + text_field.get())


# Создание текстовой записи
app_name = Label(app, text="Поисковое приложение", font="verdana 24 bold italic", fg="#333")
app_name.grid(row=0, column=1)

search_label = Label(app, text="Поиск")
search_label.grid(row=1, column=0,)


# Создание поля для ввода информации
text_field = Entry(app, width=50)
text_field.grid(row=1, column=1)
# Отслеживания события нажатия на клавишу Enter
text_field.bind('<Return>', search)
text_field.focus()

# Кнопка поиска
btn_search = Button(app, text="Найти", width=10, command=search)
btn_search.grid(row=1, column=2)

radio_google = Radiobutton(app, text="Google", value="Google", variable=search_engine)
radio_google.grid(row=2, column=1, sticky=W)

radio_yandex = Radiobutton(app, text="Yandex", value="Yandex", variable=search_engine)
radio_yandex.grid(row=2, column=1, sticky=E)

app.wm_attributes('-topmost', True)

# Функция, не позволяющая закрывать приложение
app.mainloop()
