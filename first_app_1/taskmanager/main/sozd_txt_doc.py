# -*- coding: utf8 -*-
list_of_aut = ['Тургенев', 'Булгаков', 'Гоголь', 'Некрасов', 'Толстой', 'Аксаков', 'Достоевский', 'Чехов', 'Горький', 'Паустовский']
for i in list_of_aut:
    for j in range(1, 11):
        file = open(f'C:/users/user/desktop/{i}/{i}{j}.txt', 'w')
        file.close()