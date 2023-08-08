# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

print('out() - вывод всего справочника')
print('out_name("Name") - поиск по имени')
print('delete("Name") - удалить номер')
print('add("Name", Number) - добавить/изменить номер')

dict_number = {'Иванов':111, 'Петров':333, 'Сидоров':666}

def out(TD = dict_number):
    for i in TD:
        print(i, ' - ', TD[i])
    eval(input())

def out_name(name, dn = dict_number):
    print(dn[name])
    eval(input())
    
def delete(name, dn = dict_number):
    del dn[name]
    print('Удалено')
    eval(input())

def add(name, number):
    print('Добавлено или изменено')
    dict_number[name] = number
    eval(input())

def stop():
    print('Выход')

eval(input())