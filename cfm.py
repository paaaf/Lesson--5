import os
import shutil
import sys
from famous_persons import *
from game_balans import balans

parent_direct = '/download/ConsFailManager/'
while True:
    print('1. создать папку                                  2. удалить (файл/папку)           3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории        5. посмотреть только папки        6. посмотреть только файлы ')
    print('7. просмотр информации об ОС                      8. создатель программы            9. играть в викторину')
    print('10. мой банковский счет                           11. смена рабочей директории(*)   12. выход ')
    choice = input('Выберите и введите пункт меню : ')

    if choice == '1':
        name_folder = str(input('Введите название для directory : '))
        # создать папку, проверка на существование папки
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)

    elif choice == '2':
        delete_directory = str(input('Введите название directory(file) для удаления : '))
        if os.path.isfile(delete_directory):
            os.remove(delete_directory)
            print('File is deleted \n')
        elif os.path.isdir(delete_directory):
            os.rmdir(delete_directory)
            print('Directory is deleted \n')
        else:
            #os.rmdir(delete_directory)
            print('Vi ykazali ne syshestv direct \n')

    elif choice == '3':
        # копировать (файл/папку)
        # пользователь вводит название папки/файла и новое название папки/файла. Копируем
        copy_dir = str(input('Введите название папки/файла, для копирования : '))
        new_dir = str(input('Введите новое имя для папки/файла : '))
        if os.path.isfile(copy_dir):
            shutil.copyfile(copy_dir, new_dir)
            print('Mission for coping file is done')
        elif os.path.isdir(copy_dir):
            shutil.copytree(copy_dir, new_dir)
            print('Mission for coping directory is done')
        else:
            print('Unknown name YOUR file >:-( ')
        print('Операция закончена ')

    elif choice == '4':
        print('Содержимое рабочей directory : ')
        print(os.listdir(parent_direct), '\n') # VSE 4TO EST' V PAPKE PROEKTA

    elif choice == '5':
        #посмотреть только папки
        if os.listdir(parent_direct) == '':
            for dirs, folder, files in os.walk(parent_direct):
                print('Папки рабочей директории проекта : \n', folder, '\n')
                break
        else:
            print('Содержимое директории : \n')
            print(os.listdir(parent_direct), '\n')

    elif choice == '6':
        #посмотреть только файлы
        for dirs, folder, files in os.walk(parent_direct):
            print('Файлы рабочей директории проекта : ', files)
            print('\n')
            break

    elif choice == '7':
        print('Платформа : ', sys.platform, '\n')

    elif choice == '8':
        #создатель программы
        print('Я создатель, пара, нет, я проста нагрелся, что аж дождь, капающий, становится паром:\n'
              'иии так\n'
              'с горем, пополам, пишу программу уже неделю(эту), почти, модули эти, \n'
              'похожи друг на друга, но не похожи. Трудно быть, создателем, программм (:.. \n'
              'тяжело в учении, легко в бою \n'
              'прорвёмся \n'
              'спасибо за кураторство (^^) and be happy  \n')

    elif choice == '9':
        #играть в викторину
        rounds = int(input('Сколько раз вы хотите играть?'))
        for i in range(rounds):
            get_person_and_question()
        print('Ну, ты это, заходи если ЧО!')

    elif choice == '10':
        #мой банковский счет. proga s pokypkoi iz prowlogo DZ
        balans()

    elif choice == '11':
        #смена рабочей директории
        new_directory = str(input('Пожалуйста, введите название директории, для перехода(создания) в неё (её) : '))
        print('Path parent directory :  ', parent_direct)
        print(os.getcwd())
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
        parent_direct = os.path.join(new_directory)
        os.chdir(new_directory)
        print('Path parent directory :  ', parent_direct)
        print(os.getcwd())
    elif choice == '12':
        print('Выход произведён. Всего доброго! \n')
        sys.exit(66) # POIGRAT' S 0
    else:
        print('Неверный пункт меню')