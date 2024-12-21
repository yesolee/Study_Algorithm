def solution(clothes):
    item_book = {}
    for item, ctg in clothes:
        item_book[ctg] = item_book.setdefault(ctg,0) + 1

    values = [i+1 for i in item_book.values()]
    result = 1
    for v in values:
        result *= v
    return result-1