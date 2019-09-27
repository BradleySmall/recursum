"""
Using recursion to sum a list
"""


LENGTH = 500
my_list = range(LENGTH)


def rsum(idx, the_list):
    if idx == len(the_list):
        return 0
    return the_list[idx] + rsum(idx+1, the_list)


def r_sub_sum(the_list):
    if not the_list:
        return 0
    return the_list[0] + r_sub_sum(the_list[1:])


def main():
    idx = 0
    print(rsum(idx, my_list))
    print(r_sub_sum(my_list))
    print(sum(my_list))


if __name__ == "__main__":
    main()
