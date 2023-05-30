import argparse

def find_num_ways(stair_length, num_steps):
    # Initialize vector to store num_ways for each stair_length
    num_ways = [0] * (stair_length + 1)
    num_ways[0] = 1

    for num_stairs in range(1, stair_length + 1):
        for step_size in num_steps:
            if num_stairs >= step_size:
                num_ways[num_stairs] += num_ways[num_stairs - step_size]

    return num_ways[stair_length]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Given a staircase with N steps, write a function that returns the number of unique ways you can climb the staircase \
        from a list of predetermined step sizes. The order of the steps matters.')
    parser.add_argument('-i', '--integer', nargs=1, type=int, help='Integer length of the staircase', required=True)
    parser.add_argument('-l','--list', nargs='+', type=int, help='Space-separated list of step sizes', required=True)
    args = parser.parse_args()
    print(find_num_ways(args.integer[0], args.list))