def merge_sort(input_array):
    length = len(input_array)
    # print('length={} array={}'.format(length, input_array))
    if length > 2:
        return_value = []
        half = int(length/2)
        left = merge_sort(input_array[:half])
        right = merge_sort(input_array[half:])
        # print('length={} half={} left={} right={} input_array={}'.format(length, half, left, right, input_array))
        left_index = 0
        right_index = 0
        while left_index < len(left) or right_index < len(right):
            if left_index >= len(left):
                return_value = return_value + right[right_index:]
                break
            elif right_index >= len(right):
                return_value = return_value + left[left_index:]
                break
            elif left[left_index] < right[right_index]:
                return_value.append(left[left_index])
                left_index += 1
            else:
                return_value.append(right[right_index])
                right_index += 1
        return return_value
    else:
        for i in range(len(input_array)):
            if len(input_array) is 0 or len(input_array) is 1:
                # print('returning {}'.format(input_array))
                return input_array
            elif len(input_array) == 2:
                if input_array[0] > input_array[1]:
                    # print('returning {}'.format([input_array[1], input_array[0]]))
                    return [input_array[1], input_array[0]]
                else:
                    # print('returning {}'.format(input_array))
                    return input_array
            else:
                raise ValueError('Array too large input_array={}'.format(input_array))
