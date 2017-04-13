def merge_sort(input_array):
    if len(input_array) is 0 or len(input_array) is 1:
        return input_array
    else:
        half = int(len(input_array)/2)
        left = merge_sort(input_array[:half])
        right = merge_sort(input_array[half:])

        return_value = []
        left_index = 0
        right_index = 0
        while True:
            if left_index >= len(left):
                return return_value + right[right_index:]
            elif right_index >= len(right):
                return return_value + left[left_index:]
            else:
                if left[left_index] < right[right_index]:
                    return_value.append(left[left_index])
                    left_index += 1
                else:
                    return_value.append(right[right_index])
                    right_index += 1
