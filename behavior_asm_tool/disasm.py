# disasm.py
# Дизасемблювання коду з exe-файлу

import pefile
from capstone import *


def get_code_sections(exe_path):
    pe = pefile.PE(exe_path)
    code_sections = []
    for section in pe.sections:
        if b'CODE' in section.Name or section.Characteristics & 0x20:
            code_sections.append(section)
    return code_sections


def disassemble_section(section, base_addr):
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    code = section.get_data()
    addr = base_addr + section.VirtualAddress
    instructions = list(md.disasm(code, addr))
    return instructions


def disassemble_exe(exe_path):
    pe = pefile.PE(exe_path)
    code_sections = get_code_sections(exe_path)
    all_instructions = []
    for section in code_sections:
        instrs = disassemble_section(section, pe.OPTIONAL_HEADER.ImageBase)
        all_instructions.extend(instrs)
    return all_instructions
