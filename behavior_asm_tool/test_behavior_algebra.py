# test_behavior_algebra.py
# Тест для перетворення у алгебру поведінок

from disasm import disassemble_exe
from cfg import build_cfg
from behavior_algebra import extract_behavior_algebra, print_behavior_algebra

if __name__ == "__main__":
    # Замість 'test.exe' вкажіть шлях до реального exe-файлу для тесту
    instructions = disassemble_exe('test.exe')
    G = build_cfg(instructions)
    behaviors = extract_behavior_algebra(G, instructions)
    print_behavior_algebra(behaviors)
