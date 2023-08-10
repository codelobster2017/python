import ast
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# {имя: [телефон, комментарий]}
# phone.txt

def help():
    print('create() - очистить справочник')
    print('out() - вывод всего справочника')
    print('search("Name") - поиск по имени')
    print('delete("Name") - удалить номер')
    print('add("Name", "number", "comment")) - добавить/изменить номер')
    print('save() - сохранить и выйти')
    inp()

print('Создать новый файл или открыть старый?')
print('new - новый, иначе - открыть')

create = input()
file = 'phone.txt'
if create == 'new':
    all = {}
    with open(file, 'w', encoding='UTF-8') as files:
        files.write(str(all))
    print('Введите help() для справки')
else:
    with open(file, 'r', encoding='UTF-8') as files: 
        all = ast.literal_eval(files.read())
    print('Введите help() для справки')

def inp ():
    eval(input())

def out(all = all): 
    for i in all:
        print('Имя: ', i, ' Номер: ', all[i][0], ' Комментарий: ', all[i][1])
    inp()

def search(name, all = all):
    print('Поиск по имени:', name,  ' Номер:', all[name][0], ' Комментарий:', all[name][1])
    inp()

def delete(name):
    del all[name]
    print('Удален номер ', name)
    inp()

def add(name, numm, comm, all = all):
    all[name] = [numm, comm]
    inp()

def save(all = all):
    with open('phone.txt', 'w', encoding='UTF-8') as files: 
        files.write(str(all))
    print('Сохранено')

inp()