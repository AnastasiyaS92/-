import pandas as pd
import plotly.express as px
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('files/crime_data.csv')

# Преобразование колонки 'month' в формат datetime
data['month'] = pd.to_datetime(data['month'])

# Линейный график общего количества преступлений по месяцам
fig1 = px.line(data, x='month', y='Total_crimes', title='Общее количество преступлений в России (2003-2020)',
               labels={'Total_crimes': 'Количество преступлений'},
               template='plotly_white')
fig1.show()

# Бар-график по видам преступлений
crime_types = ['Serious', 'Huge_damage', 'Ecological', 'Terrorism', 'Extremism',
               'Murder', 'Harm_to_health', 'Rape', 'Theft', 'Vehicle_theft',
               'Fraud_scam', 'Hooligan', 'Drugs', 'Weapons']

# Создание графиков для каждого типа преступления
for crime_type in crime_types:
    fig = px.bar(data, x='month', y=crime_type, title=f'Количество {crime_type} преступлений в России (2003-2020)',
                 labels={crime_type: f'Количество {crime_type}'},
                 color=crime_type, # Добавлено для разных цветов
                 template='plotly_white')
    fig.show()

# Матрица рассеяния
scatter_matrix(data[['Total_crimes', 'Serious', 'Huge_damage', 'Ecological', 'Terrorism']], figsize=(12, 12),
               diagonal='kde')
plt.suptitle('Матрица рассеяния преступности')
plt.show()

# Суммирование данных по типам преступлений
crime_types = data[['Serious', 'Huge_damage', 'Ecological', 'Terrorism', 'Extremism',
                    'Murder', 'Harm_to_health', 'Rape', 'Theft', 'Vehicle_theft',
                    'Fraud_scam', 'Hooligan', 'Drugs', 'Weapons']].sum()

# Создание круговой диаграммы
plt.figure(figsize=(8, 8))
plt.pie(crime_types, labels=crime_types.index, autopct='%1.1f%%', startangle=140)
plt.title('Распределение типов преступлений в России (2003-2020)')
plt.axis('equal')  # Чтобы круг был кругом
plt.show()


