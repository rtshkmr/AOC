#!/usr/bin/env python3

#######################################################################################################################################################################################################################################################################################################
# --- Day 5: Supply Stacks ---                                                                                                                                                                                                                                                                        #
#                                                                                                                                                                                                                                                                                                     #
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.                                                     #
#                                                                                                                                                                                                                                                                                                     #
# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack. #
#                                                                                                                                                                                                                                                                                                     #
# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.                                                                     #
#                                                                                                                                                                                                                                                                                                     #
# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:                                                                                                                                                                 #
#                                                                                                                                                                                                                                                                                                     #
#     [D]                                                                                                                                                                                                                                                                                             #
# [N] [C]                                                                                                                                                                                                                                                                                             #
# [Z] [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# move 1 from 2 to 1                                                                                                                                                                                                                                                                                  #
# move 3 from 1 to 3                                                                                                                                                                                                                                                                                  #
# move 2 from 2 to 1                                                                                                                                                                                                                                                                                  #
# move 1 from 1 to 2                                                                                                                                                                                                                                                                                  #
#                                                                                                                                                                                                                                                                                                     #
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.                                       #
#                                                                                                                                                                                                                                                                                                     #
# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:                  #
#                                                                                                                                                                                                                                                                                                     #
# [D]                                                                                                                                                                                                                                                                                                 #
# [N] [C]                                                                                                                                                                                                                                                                                             #
# [Z] [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:                                                                                                                   #
#                                                                                                                                                                                                                                                                                                     #
#         [Z]                                                                                                                                                                                                                                                                                         #
#         [N]                                                                                                                                                                                                                                                                                         #
#     [C] [D]                                                                                                                                                                                                                                                                                         #
#     [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:                                                                                                                                                                  #
#                                                                                                                                                                                                                                                                                                     #
#         [Z]                                                                                                                                                                                                                                                                                         #
#         [N]                                                                                                                                                                                                                                                                                         #
# [M]     [D]                                                                                                                                                                                                                                                                                         #
# [C]     [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# Finally, one crate is moved from stack 1 to stack 2:                                                                                                                                                                                                                                                #
#                                                                                                                                                                                                                                                                                                     #
#         [Z]                                                                                                                                                                                                                                                                                         #
#         [N]                                                                                                                                                                                                                                                                                         #
#         [D]                                                                                                                                                                                                                                                                                         #
# [C] [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.                                                                #
#                                                                                                                                                                                                                                                                                                     #
# After the rearrangement procedure completes, what crate ends up on top of each stack?                                                                                                                                                                                                               #
#                                                                                                                                                                                                                                                                                                     #
# Your puzzle answer was TLNGFGMFN.                                                                                                                                                                                                                                                                   #
# --- Part Two ---                                                                                                                                                                                                                                                                                    #
#                                                                                                                                                                                                                                                                                                     #
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.                                                                                                                                                                              #
#                                                                                                                                                                                                                                                                                                     #
# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.                                                                                                                                                 #
#                                                                                                                                                                                                                                                                                                     #
# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.                                                                                                                       #
#                                                                                                                                                                                                                                                                                                     #
# Again considering the example above, the crates begin in the same configuration:                                                                                                                                                                                                                     #
#                                                                                                                                                                                                                                                                                                     #
#     [D]                                                                                                                                                                                                                                                                                             #
# [N] [C]                                                                                                                                                                                                                                                                                             #
# [Z] [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# Moving a single crate from stack 2 to stack 1 behaves the same as before:                                                                                                                                                                                                                           #
#                                                                                                                                                                                                                                                                                                     #
# [D]                                                                                                                                                                                                                                                                                                 #
# [N] [C]                                                                                                                                                                                                                                                                                             #
# [Z] [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:                                                                                                                                   #
#                                                                                                                                                                                                                                                                                                     #
#         [D]                                                                                                                                                                                                                                                                                         #
#         [N]                                                                                                                                                                                                                                                                                         #
#     [C] [Z]                                                                                                                                                                                                                                                                                         #
#     [M] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:                                                                                                                                                                                                            #
#                                                                                                                                                                                                                                                                                                     #
#         [D]                                                                                                                                                                                                                                                                                         #
#         [N]                                                                                                                                                                                                                                                                                         #
# [C]     [Z]                                                                                                                                                                                                                                                                                         #
# [M]     [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:                                                                                                                                                                                               #
#                                                                                                                                                                                                                                                                                                     #
#         [D]                                                                                                                                                                                                                                                                                         #
#         [N]                                                                                                                                                                                                                                                                                         #
#         [Z]                                                                                                                                                                                                                                                                                         #
# [M] [C] [P]                                                                                                                                                                                                                                                                                         #
#  1   2   3                                                                                                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.                                                                                                                                                                                                          #
#                                                                                                                                                                                                                                                                                                     #
# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?                                                    #
#                                                                                                                                                                                                                                                                                                     #
# Your puzzle answer was FGLQJCMBD.                                                                                                                                                                                                                                                                   #
#######################################################################################################################################################################################################################################################################################################

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

# NOTE: this only works because items are represented by a single letter:
NUM_CHARS_IN_ITEM_DISPLAY = 4 # [A]_ i.e. with a trailing space

def create_initial_stacks(num_stacks, container_lines):
    stacks = [[] for idx in range(num_stacks)]
    # keeps topmost elem at end of list:
    reversed_container_lines = reversed(container_lines)

    for line in reversed_container_lines:
        line_chars = [*line]
        for stack_idx in range(num_stacks):
            item_char_idx = (stack_idx * NUM_CHARS_IN_ITEM_DISPLAY) + 1

            if item_char_idx >= len(line_chars):
                break # prevents idx out of range errors

            item_char = line_chars[item_char_idx]
            if item_char.strip():
                stacks[stack_idx].append(item_char)

    return stacks

def get_rearrangement_instructions(input_lines, blank_line_idx):
    instructions = []

    for idx in range(blank_line_idx + 1, len(input_lines)):
        stringified_instruction = input_lines[idx].strip()
        triple = [elem for elem in stringified_instruction.split(" ")
                  if elem.isnumeric()]


        # qty, source, destination
        instructions.append(triple)

    return instructions

def organize_input_info(input_lines):
    # identifies number of columns:
    num_stacks = -1
    blank_line_idx = None
    rearrangement_instructions = []

    for idx, line in enumerate(input_lines):
        is_blank_line = not (line.strip())
        if is_blank_line:
            blank_line_idx = idx
            break

    column_label_line = input_lines[blank_line_idx - 1].strip()
    elems_in_stack_label = [elem for elem in column_label_line.split(" ") if elem]
    num_stacks = int(elems_in_stack_label[-1])

    initial_stacks = create_initial_stacks(num_stacks, input_lines[:blank_line_idx - 1])
    rearrangement_instructions = get_rearrangement_instructions(input_lines, blank_line_idx)

    return initial_stacks, rearrangement_instructions

def solve_part_1(input_lines):
    stacks, instructions = organize_input_info(input_lines)

    for quantity, source, destination in instructions:
        for i in range(int(quantity)):
            item = stacks[int(source) - 1].pop()
            stacks[int(destination) - 1].append(item)

    final_msg = "".join([stacks[stack_idx][-1] for stack_idx in  range(len(stacks))])

    return final_msg

def solve_part_2(input_lines):
    stacks, instructions = organize_input_info(input_lines)

    for quantity, source, destination in instructions:
        source_stack = stacks[int(source) - 1]
        payload = reversed([source_stack.pop() for i in range(int(quantity))])
        stacks[int(destination) - 1] += payload

    final_msg = "".join([stacks[stack_idx][-1] for stack_idx in  range(len(stacks))])

    return final_msg

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
