def move_zeros(array):
    new_array = [i for i in array if i != 0]
    new_array.extend([0]*array.count(0))

    return new_array
