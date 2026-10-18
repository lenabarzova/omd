from collections import defaultdict


def do_ratings():
    reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

    product_reviews = defaultdict(list)
    for review in reviews:
        product = review['product'].lower()
        product_reviews[product].append(review['stars'])

    average_ratings = {}
    for product, stars in product_reviews.items():
        average_ratings[product] = sum(stars) / len(stars)
    print('средняя оценка каждого товара:', average_ratings)

    acceptable_products = []
    for product, stars in product_reviews.items():
        if len(stars) >= 2:
            acceptable_products.append(product)
    worst_product = min(acceptable_products, key=lambda product: average_ratings[product])
    print('худший товар по средней оценке:', worst_product)

    low_rating_count = 0
    for review in reviews:
        if review['stars'] in (1, 2):
            low_rating_count += 1
    print('отзывы на 1 или 2 звезды:', low_rating_count, 'шт')

    low_rating_share = low_rating_count / len(reviews) * 100
    print('доля отзывов на 1 или 2 звезды:', low_rating_share, '%')


if __name__ == '__main__':
    do_ratings()
