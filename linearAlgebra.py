def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def dot(v, w):
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

print vector_add([1, 2], [3, 4])

print vector_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print dot([1, 2, 3], [4, 5, 6])

print dot([1, 2, 3], [1, 2, 3])
