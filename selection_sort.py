def selection_sort(a_list):
    for sort_before in range(len(a_list) - 1, 0, -1):  # sort_before is the index below which sorting needs to be done

        max_index_pos = 0  # we assume that the first element is the max

        for location in range(1, sort_before + 1): # location is the index of all elements on and before sort_before
                                                   # i.e. index of elements that needs to be sorted

            if a_list[location] > a_list[max_index_pos]:  # checks if current number is greater than the previous max number
                max_index_pos = location

        # exchange the greatest number of the unsorted part as the first element of the sorted part
        a_list[sort_before], a_list[max_index_pos] = a_list[max_index_pos], a_list[sort_before]
