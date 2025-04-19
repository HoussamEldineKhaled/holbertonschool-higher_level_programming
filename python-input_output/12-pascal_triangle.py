#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""

    if n <= 0:
        return []

    final_list = [[1]]

    for i in range(1, n):
        row_last = final_list[-1]

        new_row = [1]

        for j in range(1, i):
            new_row.append(row_last[j - 1] + row_last[j])
        new_row.append(1)
        final_list.append(new_row)
    return final_list
