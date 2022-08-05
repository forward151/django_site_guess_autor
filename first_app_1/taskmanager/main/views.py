import pymorphy2
import re
morph = pymorphy2.MorphAnalyzer()

from django.shortcuts import render, redirect
from .models import TaskF, Table, TableAuthors, Test
from .forms import TaskFormF, TableForm, TableAuthorsForm, TestForm


def main_page(request):
    return render(request, 'main/main_page.html')


def answer(request):
    return render(request, 'main/Answer.html')


def page_input(request):
    return render(request, 'main/page_input.html')


def input_data_file(request):
    list_prep = ['...', '!..', '?..', '!', '?', '.', ',', ';', ':']
    error = ''
    if request.method == 'POST':
        form = TaskFormF(request.POST, request.FILES)
        if form.is_valid():
            sn = form.cleaned_data.get('title')
            form.save()
            file = form.cleaned_data.get('task_1')
            str_text = ''
            for line in file:
                str_text = str_text + line.decode('Windows-1251')  # "str_text" will be of 'str' type
            now = num_of_words(str_text=str_text)
            los = round(len_of_sentence(str_text=str_text, list_prep=list_prep), 2)
            low = round(len_of_words(str_text=str_text, list_prep=list_prep), 2)
            nop = num_of_prep(str_text=str_text, list_prep=list_prep)
            pos = part_of_speech(str_text=str_text, list_prep=list_prep)
            print(f'Количество слов в тексте {now}')
            print(f'Среднее количество слов в предложении {los}')
            print(f'Средняя длина слова в тексте: {low}')
            print(f'Количество различных знаков препинания:\n{nop}')
            print(f'Количество различных частей речи:\n{pos}')
            t1 = Table.objects.create(surname=str(sn), len_of_words=low, len_of_sentence=los,
                                      num_of_prep_a=nop['...'], num_of_prep_b=nop['!..'], num_of_prep_c=nop['?..'],
                                      num_of_prep_d=nop['!'], num_of_prep_e=nop['?'], num_of_prep_f=nop['.'],
                                      num_of_prep_g=nop[','], num_of_prep_h=nop[';'], num_of_prep_i=nop[':'],
                                      part_of_speech_a=pos['noun'], part_of_speech_b=pos['verb'],
                                      part_of_speech_c=pos['adjective'], part_of_speech_d=pos['adverb'],
                                      part_of_speech_e=pos['participle'], part_of_speech_f=pos['gerunds'])
            t1.save()
            try:
                task = TableAuthors.objects.get(surname=str(sn))
                print('Автор существует')
                num = len(list(Table.objects.order_by('-id')))
                task.len_of_words = (task.len_of_words * num + los) / (num + 1)
                task.len_of_sentence = (task.len_of_sentence * num + los) / (num + 1)
                task.num_of_prep_a = (task.num_of_prep_a * num + los) / (num + 1)
                task.num_of_prep_b = (task.num_of_prep_b * num + los) / (num + 1)
                task.num_of_prep_c = (task.num_of_prep_c * num + los) / (num + 1)
                task.num_of_prep_d = (task.num_of_prep_d * num + los) / (num + 1)
                task.num_of_prep_e = (task.num_of_prep_e * num + los) / (num + 1)
                task.num_of_prep_f = (task.num_of_prep_f * num + los) / (num + 1)
                task.num_of_prep_g = (task.num_of_prep_g * num + los) / (num + 1)
                task.num_of_prep_h = (task.num_of_prep_h * num + los) / (num + 1)
                task.num_of_prep_i = (task.num_of_prep_i * num + los) / (num + 1)
                task.part_of_speech_a = (task.part_of_speech_a * num + los) / (num + 1)
                task.part_of_speech_b = (task.part_of_speech_b * num + los) / (num + 1)
                task.part_of_speech_c = (task.part_of_speech_c * num + los) / (num + 1)
                task.part_of_speech_d = (task.part_of_speech_d * num + los) / (num + 1)
                task.part_of_speech_e = (task.part_of_speech_e * num + los) / (num + 1)
                task.part_of_speech_f = (task.part_of_speech_f * num + los) / (num + 1)
            except BaseException:
                print('Автор не существует')
                t2 = TableAuthors.objects.create(surname=str(sn), len_of_words=low, len_of_sentence=los,
                                          num_of_prep_a=nop['...'], num_of_prep_b=nop['!..'], num_of_prep_c=nop['?..'],
                                          num_of_prep_d=nop['!'], num_of_prep_e=nop['?'], num_of_prep_f=nop['.'],
                                          num_of_prep_g=nop[','], num_of_prep_h=nop[';'], num_of_prep_i=nop[':'],
                                          part_of_speech_a=pos['noun'], part_of_speech_b=pos['verb'],
                                          part_of_speech_c=pos['adjective'], part_of_speech_d=pos['adverb'],
                                          part_of_speech_e=pos['participle'], part_of_speech_f=pos['gerunds'])
                t2.save()

            return render(request, 'main/page_input_ok.html')
        else:
            error = 'Некорректная форма'
    form = TaskFormF()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/input_data_file.html', context)


def input_test(request):
    list_prep = ['...', '!..', '?..', '!', '?', '.', ',', ';', ':']
    error = ''
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('task')
            str_text = ''
            for line in file:
                str_text = str_text + line.decode('Windows-1251')  # "str_text" will be of 'str' type
            now = num_of_words(str_text=str_text)
            los = round(len_of_sentence(str_text=str_text, list_prep=list_prep), 2)
            low = round(len_of_words(str_text=str_text, list_prep=list_prep), 2)
            nop_a = num_of_prep(str_text=str_text, list_prep=list_prep)['...']
            nop_b = num_of_prep(str_text=str_text, list_prep=list_prep)['!..']
            nop_c = num_of_prep(str_text=str_text, list_prep=list_prep)['?..']
            nop_d = num_of_prep(str_text=str_text, list_prep=list_prep)['!']
            nop_e = num_of_prep(str_text=str_text, list_prep=list_prep)['?']
            nop_f = num_of_prep(str_text=str_text, list_prep=list_prep)['.']
            nop_g = num_of_prep(str_text=str_text, list_prep=list_prep)[',']
            nop_h = num_of_prep(str_text=str_text, list_prep=list_prep)[';']
            nop_i = num_of_prep(str_text=str_text, list_prep=list_prep)[':']
            pos_a = part_of_speech(str_text=str_text, list_prep=list_prep)['noun']
            pos_b = part_of_speech(str_text=str_text, list_prep=list_prep)['verb']
            pos_c = part_of_speech(str_text=str_text, list_prep=list_prep)['adjective']
            pos_d = part_of_speech(str_text=str_text, list_prep=list_prep)['adverb']
            pos_e = part_of_speech(str_text=str_text, list_prep=list_prep)['participle']
            pos_f = part_of_speech(str_text=str_text, list_prep=list_prep)['gerunds']
            print(f'Среднее количество слов в предложении {len_of_sentence(str_text=str_text, list_prep=list_prep)}')
            print(f'Средняя длина слова в тексте: {len_of_words(str_text=str_text, list_prep=list_prep)}')
            print(f'Количество различных знаков препинания:\n{num_of_prep(str_text=str_text, list_prep=list_prep)}')
            print(f'Количество различных частей речи:\n{part_of_speech(str_text=str_text, list_prep=list_prep)}')
            list_los = []
            list_low = []
            list_nop_a = []
            list_nop_b = []
            list_nop_c = []
            list_nop_d = []
            list_nop_e = []
            list_nop_f = []
            list_nop_g = []
            list_nop_h = []
            list_nop_i = []
            list_pos_a = []
            list_pos_b = []
            list_pos_c = []
            list_pos_d = []
            list_pos_e = []
            list_pos_f = []
            list_of_authors = list(TableAuthors.objects.all())
            for obj in TableAuthors.objects.order_by('-id'):
                list_los.append(obj.len_of_sentence)
                list_low.append(obj.len_of_words)
                list_nop_a.append(obj.num_of_prep_a)
                list_nop_b.append(obj.num_of_prep_b)
                list_nop_c.append(obj.num_of_prep_c)
                list_nop_d.append(obj.num_of_prep_d)
                list_nop_e.append(obj.num_of_prep_e)
                list_nop_f.append(obj.num_of_prep_f)
                list_nop_g.append(obj.num_of_prep_g)
                list_nop_h.append(obj.num_of_prep_h)
                list_nop_i.append(obj.num_of_prep_i)
                list_pos_a.append(obj.part_of_speech_a)
                list_pos_b.append(obj.part_of_speech_b)
                list_pos_c.append(obj.part_of_speech_c)
                list_pos_d.append(obj.part_of_speech_d)
                list_pos_e.append(obj.part_of_speech_e)
                list_pos_f.append(obj.part_of_speech_f)
            x = 10000
            for i in range(len(list_los)):
                if abs(list_los[i] - los) < x:
                    x = abs(list_los[i] - los)
                    ind_los_i = i
            x = 10000

            for i in range(len(list_low)):
                if abs(list_low[i] - low) < x:
                    x = abs(list_low[i] - low)
                    ind_low_i = i
            x = 10000

            for i in range(len(list_nop_a)):
                if abs(list_nop_a[i] - nop_a) < x:
                    x = abs(list_nop_a[i] - nop_a)
                    ind_nop_a_i = i
            x = 10000

            for i in range(len(list_nop_b)):
                if abs(list_nop_b[i] - nop_b) < x:
                    x = abs(list_nop_b[i] - nop_b)
                    ind_nop_b_i = i
            x = 10000

            for i in range(len(list_nop_c)):
                if abs(list_nop_c[i] - nop_c) < x:
                    x = abs(list_nop_c[i] - nop_c)
                    ind_nop_c_i = i
            x = 10000

            for i in range(len(list_nop_d)):
                if abs(list_nop_d[i] - nop_d) < x:
                    x = abs(list_nop_d[i] - nop_d)
                    ind_nop_d_i = i
            x = 10000

            for i in range(len(list_nop_e)):
                if abs(list_nop_e[i] - nop_e) < x:
                    x = abs(list_nop_e[i] - nop_e)
                    ind_nop_e_i = i
            x = 10000

            for i in range(len(list_nop_f)):
                if abs(list_nop_f[i] - nop_f) < x:
                    x = abs(list_nop_f[i] - nop_f)
                    ind_nop_f_i = i
            x = 10000

            for i in range(len(list_nop_g)):
                if abs(list_nop_g[i] - nop_g) < x:
                    x = abs(list_nop_g[i] - nop_g)
                    ind_nop_g_i = i
            x = 10000

            for i in range(len(list_nop_h)):
                if abs(list_nop_h[i] - nop_h) < x:
                    x = abs(list_nop_h[i] - nop_h)
                    ind_nop_h_i = i
            x = 10000

            for i in range(len(list_nop_i)):
                if abs(list_nop_i[i] - nop_i) < x:
                    x = abs(list_nop_i[i] - nop_i)
                    ind_nop_i_i = i
            x = 10000

            for i in range(len(list_pos_a)):
                if abs(list_pos_a[i] - pos_a) < x:
                    x = abs(list_pos_a[i] - pos_a)
                    ind_pos_a_i = i
            x = 10000

            for i in range(len(list_pos_b)):
                if abs(list_pos_b[i] - pos_b) < x:
                    x = abs(list_pos_b[i] - pos_b)
                    ind_pos_b_i = i
            x = 10000

            for i in range(len(list_pos_c)):
                if abs(list_pos_c[i] - pos_c) < x:
                    x = abs(list_pos_c[i] - pos_c)
                    ind_pos_c_i = i
            x = 10000

            for i in range(len(list_pos_d)):
                if abs(list_pos_d[i] - pos_d) < x:
                    x = abs(list_pos_d[i] - pos_d)
                    ind_pos_d_i = i
            x = 10000

            for i in range(len(list_pos_e)):
                if abs(list_pos_e[i] - pos_e) < x:
                    x = abs(list_pos_e[i] - pos_e)
                    ind_pos_e_i = i
            x = 10000

            for i in range(len(list_pos_f)):
                if abs(list_pos_f[i] - pos_f) < x:
                    x = abs(list_pos_f[i] - pos_f)
                    ind_pos_f_i = i
            x = 10000
            print(ind_los_i, ind_low_i, ind_nop_a_i, ind_nop_b_i, ind_nop_c_i, ind_nop_d_i, ind_nop_e_i, ind_nop_f_i, ind_nop_g_i, ind_nop_h_i, ind_nop_i_i, ind_pos_a_i, ind_pos_b_i, ind_pos_c_i, ind_pos_d_i, ind_pos_e_i, ind_pos_f_i)
            print(list_of_authors)
            list_end = [ind_los_i, ind_low_i, ind_nop_a_i, ind_nop_b_i, ind_nop_c_i, ind_nop_d_i, ind_nop_e_i, ind_nop_f_i, ind_nop_g_i, ind_nop_h_i, ind_nop_i_i, ind_pos_a_i, ind_pos_b_i, ind_pos_c_i, ind_pos_d_i, ind_pos_e_i, ind_pos_f_i]
            n = 0
            for i in range(len(list_end)):
                if list_end.count(list_end[i]) > n:
                    n = list_end.count((list_end[i]))
                    i_out = list_end[i]

            print(list_of_authors[i_out].surname)
            answer = list_of_authors[i_out].surname
            return render(request, 'main/page_input_ok.html', {'answer': answer})

        else:
            error = 'Некорректная форма'
    form = TestForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/input_test.html', context)


def materials(request):
    return render(request, 'main/materials.html')


def about(request):
    return render(request, 'main/about.html')


def other(request):
    return render(request, 'main/other.html')


def input_ok(request):
    return render(request, 'main/page_input_ok.html')


def page_database(request):
    tasks = list(Table.objects.order_by('-id'))
    print(tasks)
    return render(request, 'main/page_database.html', {'title': 'Главная страница', 'tasks': tasks})




#  Функции для получения данных по тексту
def num_of_words(str_text):
    list_of_words = str_text.split(' ')
    return len(list_of_words)



def len_of_words(str_text, list_prep):
    list_alphabet = []
    for k in str_text:
        list_alphabet.append(k)
    for k in range(len(list_alphabet)):
        if list_alphabet[k] in list_prep:
            list_alphabet[k] = ''
    text_without_prep = ''.join(list_alphabet)
    list_words = text_without_prep.split(' ')
    num_list_words = len(list_words)
    for k in range(len(list_words)):
        list_words[k] = len(list_words[k])
    sum_list_words = sum(list_words)
    sr_len_of_words = sum_list_words / num_list_words
    return sr_len_of_words


def num_of_sentences(str_text):
    split_regex = re.compile(r'[.|!|...|?]')
    sentences = list(filter(lambda t: t, [t.strip() for t in split_regex.split(str_text)]))
    num_of_sentences = len(sentences)
    return num_of_sentences



def len_of_sentence(str_text, list_prep):
    split_regex = re.compile(r'[.|!|...|?]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(str_text)])
    list_of_numwords = []
    for n in sentences:
        list_of_alphabet = []
        for i in n:
            list_of_alphabet.append(i)
        for i in list_of_alphabet:
            if i in list_prep:
                list_of_alphabet.remove(i)
        words = ''.join(list_of_alphabet)
        list_of_words = words.split(' ')
        list_of_numwords.append(len(list_of_words))
    return sum(list_of_numwords) / len(list_of_numwords)


def del_prep(str_text, list_prep):
    list_alphabet = []
    for k in str_text:
        list_alphabet.append(k)
    for k in range(len(list_alphabet)):
        if list_alphabet[k] in list_prep:
            list_alphabet[k] = ''
    text_without_prep = ''.join(list_alphabet)
    return text_without_prep


def num_of_prep(str_text, list_prep):
    dict_of_prep = {}
    nos = num_of_sentences(str_text=str_text)
    for i in list_prep:
        dict_of_prep[i] = str_text.count(i) / nos
        while str_text.find(i) != -1:
            x = str_text.index(i)
            str_text = str_text[0:x] + str_text[x + len(i)::]
    return dict_of_prep


def part_of_speech(str_text, list_prep):
    dict_of_parts = {'noun': 0, 'verb': 0, 'adjective': 0, 'adverb': 0, 'participle': 0, 'gerunds': 0}
    text = del_prep(str_text=str_text, list_prep=list_prep)
    nof = num_of_words(str_text=str_text)
    list_of_text = text.split(' ')
    for i in list_of_text:
        a = morph.parse(i)[0]
        if a.tag.POS == 'NOUN':
            dict_of_parts['noun'] += 1
        elif a.tag.POS == 'ADJF' or a.tag.POS == 'ADJS':
            dict_of_parts['adjective'] += 1
        elif a.tag.POS == 'VERB' or a.tag.POS == 'INFN':
            dict_of_parts['verb'] += 1
        elif a.tag.POS == 'ADVB':
            dict_of_parts['adverb'] += 1
        elif a.tag.POS == 'PRTF' or a.tag.POS == 'PRTS':
            dict_of_parts['participle'] += 1
        elif a.tag.POS == 'GRND':
            dict_of_parts['gerunds'] += 1
    for i in dict_of_parts:
        dict_of_parts[i] = round(dict_of_parts[i] / nof, 2)
    return dict_of_parts
