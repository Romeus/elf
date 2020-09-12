#!/usr/bin/env python3

import sys
from elftools.elf.elffile import ELFFile

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("You must provide this script with an elf binary file you want to examine")
        exit(1)

    print(f"Sections of the file {sys.argv[1]} that are not loaded into memory")

    with open(sys.argv[1], 'rb') as elffile:
        for section in ELFFile(elffile).iter_sections():
            if not section.header.sh_addr:
                print(section.name)

