def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) == 0:
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item


if __name__ == '__main__':
    the_list = map(int, raw_input(
        "Please enter elements, separated by comma:").split(","))
    print(list(powerset(the_list)))
