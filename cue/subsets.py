# Congratulations.  You have reached the final level.

#   For the final task, you must find all subsets of an array
#   where the largest number is the sum of the remaining numbers.
#   For example, for an input of:
#
#           (1, 2, 3, 4, 6)
#
#               the subsets would be
#
#                 1 + 2 = 3
#                 1 + 3 = 4
#                 2 + 4 = 6
#                 1 + 2 + 3 = 6

#    Here is the list of numbers you should run your code on.
#    The password is the number of subsets.  In the above case the
#    answer would be 4.

number_list = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]

def subsets(set):
    sub_subsets = []
    if not set:
        sub_subsets.append([])
    else:
        for sub_subset in subsets(set[:-1]):
            sub_subsets.append(sub_subset)
            sub_subsets.append(sub_subset + [set[-1]])

    return sub_subsets

number_subsets = subsets(number_list)

# Filter predicate
def largest_is_sum_remaining(subset):
    if not subset:
        return False
    largest = max(subset)
    max_idx = subset.index(largest)
    remaining = subset[:max_idx] + subset[max_idx+1:]
    return sum(remaining) == largest

print filter(largest_is_sum_remaining, number_subsets)
print len(filter(largest_is_sum_remaining, number_subsets))
