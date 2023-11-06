def sequence_matrix(arr):
    shift_right += 1
    shift_left -= 1
    column = 0
    length = len(arr)
    first_diag, second_diag = 0,0
    for i in range(length):
        first_diag += arr[column][shift_right]
        second_diag -= arr[column][shift_left]
        column += 1
    return abs(first_diag - second_diag)
sequence_matrix([[11,2,4],[4,5,6],[10,8,-12]])
