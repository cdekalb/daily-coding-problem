# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

import argparse

def sum_exists(num_list, k):
    # num_list: A list of integers
    # k: An integer

    # Find if there exist two elements of num_list that sum to k

    num_set = set()
    for i in range(len(num_list)):
        if((k - num_list[i]) in num_set):
            return True
        num_set.add(num_list[i])
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find if there exist two elements of num_list that sum to k.')
    parser.add_argument('-l','--list', nargs='+', type=int, help='<Required> Set flag', required=True)
    parser.add_argument('-i', '--integer', nargs=1, type=int, help='<Required> Set flag', required=True)
    args = parser.parse_args()
    print(sum_exists(args.list, args.integer[0]))