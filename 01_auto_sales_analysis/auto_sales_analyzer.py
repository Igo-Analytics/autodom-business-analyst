import pandas as pd
import numpy as np

print("🚗 Анализатор эффективности дилерских центров")

# Создаем демо-данные
dealers = [f'ДЦ_{i:02d}' for i in range(1, 6)]  # 5 ДЦ для примера
data = []

for dealer in dealers:
    for month in range(1, 4):  # 3 месяца
        data.append({
            'ДЦ': dealer,
            'Месяц': f'2024-{month:02d}',
            'Продажи': np.random.randint(20, 100),
            'Выручка': np.random.randint(5000000, 15000000)
        })

df = pd.DataFrame(data)
print(f"📊 Создано записей: {len(df)}")

# Анализ
total_revenue = df['Выручка'].sum()
avg_sales = df['Продажи'].mean()

print(f"💰 Общая выручка: {total_revenue:,} ₽")
print(f"📈 Средние продажи: {avg_sales:.0f} авто/мес")

# Топ ДЦ
top_dealers = df.groupby('ДЦ')['Выручка'].sum().sort_values(ascending=False)
print("\n🏆 Топ ДЦ по выручке:")
for dealer, revenue in top_dealers.items():
    print(f"   {dealer}: {revenue:,} ₽")
