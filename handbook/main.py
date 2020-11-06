import shelve
import os

# name = input()
# surname = input()
# number = input()
# city = input()
# city = input()


def createhandbook():
    for i in range(100000):
        if os.path.exists(f"handbook{i + 1}.txt"):
            continue
        else:
            f1 = open(f'handbook{i + 1}.txt', 'w')
            f1.close()
            break

def deletehandbook():
    os.remove(input('Какой handbook удалить? >')+'.txt')

def openhandbook():
    listhandbooks = []
    for j in os.listdir():
        if j.startswith('handbook'):
            listhandbooks.append(j)
    file = input('Какой handbook открыть? >')+'.txt'
    open(file, 'r').read()


    def notehandbook(name, surname, number, city, email):
        file1 = open(file, 'w')
        for i in range(10000):
            if os.path.exists(f'id{i+1}:'):
                continue
            else:
                file1.write(f'id{i+1}:' + '\n')
                break
        file1.write('\t' + name + '\n')
        file1.write('\t' + surname + '\n')
        file1.write('\t' + number + '\n')
        file1.write('\t' + city + '\n')
        file1.write('\t' + email + '\n\n')
    notehandbook(input('Имя >'), input('Фамилия >'), input('Номер >'), input('Город >'), input('Email >'))


createhandbook()
openhandbook()

