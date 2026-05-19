""" Лабораторная работа 3, вариант 4 """
# Задание 1

from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import seaborn as sns

# 1. Загрузка данных
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
# Переименовываем целевые значения для лучшей легенды (0: злокачественная, 1: доброкачественная)
df['class_name'] = df['target'].map({0: 'malignant', 1: 'benign'})

# 2. Построение графика
plt.figure(figsize=(10, 6))

# Используем seaborn для удобного раскрашивания по классам
sns.scatterplot(data=df, x='mean radius', y='mean texture', hue='class_name', palette='deep', s=100)

plt.title("Рак молочной железы: Средний радиус vs Средняя текстура")
plt.xlabel("Средний радиус")
plt.ylabel("Средняя текстура")
plt.legend(title='Диагноз')
plt.grid(True, alpha=0.3)

plt.show()


# Задание 2


# 1. Загрузка данных
data = sm.datasets.grunfeld.load_pandas().data

# 2. Выбор 3 произвольных фирм
# В наборе данных обычно есть столбец 'firm'. Выберем 3 уникальные фирмы.
# Например, возьмём первые 3 уникальные фирмы, найденные в данных.
unique_firms = data['firm'].unique()
selected_firms = unique_firms[:3] 

# Фильтруем данные для этих 3 фирм
df_filtered = data[data['firm'].isin(selected_firms)]

# 3. Построение графиков

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=False)
variables = ['invest', 'value', 'capital']

for ax, variable in zip(axes, variables):
    # x='year', y=variable, hue='firm' создаёт линии для каждой фирмы
    sns.lineplot(data=df_filtered, x='year', y=variable, hue='firm', ax=ax, marker='o')
    ax.set_title(f"Динамика {variable.capitalize()}")
    ax.set_xlabel("Год")
    ax.set_ylabel(variable.capitalize())
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.suptitle("Данные Grunfeld: Динамика для 3 выбранных фирм", fontsize=16, y=1.05)
plt.show()