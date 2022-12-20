import matplotlib.pyplot as plt

# Список языков программирования
programmingLanguages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
# Список значений популярности языков соответственно
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# Цвета для сегментов круговой диаграммы
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# Построение круговой диаграммы с заданными параметрами
plt.pie(popularity, labels=programmingLanguages, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()
