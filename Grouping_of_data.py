import pandas as pd
import numpy as np
from Filtrations_of_data import students_performance


    # группировка данных
print('\n                 file: Grouping_of_data')
print('\n     группировка данных')
print('\n сгруппируем данные по двум группам female/male - чтобы сделать мультииндекс, убрать в groupby ..as_index = False')
mean_scores = students_performance.groupby(['gender', 'race/ethnicity'], as_index = False) \
      .aggregate({'math_score': 'mean', 'reading_score': 'mean'}) \
      .rename(columns=
                    {'math_score': 'mean_math_score', 'reading_score': 'mean_reading_score'})
print(mean_scores)
print(mean_scores.index)
print('\n Сколько уникальных оценок на пересечении двух групп по math_score')
print(students_performance.groupby(['gender', 'race/ethnicity']).math_score.nunique())
    # найдем топ 5 математиков девушек и юношей
print('\n отсортируем данные методом sort_values по убыванию и найдем топ 5 математиков девушек и юношей')
print(students_performance.sort_values(['gender', 'math_score'], ascending=False)\
      .groupby('gender').head())
print('\n успеваемость студентов - суммарный бал')
students_performance['total_score'] = sum([students_performance.math_score, students_performance.reading_score, students_performance.writing_score])
print(students_performance.head())
print('\n создадим колонку total_score_log')
students_performance = students_performance.assign(total_score_log = np.log(students_performance.total_score))
print(students_performance.head())
print('\n удалим колонку total_score')
print(students_performance.drop(['total_score', 'lunch'], axis=1).head())
