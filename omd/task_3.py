def explore_orders(): 
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]

    total_returns = 0
    returned_buyers = []
    delivered_count = 0
    delivered_total = 0

    for order in orders:
        if order['status'] == 'returned':
            total_returns += order['amount']

            if order['buyer'] not in returned_buyers:
                returned_buyers.append(order['buyer'])

        elif order['status'] == 'delivered':
            delivered_count += 1

            delivered_total += order['amount']
    average_check = delivered_total / delivered_count

    print(total_returns)
    print(returned_buyers)
    print(delivered_count)
    print(average_check)

if __name__ == '__main__':
    explore_orders()
