#!/usr/bin/env python3

    ##############################################################################################################################################################################################################################################################################################################################################################################
    # --- Day 7: No Space Left On Device ---                                                                                                                                                                                                                                                                                                                                     #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?                                                                                                                                                                         #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # The device the Elves gave you has problems with more than just its communication system. You try to run a system update:                                                                                                                                                                                                                                                   #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # $ system-update --please --pretty-please-with-sugar-on-top                                                                                                                                                                                                                                                                                                                 #
    # Error: No space left on device                                                                                                                                                                                                                                                                                                                                             #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Perhaps you can delete some files to make space for the update?                                                                                                                                                                                                                                                                                                              #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:                                                                                                                                                                                                                                            #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # $ cd /                                                                                                                                                                                                                                                                                                                                                                     #
    # $ ls                                                                                                                                                                                                                                                                                                                                                                       #
    # dir a                                                                                                                                                                                                                                                                                                                                                                      #
    # 14848514 b.txt                                                                                                                                                                                                                                                                                                                                                             #
    # 8504156 c.dat                                                                                                                                                                                                                                                                                                                                                              #
    # dir d                                                                                                                                                                                                                                                                                                                                                                      #
    # $ cd a                                                                                                                                                                                                                                                                                                                                                                     #
    # $ ls                                                                                                                                                                                                                                                                                                                                                                       #
    # dir e                                                                                                                                                                                                                                                                                                                                                                      #
    # 29116 f                                                                                                                                                                                                                                                                                                                                                                    #
    # 2557 g                                                                                                                                                                                                                                                                                                                                                                     #
    # 62596 h.lst                                                                                                                                                                                                                                                                                                                                                                #
    # $ cd e                                                                                                                                                                                                                                                                                                                                                                     #
    # $ ls                                                                                                                                                                                                                                                                                                                                                                       #
    # 584 i                                                                                                                                                                                                                                                                                                                                                                      #
    # $ cd ..                                                                                                                                                                                                                                                                                                                                                                    #
    # $ cd ..                                                                                                                                                                                                                                                                                                                                                                    #
    # $ cd d                                                                                                                                                                                                                                                                                                                                                                     #
    # $ ls                                                                                                                                                                                                                                                                                                                                                                       #
    # 4060174 j                                                                                                                                                                                                                                                                                                                                                                  #
    # 8033020 d.log                                                                                                                                                                                                                                                                                                                                                              #
    # 5626152 d.ext                                                                                                                                                                                                                                                                                                                                                              #
    # 7214296 k                                                                                                                                                                                                                                                                                                                                                                  #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.                                                                            #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:                                                                                                                                                                                                                                                       #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    #     cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:                                                                                                                                                                                                                                     #
    #         cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.                                                                                                                                                                                                                                           #
    #         cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.                                                                                                                                                                                                                            #
    #         cd / switches the current directory to the outermost directory, /.                                                                                                                                                                                                                                                                                                 #
    #     ls means list. It prints out all of the files and directories immediately contained by the current directory:                                                                                                                                                                                                                                                          #
    #         123 abc means that the current directory contains a file named abc with size 123.                                                                                                                                                                                                                                                                                  #
    #         dir xyz means that the current directory contains a directory named xyz.                                                                                                                                                                                                                                                                                           #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Given the commands and output in the example above, you can determine that the filesystem looks visually like this:                                                                                                                                                                                                                                                        #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # - / (dir)                                                                                                                                                                                                                                                                                                                                                                  #
    # - a (dir)                                                                                                                                                                                                                                                                                                                                                                  #
    #     - e (dir)                                                                                                                                                                                                                                                                                                                                                              #
    #     - i (file, size=584)                                                                                                                                                                                                                                                                                                                                                   #
    #     - f (file, size=29116)                                                                                                                                                                                                                                                                                                                                                 #
    #     - g (file, size=2557)                                                                                                                                                                                                                                                                                                                                                  #
    #     - h.lst (file, size=62596)                                                                                                                                                                                                                                                                                                                                             #
    # - b.txt (file, size=14848514)                                                                                                                                                                                                                                                                                                                                              #
    # - c.dat (file, size=8504156)                                                                                                                                                                                                                                                                                                                                               #
    # - d (dir)                                                                                                                                                                                                                                                                                                                                                                  #
    #     - j (file, size=4060174)                                                                                                                                                                                                                                                                                                                                               #
    #     - d.log (file, size=8033020)                                                                                                                                                                                                                                                                                                                                           #
    #     - d.ext (file, size=5626152)                                                                                                                                                                                                                                                                                                                                           #
    #     - k (file, size=7214296)                                                                                                                                                                                                                                                                                                                                               #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.                                                                                                                                                                                                     #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)      #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # The total sizes of the directories above can be found as follows:                                                                                                                                                                                                                                                                                                          #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    #     The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.                                                                                                                                                                                                                                                         #
    #     The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).                                                                                                                                                                                          #
    #     Directory d has total size 24933642.                                                                                                                                                                                                                                                                                                                                   #
    #     As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.                                                                                                                                                                                                                                                      #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)                                                                       #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?                                                                                                                                                                                                                                                  #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Your puzzle answer was 1243729.                                                                                                                                                                                                                                                                                                                                            #
    # --- Part Two ---                                                                                                                                                                                                                                                                                                                                                           #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Now, you're ready to choose a directory to delete.                                                                                                                                                                                                                                                                                                                         #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.                                                                                                                                                 #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run. #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # To achieve this, you have the following options:                                                                                                                                                                                                                                                                                                                           #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    #     Delete directory e, which would increase unused space by 584.                                                                                                                                                                                                                                                                                                          #
    #     Delete directory a, which would increase unused space by 94853.                                                                                                                                                                                                                                                                                                        #
    #     Delete directory d, which would increase unused space by 24933642.                                                                                                                                                                                                                                                                                                     #
    #     Delete directory /, which would increase unused space by 48381165.                                                                                                                                                                                                                                                                                                     #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.                                                                                                                                                        #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?                                                                                                                                                                                                                    #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Your puzzle answer was 4443914.                                                                                                                                                                                                                                                                                                                                            #
    #                                                                                                                                                                                                                                                                                                                                                                            #
    # Both parts of this puzzle are complete! They provide two gold stars: **                                                                                                                                                                                                                                                                                                    #
    ##############################################################################################################################################################################################################################################################################################################################################################################

import sys

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

def create_tree(input_lines):
    """
    Creates a basic tree representing the file-system.
    All the directory sizes in the tree will be finalized when this function
    returns its value (a tree).
    """
    file_tree = Tree()

    ls_buffer = []

    for idx, line in enumerate(input_lines):
        line = line.strip()
        split_line = line.split(' ')

        is_command = split_line[0] == '$'
        if is_command:
            if (len(ls_buffer) > 0):
                file_tree.dump_ls_buffer(ls_buffer)
                ls_buffer = []

            if split_line[1] == 'cd':
                file_tree.change_dir(split_line[2])
        else:
            ls_buffer.append(split_line)

            if (idx == len(input_lines) - 1):
                file_tree.dump_ls_buffer(ls_buffer)
                ls_buffer = []
                break

    file_tree.root_node.update_size()

    return file_tree

def get_dirs_below_limit(root_dir, limit):

    dirs = []
    if (root_dir.size <= limit):
        dirs.append(root_dir)

    for child in root_dir.children:
        if child.type != 'dir':
            continue
        dirs += get_dirs_below_limit(child, limit)

    return dirs


def solve_part_1(tree):
    dirs_below_limit = get_dirs_below_limit(tree.root_node, 100000)
    print(f"Dirs below limit:\n {dirs_below_limit}")

    sum_of_sizes = sum([dir.size for dir in dirs_below_limit])

    return sum_of_sizes

def get_deletable_dirs(root_dir, current_unused_space):
    MIN_UNUSED_SPACE = 30000000
    dirs = []
    if ((root_dir.size + current_unused_space) >= MIN_UNUSED_SPACE):
        dirs.append(root_dir)

    for child in root_dir.children:
        if child.type != 'dir':
            continue
        dirs += get_deletable_dirs(child, current_unused_space)

    return dirs

def solve_part_2(tree):
    DISK_SIZE = 70000000

    current_unused_space = DISK_SIZE - tree.root_node.size
    candidates = get_deletable_dirs(tree.root_node, current_unused_space)

    smallest_size = int(sys.maxsize)
    smallest_candidate = None
    print("Candidates: ", candidates)

    for candidate in candidates:
        if candidate.size < smallest_size:
            smallest_size = candidate.size
            smallest_candidate = candidate

    return smallest_candidate

def main():
    input = parse_input('./input.in', True)
    print(f"Input has {len(input or [])} lines")

    if not input:
        msg = "Why even bother!?"
        print(msg)

        return

    filesystem_tree = create_tree(input)

    part_1_solution = solve_part_1(filesystem_tree)
    part_2_solution = solve_part_2(filesystem_tree)

    part_1_msg = part_1_solution or "Yet to solve part 1"
    part_2_msg = part_2_solution or "Yet to solve part 2"
    print(f"part 1 solution: {part_1_msg} ")
    print(f"part 2 solution: {part_2_msg} ")

    return

#############################################################################
# Outlined below is a basic tree and node class for use in  this puzzle example: #
#############################################################################
class Tree:

    def __init__(self):
        self.root_node = Node(name='/', type='dir')
        self.pointer = self.root_node

    def __repr__(self):
        tree_string = f"{self.root_node.get_dir_node_string()}"
        return tree_string

    def dump_ls_buffer(self, ls_buffer):
        for item in ls_buffer:
            if not self.pointer:
                print(f'⛔️ error: {self.pointer} should not be none...')
                return

            self.pointer.add_item(item)

    def change_dir(self, arg):

        if arg == '/':
            self.pointer = self.root_node

        elif arg == '..':
            self.pointer = self.pointer.parent_node

        else:
            current_children = self.pointer.children
            for child in current_children:
                if child.type == 'dir' and child.name == arg:
                    self.pointer = child
                    return
            print("⛔️ Error: trying to step into a dir that doesn't exist")

class Node:

    def __init__(self, name=None, parent_node=None, type='file', size=None):
        self.name = name
        self.type = type
        self.size = size
        self.parent_node = parent_node

        if self.type == 'dir':
            self.children = []
        else:
            self.children = None

    def __repr__(self):
        res = f"{hex(id(self))} {self.name} {self.type} size: {self.size}"

        return res

    def get_dir_node_string(self, level=1):

        if self.type != 'dir':
            return self.__repr__()

        padding = "".join([f'.' for x in range(level)])

        res = f'{padding} {self}\n'

        for child in self.children:
            if child.type == 'file':
                res += f"{padding + '.'} {child}\n"
            if child.type == 'dir':
                res += child.get_dir_node_string(level + 1)

        res += '\n'

        return res

    def update_size(self):
        if self.type == 'dir':
            size = 0
            for child in self.children:
                child.update_size()
                size += child.size
            self.size = size

    def add_item(self, item):

        if (self.type != 'dir'):
            print(f"⛔️ Error: trying to add item to a non-directory node")

            return

        size = None
        if item[0] == 'dir':
            type = item[0]
            name = item[1]
        else:
            type = 'file'
            size = int(item[0])
            name = item[1]

        new_node = Node(name=name, type=type, size=size, parent_node=self)
        self.children.append(new_node)

if __name__ == "__main__":
    main()
