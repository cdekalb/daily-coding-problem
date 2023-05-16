import argparse

def excluded_list_product(a):
    # a: A list of real numbers

    # Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    b = []

    for i in range(len(a)):
        removed_list = [a[x] for x,j in enumerate(a) if j != a[i]]
        result = 1
        for k in range(len(removed_list)):
            result = result * removed_list[k]
        b.append(result)
    return(b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Given an array of integers, return a new array such that each element at index i of the new array is the product \
        of all the numbers in the original array except the one at i.')
    parser.add_argument('-l','--list', nargs='+', type=int, help='Space-separated values of list', required=True)
    args = parser.parse_args()
    print(excluded_list_product(args.list))