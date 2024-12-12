import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('files/crime_data.csv')  # путь к файлу

# Преобразование столбца 'month' в формат даты
data['month'] = pd.to_datetime(data['month'])

# Установка стиля Seaborn
sns.set(style="whitegrid")

# Визуализация общего количества преступлений по месяцам
plt.figure(figsize=(14, 7))
sns.lineplot(data=data, x='month', y='Total_crimes', marker='o')
plt.title('Общее количество преступлений в России (2003-2020)')
plt.xlabel('Месяц')
plt.ylabel('Количество преступлений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Визуализация серьезных преступлений
plt.figure(figsize=(14, 7))
sns.lineplot(data=data, x='month', y='Serious', marker='o', color='red')
plt.title('Серьезные преступления в России (2003-2020)')
plt.xlabel('Месяц')
plt.ylabel('Количество серьезных преступлений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Визуализация различных типов преступлений
plt.figure(figsize=(14, 7))
sns.lineplot(data=data, x='month', y='Murder', marker='o', label='Убийства')
sns.lineplot(data=data, x='month', y='Rape', marker='o', label='Изнасилования')
sns.lineplot(data=data, x='month', y='Theft', marker='o', label='Кражи')
plt.title('Различные типы преступлений в России (2003-2020)')
plt.xlabel('Месяц')
plt.ylabel('Количество преступлений')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Скрипичный график

data['month'] = pd.to_datetime(data['month'])
data['year'] = data['month'].dt.year  # Замена x='month' на x='year'

plt.figure(figsize=(12, 6))
sns.violinplot(x='year', y='Total_crimes', data=data)
plt.title('Скрипичный график состояния преступности по годам')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Создание тепловой карты

# Преобразование столбца 'month' в datetime
data['month'] = pd.to_datetime(data['month'])
data['year'] = data['month'].dt.year  # Добавление столбца 'year'

# Группировка данных по годам и суммирование только числовых значений
data = data.groupby('year').sum(numeric_only=True)  # Используем numeric_only=True для суммирования только числовых столбцов

# Создание тепловой карты
plt.figure(figsize=(12, 8))
sns.heatmap(data, cmap='Reds', annot=True, fmt=".1f")

# Настройка заголовка и меток
plt.title('Тепловая карта состояния преступности в России (2003-2020)')
plt.xlabel('Тип преступления')
plt.ylabel('Год')

# Показать график
plt.show()

