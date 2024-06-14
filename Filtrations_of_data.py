import pandas as pd
from First_steps_with_data import students_performance
from First_steps_with_data import students_performance_with_names
import numpy as np

print('\n                 file: Filtrations_of_data')
print('\n        фильтрация данных')
print('\n отфильтруем gender по female с помощью iloc')
print(students_performance.loc[students_performance.gender == 'female', ['gender', 'writing score']].head())
print('\n создадим переменную для определения среднего по writing score')
mean_writing_score = students_performance['writing score'].mean()
print(mean_writing_score)
print('\n отберем значения по writing score, которые превышают среднее, с помощью loc')
print(students_performance.loc[students_performance['writing score'] > mean_writing_score].head())
print('\n отобрать только те наблюдения, у которых значение по переменной writing score >  среднего, '
      'а значение переменной gender == female')
querys = students_performance[(students_performance['writing score'] > mean_writing_score) & \
                              (students_performance.gender == 'female')].head()
print(querys)
print('\n переименуем названия колонок, у которых есть пробелы в названиях')
students_performance = students_performance \
    .rename(columns =
                     {'parental level of education': 'parental_level_of_education',
                      'test preparation course': 'test_preparation_course',
                      'math score': 'math_score',
                      'reading score': 'reading_score',
                      'writing score': 'writing_score'
                                    }
            )
print(students_performance.head())
print('\n вывести данные с помощью метода query(''), для которых writing_score > 74')
print(students_performance.query('writing_score > 74').head())
print('\n вывести данные для gender == "female" ')
print(students_performance.query('gender == "female"').head())
print('\n Создадим переменную, которая может менять свое значение')
writing_score_query = 95
print('\n значение изменяемой переменной', writing_score_query)
print('\n сравним значение с изменяемой переменной')
print(students_performance.query('writing_score > @writing_score_query').head())
print('\n имена колонок', list(students_performance))
print('\n имена колонок со словом score')
print([i for i in list(students_performance) if 'score' in i])
print('\n отфильтруем имена колонок со словом score с помощью метода filter')
print(students_performance.filter(like='score').head())
print('\n отфильтруем слова в строках, содержащие букву е')
print(students_performance_with_names.filter(like='e', axis=0).head())
