"""
# https://www.hackerearth.com/problem/algorithm/graduating-5b72b1c7-bc102a51/

Explanation:
For example, if you are not allowed to miss classes for two or more consecutive days,

Let's call the day she's absent as A. And the day she's present as P

Then all possible attendance combinations for n=3 days will be -
AAA, AAP, APA, APP, PAA, PAP, PPA, and PPP -> Now in combinations AAA, AAP, and PAA, she's absent for more than or
equal to two consecutive days. Thus, we'll reject these.

Required Combinations: APA, APP, PAP, PPA, and PPP -> 5 ways. Print 5

Now, in 2 combinations (APA & PPA) from 5 possible combinations, she'll not be able to attend the ceremony.

Thus, print Probability as 2/5
"""

from itertools import product


def find_possible_ways_to_attend(n) -> list[str]:
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
    # The student will miss the graduation ceremony if she's absent on the last day.
    chance_of_missing = [way for way in ways_to_attend if way[-1] == "A"]
    return chance_of_missing


possible_ways = find_possible_ways_to_attend(n=5)
probability = find_probability_of_missing(ways_to_attend=possible_ways)
print(f"{len(probability)}/{len(possible_ways)}")
