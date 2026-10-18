from collections import Counter

def explore_searches():
    
    queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]
    query_counts = Counter(queries)
    print(len(queries))
    print(query_counts)
    print(query_counts.most_common(1))
    print(round(query_counts.most_common(1)[0][1] / len(queries) * 100, 2))
    for query, count in query_counts.items():
        if count == 1:
            print(query)
    
if __name__ == '__main__':
    explore_searches()
