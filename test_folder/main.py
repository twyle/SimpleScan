#!/usr/bin/python3
from task import generate_two_numbers, add_two_numbers

if __name__ == '__main__':
    int_one, int_two = generate_two_numbers()
    int_sum = add_two_numbers(int_one, int_two)
    print(int_sum)