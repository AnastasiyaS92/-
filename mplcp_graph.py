import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk


data = pd.read_csv('files/crime_data.csv')  # путь файлу

# столбец 'month' в формате datetime
data['month'] = pd.to_datetime(data['month'])

# Установка стиля mplcyberpunk
plt.style.use('cyberpunk')

# Визуализация общего количества преступлений по месяцам
plt.figure(figsize=(14, 7))
plt.plot(data['month'], data['Total_crimes'], label='Total Crimes', color='cyan', linewidth=2)
plt.title('Общее количество преступлений в России (2003-2020)', fontsize=16)
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Количество преступлений', fontsize=14)
plt.legend()
plt.grid()
mplcyberpunk.add_glow_effects()
plt.show()

# Визуализация серьезных преступлений
plt.figure(figsize=(14, 7))
plt.plot(data['month'], data['Serious'], label='Серьезные преступления', color='magenta', linewidth=2)
plt.title('Серьезные преступления в России (2003-2020)', fontsize=16)
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Количество серьезных преступлений', fontsize=14)
plt.legend()
plt.grid()
mplcyberpunk.add_glow_effects()
plt.show()

# Визуализация убийств
plt.figure(figsize=(14, 7))
plt.plot(data['month'], data['Murder'], label='Убийства', color='red', linewidth=2)
plt.title('Количество убийств в России (2003-2020)', fontsize=16)
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Количество убийств', fontsize=14)
plt.legend()
plt.grid()
mplcyberpunk.add_glow_effects()
plt.show()




