from django.db import models


class TaskF(models.Model):

    title = models.CharField('Название', max_length=50)
    task_1 = models.FileField()

    def __str__(self):
        return self.title


class Test(models.Model):

    task = models.FileField()



# a - ...| b - !.. | c - ?.. | d - ! | e - ? | f - . | g - , | h - ; | i - :
# a - noun | b - verb | c - adjective | d - adverb | e - participle | f - gerunds |

class Table(models.Model):
    surname = models.CharField('фамилия', max_length=200)
    len_of_sentence = models.FloatField('Средняя длина предложения')
    len_of_words = models.FloatField('Средняя длина слова')
    num_of_prep_a = models.FloatField('Количество "..." :')
    num_of_prep_b = models.FloatField('Количество "!.." :')
    num_of_prep_c = models.FloatField('Количество "!" :')
    num_of_prep_d = models.FloatField('Количество "!" :')
    num_of_prep_e = models.FloatField('Количество "?" :')
    num_of_prep_f = models.FloatField('Количество "." :')
    num_of_prep_g = models.FloatField('Количество "," :')
    num_of_prep_h = models.FloatField('Количество ":" :')
    num_of_prep_i = models.FloatField('Количество ":" :')
    part_of_speech_a = models.FloatField('Количество существительных')
    part_of_speech_b = models.FloatField('Количество глаголов')
    part_of_speech_c = models.FloatField('Количество прлагательных')
    part_of_speech_d = models.FloatField('Количество наречий')
    part_of_speech_e = models.FloatField('Количество причастий')
    part_of_speech_f = models.FloatField('Количество деепричастий')


    def __str__(self):
        return self.surname

class TableAuthors(models.Model):
    surname = models.CharField('фамилия', max_length=200)
    len_of_sentence = models.FloatField('Средняя длина предложения')
    len_of_words = models.FloatField('Средняя длина слова')
    num_of_prep_a = models.FloatField('Среднее количество "..." :')
    num_of_prep_b = models.FloatField('Среднее количество "!.." :')
    num_of_prep_c = models.FloatField('Среднее количество "?.." :')
    num_of_prep_d = models.FloatField('Среднее количество "!" :')
    num_of_prep_e = models.FloatField('Среднее количество "?" :')
    num_of_prep_f = models.FloatField('Среднее количество "." :')
    num_of_prep_g = models.FloatField('Среднее количество "," :')
    num_of_prep_h = models.FloatField('Среднее количество ":" :')
    num_of_prep_i = models.FloatField('Среднее количество ":" :')
    part_of_speech_a = models.FloatField('Среднее количество существительных')
    part_of_speech_b = models.FloatField('Среднее количество глаголов')
    part_of_speech_c = models.FloatField('Среднее количество прлагательных')
    part_of_speech_d = models.FloatField('Среднее количество наречий')
    part_of_speech_e = models.FloatField('Среднее количество причастий')
    part_of_speech_f = models.FloatField('Среднее количество деепричастий')


    def __str__(self):
        return self.surname