def transformer_tuples(List, fn):
    result = []

    for i in List:
        transformation = map(fn, i)

        result.append(list(tuple(transformation) ))

    print(result)

transformer_tuples([(1,2,5), (2,4,5)], lambda x: x * 2)