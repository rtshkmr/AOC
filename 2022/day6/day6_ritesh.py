#!/usr/bin/env python3

##########################################################################################################################################################################################################################################################################################################################################################
# --- Day 6: Tuning Trouble ---                                                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                                                                        #
# The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the star fruit grove.                                                                                                                                                                                                                        #
#                                                                                                                                                                                                                                                                                                                                                        #
# As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy features, but the most important one to set up right now is the communication system.                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                                                                        #
# However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.                                                                                                               #
#                                                                                                                                                                                                                                                                                                                                                        #
# As if inspired by comedic timing, the device emits a few colorful sparks.                                                                                                                                                                                                                                                                              #
#                                                                                                                                                                                                                                                                                                                                                        #
# To be able to communicate with the Elves, the device needs to lock on to their signal. The signal is a series of seemingly-random characters that the device receives one at a time.                                                                                                                                                                   #
#                                                                                                                                                                                                                                                                                                                                                        #
# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.                                                                               #
#                                                                                                                                                                                                                                                                                                                                                        #
# The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker. #
#                                                                                                                                                                                                                                                                                                                                                        #
# For example, suppose you receive the following datastream buffer:                                                                                                                                                                                                                                                                                      #
#                                                                                                                                                                                                                                                                                                                                                        #
# mjqjpqmgbljsphdztnvjfqwrcgsmlb                                                                                                                                                                                                                                                                                                                         #
#                                                                                                                                                                                                                                                                                                                                                        #
# After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.                                               #
#                                                                                                                                                                                                                                                                                                                                                        #
# The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.                                       #
#                                                                                                                                                                                                                                                                                                                                                        #
# Here are a few more examples:                                                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                                                                        #
#     bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5                                                                                                                                                                                                                                                                                       #
#     nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6                                                                                                                                                                                                                                                                                       #
#     nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10                                                                                                                                                                                                                                                                                 #
#     zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11                                                                                                                                                                                                                                                                                  #
#                                                                                                                                                                                                                                                                                                                                                        #
# How many characters need to be processed before the first start-of-packet marker is detected?                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                                                                        #
# Your puzzle answer was 1896.                                                                                                                                                                                                                                                                                                                           #
# --- Part Two ---                                                                                                                                                                                                                                                                                                                                       #
#                                                                                                                                                                                                                                                                                                                                                        #
# Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.                                                                                                                                                                                                            #
#                                                                                                                                                                                                                                                                                                                                                        #
# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.                                                                                                                                                                                                                           #
#                                                                                                                                                                                                                                                                                                                                                        #
# Here are the first positions of start-of-message markers for all of the above examples:                                                                                                                                                                                                                                                                  #
#                                                                                                                                                                                                                                                                                                                                                        #
#     mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19                                                                                                                                                                                                                                                                                    #
#     bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23                                                                                                                                                                                                                                                                                      #
#     nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23                                                                                                                                                                                                                                                                                      #
#     nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29                                                                                                                                                                                                                                                                                 #
#     zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26                                                                                                                                                                                                                                                                                  #
#                                                                                                                                                                                                                                                                                                                                                        #
# How many characters need to be processed before the first start-of-message marker is detected?                                                                                                                                                                                                                                                         #
#                                                                                                                                                                                                                                                                                                                                                        #
# Your puzzle answer was 3452.                                                                                                                                                                                                                                                                                                                           #
##########################################################################################################################################################################################################################################################################################################################################################

WINDOW_SIZE_PACKET = 4 # 4 chars
WINDOW_SIZE_MSG = 14 # 14 chars

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

def check_duplicates_in_window(window_contents):
    """
    Returns true if there are duplicates in the window's contents.
    """
    window = {}

    for content in window_contents:
        if (window.get(content)):
            return True
        else:
            window[content] = 'Exists'

    return False

def solve_part_1(input):
    input_chars = [*input]

    for idx in range(len(input_chars)):
        marker_idx = idx + WINDOW_SIZE_PACKET
        if (marker_idx) > len(input_chars):
            break

        window_contents = input_chars[idx:marker_idx]
        has_duplicates = check_duplicates_in_window(window_contents)

        if not has_duplicates:
            return marker_idx

    return None

def solve_part_2(input):
    input_chars = [*input]

    for idx in range(len(input_chars)):
        marker_idx = idx + WINDOW_SIZE_MSG
        if (marker_idx) > len(input_chars):
            break

        window_contents = input_chars[idx:marker_idx]
        has_duplicates = check_duplicates_in_window(window_contents)

        if not has_duplicates:
            return marker_idx

    return None

def main():

    # tests inputs:
    input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # ans part 1: 7 part 2: 19
    input = "bvwbjplbgvbhsrlpgdmjqwftvncz" # ans: 5 part 2: 23
    input = "nppdvjthqldpwncqszvftbrmjlhg" # ans: 6 part 2: 23
    input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # ans: 10 part 2: 29
    input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # ans: 11 part 2: 26

    input = parse_input('./input.in')


    if not input:
        msg = "Why even bother!?"
        print(msg)

        return




    part_1_solution = solve_part_1(input)
    part_2_solution = solve_part_2(input)

    print(f"part 1 solution: {part_1_solution} ")
    print(f"part 2 solution: {part_2_solution} ")

    return

if __name__ == "__main__":
    main()
