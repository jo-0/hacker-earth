# https://www.hackerearth.com/problem/algorithm/graduating-5b72b1c7-bc102a51/


from itertools import product


def find_all_possible_attendance_combinations(n) -> list[str]:
    """
    Lets call the day she's absent as A. And the day she's present as P, find all possible ways to attend classes for
    'n' days.
    """
    return ["".join(attendance) for attendance in product(["A", "P"], repeat=n)]


find_all_possible_attendance_combinations(5)
