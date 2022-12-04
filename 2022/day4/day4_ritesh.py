#!/usr/bin/env python3

##############################################################################################################################################################################################################################################################################################################################################################################################################################
# --- Day 4: Camp Cleanup ---                                                                                                                                                                                                                                                                                                                                                                                                #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.                                                                                                                                                                 #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).                                                                                                                   #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# For example, consider the following list of section assignment pairs:                                                                                                                                                                                                                                                                                                                                                      #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# 2-4,6-8                                                                                                                                                                                                                                                                                                                                                                                                                    #
# 2-3,4-5                                                                                                                                                                                                                                                                                                                                                                                                                    #
# 5-7,7-9                                                                                                                                                                                                                                                                                                                                                                                                                    #
# 2-8,3-7                                                                                                                                                                                                                                                                                                                                                                                                                    #
# 6-6,4-6                                                                                                                                                                                                                                                                                                                                                                                                                    #
# 2-6,4-8                                                                                                                                                                                                                                                                                                                                                                                                                    #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# For the first few pairs, this list means:                                                                                                                                                                                                                                                                                                                                                                                  #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
#     Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).                                                                                                                                                                                                                                                     #
#     The Elves in the second pair were each assigned two sections.                                                                                                                                                                                                                                                                                                                                                          #
#     The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.                                                                                                                                                                                                                                                                                 #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:                                                                                                                                                                                                                                     #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# .234.....  2-4                                                                                                                                                                                                                                                                                                                                                                                                             #
# .....678.  6-8                                                                                                                                                                                                                                                                                                                                                                                                             #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# .23......  2-3                                                                                                                                                                                                                                                                                                                                                                                                             #
# ...45....  4-5                                                                                                                                                                                                                                                                                                                                                                                                             #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# ....567..  5-7                                                                                                                                                                                                                                                                                                                                                                                                             #
# ......789  7-9                                                                                                                                                                                                                                                                                                                                                                                                             #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# .2345678.  2-8                                                                                                                                                                                                                                                                                                                                                                                                             #
# ..34567..  3-7                                                                                                                                                                                                                                                                                                                                                                                                             #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# .....6...  6-6                                                                                                                                                                                                                                                                                                                                                                                                             #
# ...456...  4-6                                                                                                                                                                                                                                                                                                                                                                                                             #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# .23456...  2-6                                                                                                                                                                                                                                                                                                                                                                                                             #
# ...45678.  4-8                                                                                                                                                                                                                                                                                                                                                                                                             #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs. #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# In how many assignment pairs does one range fully contain the other?                                                                                                                                                                                                                                                                                                                                                       #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# Your puzzle answer was 459.                                                                                                                                                                                                                                                                                                                                                                                                #
# --- Part Two ---                                                                                                                                                                                                                                                                                                                                                                                                           #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.                                                                                                                                                                                                                                                                         #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:                                                                                                                                                                                                                                                           #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
#     5-7,7-9 overlaps in a single section, 7.                                                                                                                                                                                                                                                                                                                                                                                #
#     2-8,3-7 overlaps all of the sections 3 through 7.                                                                                                                                                                                                                                                                                                                                                                      #
#     6-6,4-6 overlaps in a single section, 6.                                                                                                                                                                                                                                                                                                                                                                                #
#     2-6,4-8 overlaps in sections 4, 5, and 6.                                                                                                                                                                                                                                                                                                                                                                                 #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# So, in this example, the number of overlapping assignment pairs is 4.                                                                                                                                                                                                                                                                                                                                                       #
#                                                                                                                                                                                                                                                                                                                                                                                                                            #
# In how many assignment pairs do the ranges overlap?                                                                                                                                                                                                                                                                                                                                                                        #
##############################################################################################################################################################################################################################################################################################################################################################################################################################


def parse_input(url, readlines=False):
    """
    Parses input file via provided url.
    Returns lines read as a list if readlines is True.
    """

    try:
        with open(url, 'r') as file:
            content = file.readlines() if readlines else file.read()

            return content

    except Exception as e:
        msg = f"Error reading input file: {e}"
        print(msg)

    return None

def check_full_range_overlap(first_range, second_range):
    first_range = [int(e) for e in first_range.split('-')]
    second_range = [int (e) for e in second_range.split('-')]

    is_range_superset = lambda range_a, range_b: ((range_a[0] <= range_b[0]) \
                                             and (range_a[1] >= range_b[1]))

    if (is_range_superset(first_range, second_range)
        or is_range_superset(second_range, first_range)):
        return True

    return False

def solve_part_1(input_lines):

    counter = 0

    for pair in input_lines:
        first_range, second_range = pair.strip().split(",")
        is_overlap = check_full_range_overlap(first_range, second_range)
        counter += 1 if is_overlap else 0

    return counter

def check_if_no_overlaps_in_ranges(first_range, second_range):
    first_range = [int(e) for e in first_range.split('-')]
    second_range = [int (e) for e in second_range.split('-')]

    is_first_range_left_of_second_range = first_range[0] < second_range[0] and first_range[1] < second_range[0]
    is_first_range_right_of_second_range = second_range[0] < first_range[0] and second_range[1] < first_range[0]

    if (is_first_range_left_of_second_range or is_first_range_right_of_second_range):
        return True

    return False

def solve_part_2(input_lines):

    count_no_overlaps = 0

    for pair in input_lines:
        first_range, second_range = pair.strip().split(",")
        is_not_overlapping_at_all = check_if_no_overlaps_in_ranges(first_range, second_range)
        count_no_overlaps += 1 if is_not_overlapping_at_all else 0

    num_overlaps = len(input_lines) - count_no_overlaps

    return num_overlaps

def main():
    input_lines = parse_input('./input.in', readlines=True)

    if not input_lines:
        msg = "Why even bother!?"
        print(msg)

        return

    part_1_solution = solve_part_1(input_lines)
    part_2_solution = solve_part_2(input_lines)

    print(f"part 1 solution: {part_1_solution} ")
    print(f"part 2 solution: {part_2_solution} ")

    return

if __name__ == "__main__":
    main()
