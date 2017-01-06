def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

print vector_add([1, 2], [3, 4])
