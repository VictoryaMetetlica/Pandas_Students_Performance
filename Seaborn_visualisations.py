import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Grouping_of_data import students_performance

print('\n                 file: Seaborn_visualisations')
print('\n     визуализация Seaborn')
print('\n построим скэттерплот lmplot - посмотрим корреляцию math_score/reading_score')
print(sns.lmplot(x='math_score', y='reading_score', data=students_performance))
plt.show()
print('\n добавим группировку по gender')
print(sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance))
plt.show()
print('\n уберем апроксимирующие регрессионные прямые')
print(sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance, fit_reg=False))
plt.show()
print('\n     введем переменную ах для даленейшей обработки графика')
ax = sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance, fit_reg=False)
print('\n     переименуем названия осей')
ax.set_xlabels('math score')
ax.set_ylabels('reading scores')
plt.show()
print('\n Используем функцию тепловой карты (диаграмма кореляции) math_score/reading_score Seaborn с аргументами:'
        'cmap="viridis" цветовая схема')
g = sns.heatmap([students_performance.math_score.iloc[0:10], students_performance.reading_score.iloc[0:10]], cmap='viridis')
print('\n и установим надпись по оси x наверху тепловой карты')
g.xaxis.set_ticks_position('top')
plt.show()
print('\n рассмотрим распределение данных по математике с помощью kdeplot')
print(sns.kdeplot(students_performance.math_score))
plt.show()
print('\n используем скрипичный график (violin плот) math_score')
print(sns.violinplot(students_performance.math_score))