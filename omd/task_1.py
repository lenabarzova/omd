def storage_check():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print(moscow.intersection(kazan))
    print(moscow.difference(kazan))
    print(kazan.difference(moscow))
    print(len(moscow.union(kazan)))


if __name__ == '__main__':
    storage_check()
