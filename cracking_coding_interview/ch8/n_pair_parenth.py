def pair_parenth(n):
    if n == 1:
        yield '()'
    else:
        for item in list(pair_parenth(n - 1)):
            item_list = list(item)
            item_list.insert(0, '(')
            item_list.insert(1, ')')
            yield ''.join(item_list)
            # reset
            del item_list[1]
            item_list.insert(2, ')')
            yield ''.join(item_list)


if __name__ == '__main__':
    print(list(pair_parenth(3)))
