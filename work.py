from random import *
import json

notes={"Phones": {"Alex": ["+ 375 29 125 48 63", "+375 33 256 96 86"]}, 
        "shopping in the store": {"list": ["+375 29 859 63 12"]}, 
        "My cards": ["4400568780235152", "1458659256982356"]}

def save():
    with open("notes.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(notes,ensure_ascii=False))
    print("Заметка добавлена в файл notes.json")
while True:
    command=input('Изучите перечень команд через ввод цифры "0".Введите команду 0:')

    if command=="1":

        print('Список заметок: ')
        print(notes)
    elif command=="2":
        f=input('Введите название заметки: ')
        k=input('Введите заметку: ')
        notes[f]=k
        save()
        print ("Заметка была успешно добавлена в список")
    elif command == "0":
        print('1 - список заметок, 2 - добавить заметку, 3 - удалить заметку, 4 - редактирование заметки, 5-поиск заметки, 6- загрузить измененный список заметок')
    elif command=="3":
        f=input('Введите имя заметки, который нужно удалить:')  
        try:
            del notes[f]
            print('Заметка успешно удалена')  
        except:
            print('Такой заметки нет в списке')   
    elif command == "4":
        n=input('Введите имя редактируемой заметки: ')
        q=notes[n]
        print(q)
        m=input('Введите отредактированное имя заметки: ')
        b=input('Виедите отредактированную заметку: ')
        notes[n]=b
        notes[m] = notes[n]
        del notes[n]
        print('Заметка была успешно изменена')
        print(notes)
    elif command =="5":
        a=input('Введите имя списка для поиска: ')
        with open("notes.json","r",encoding="utf-8") as fh:
            score =0
            while True:
                x=fh.readline()
                if a in x:
                    score+=1
                    print(notes[a])
                elif x=='':
                    if score>0:
                        break
                    else:
                        print("Таких данных нет")
                        break
  
    elif command=="6":
        with open ("notes.json","r",encoding="utf-8") as fh:
            notes=json.load(fh)
        print('Список был успешно загружен.')     
    else:
        print('Неопознанная команда. Просьба изучить мануал через команду /help')