#!/usr/bin/env python3

import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.segments import Segment

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("You must provide this script with an elf binary file you want to examine")
        exit(1)

    print(f"Segments of the file {sys.argv[1]} which size on disk and in memory differs")

    with open(sys.argv[1], 'rb') as elffile:
        for segment in ELFFile(elffile).iter_segments():
            if segment.header.p_filesz != segment.header.p_memsz:
                seg_head = segment.header
                print(f"Type: {seg_head.p_type}\nOffset: {hex(seg_head.p_offset)}\nSize in file:{hex(seg_head.p_filesz)}\nSize in memory:{hex(seg_head.p_memsz)}")
