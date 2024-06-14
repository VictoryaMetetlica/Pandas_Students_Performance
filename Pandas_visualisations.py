import pandas as pd
import matplotlib.pyplot as plt
from Grouping_of_data import students_performance


print('\n                 file: Pandas_visualisations')
print('\n     визуализация Pandas')
print('\n построим гистограмму распеределения math_score')
print(students_performance.math_score.hist())
    # метод  вызова графического отображения
plt.show()
print('\n построим скэттерплот - посмотрим корреляцию math_score/reading_score')
print(students_performance.plot.scatter(x='math_score', y='reading_score'))
plt.show()
