# https://www.hackerearth.com/problem/algorithm/graduating-5b72b1c7-bc102a51/


from itertools import product


def find_possible_attendance_combinations(n) -> list[str]:
    """
    Lets call the day she's absent as A. And the day she's present as P, find all possible ways to attend classes for
    'n' days.
    """
    all_ways = ["".join(attendance) for attendance in product(["A", "P"], repeat=n)]

    # If she’s absent for more than or equal to 4 consecutive days, we’ll reject those ways.
    rejected_ways = [way for way in all_ways if "AAAA" in way]
    possible_ways = list(set(all_ways) - set(rejected_ways))
    return possible_ways


def find_probability_of_missing(ways_to_attend) -> list[str]:
    # The probability that the student will miss the graduation ceremony is high if she's absent on the last day.
    chance_of_missing = [way for way in ways_to_attend if way[-1] == "A"]
    return chance_of_missing


possible_ways = find_possible_attendance_combinations(n=10)
probability = find_probability_of_missing(ways_to_attend=possible_ways)
print(f"{len(probability)}/{len(possible_ways)}")
