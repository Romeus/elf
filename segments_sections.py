#!/usr/bin/env python3

import sys
from elftools.elf.elffile import ELFFile

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("You must provide this script with an elf binary file you want to examine")
        exit(1)

    print(f"Mapping between segments and sections in the file {sys.argv[1]}")

    elffile = ELFFile(open(sys.argv[1], 'rb'))

    segments = list()
    for segment_idx in range(elffile.num_segments()):
        segments.insert(segment_idx, dict())
        segments[segment_idx]['segment'] = elffile.get_segment(segment_idx)
        segments[segment_idx]['sections'] = list()
       
    for section_idx in range(elffile.num_sections()):
        section = elffile.get_section(section_idx)
        for segment in segments:
            if segment['segment'].section_in_segment(section):
                segment['sections'].append(section)
                
    for segment in segments:
        seg_head = segment['segment'].header
        print("Segment:")
        print(f"Type: {seg_head.p_type}\nOffset: {hex(seg_head.p_offset)}\nVirtual address: {hex(seg_head.p_vaddr)}\nPhysical address: {(seg_head.p_paddr)}\Size in file:{hex(seg_head.p_filesz)}\nSize in memory:{hex(seg_head.p_memsz)}\n")

        if segment['sections']:
            print("Segment's sections:")
            print([(section.name, hex(section['sh_addr'])) for section in segment['sections']], sep=', ', end='\n')
        else:
            print('Segment contains no sections')

        print('\n--------------------------------------------------------------------------------')
