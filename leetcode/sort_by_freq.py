import operator


def sort_by_freq(the_string):
    hash_table = {ord(i): 0 for i in the_string}

    for i in the_string:
        if hash_table.get(ord(i), None) is not None:
            hash_table[ord(i)] += 1

    hash_table_sorted = sorted(hash_table.items(), key=operator.itemgetter(1),
                               reverse=True)

    final_temp = [chr(i[0]) * i[1] for i in hash_table_sorted]

    return "".join(final_temp)


if __name__ == '__main__':
    print(sort_by_freq("bbbcattylelllester"))
