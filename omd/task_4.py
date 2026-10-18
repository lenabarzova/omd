def shop_finances():
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]

    total_revenue = 0
    for day in days:
        total_revenue += day['revenue']
    print(total_revenue)

    best_day = max(days, key=lambda day: day['revenue'])
    print('максимальная выручка', best_day['day'], ':', best_day['revenue'])

    for day in days:
        average_revenue = day['revenue'] / day['orders']
        print('средняя выручка на один заказ:', day['day'], average_revenue)
        
    for day in days:
        if day['returns'] / day['orders'] > 0.2:
            print('возвратов больше 20% заказов:', day['day'])


if __name__ == '__main__':
    shop_finances()
