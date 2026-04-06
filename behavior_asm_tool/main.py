# Behavior Algebra Extractor
# Головний скрипт для аналізу exe-файлів


import sys
from utils import extract_imports
from disasm import disassemble_exe
from cfg import build_cfg
from behavior_algebra import extract_behavior_algebra, print_behavior_algebra

def menu():
    print("Виберіть дію:")
    print("1. Витягти імпортовані функції (DLL)")
    print("2. Дизасемблювати код")
    print("3. Побудувати граф переходів (CFG)")
    print("4. Перетворити у алгебру поведінок")
    print("0. Вийти")


def ask_save_to_file(default_name, content_lines):
    ans = input("Зберегти результат у файл? (y/n): ").strip().lower()
    if ans == 'y':
        fname = input(f"Введіть ім'я файлу (Enter для {default_name}): ").strip()
        if not fname:
            fname = default_name
        with open(fname, 'w', encoding='utf-8') as f:
            for line in content_lines:
                f.write(line + '\n')
        print(f"[OK] Збережено у {fname}")
    else:
        for line in content_lines:
            print(line)

def main():
    exe_path = input("Введіть шлях до exe-файлу: ").strip()
    instructions = None
    cfg = None
    while True:
        menu()
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            imports = extract_imports(exe_path)
            lines = ["[Імпортовані функції]:"]
            for dll, funcs in imports.items():
                lines.append(f"{dll}:")
                for func in funcs:
                    lines.append(f"  {func}")
            ask_save_to_file("imports.txt", lines)
        elif choice == "2":
            instructions = disassemble_exe(exe_path)
            lines = [f"[INFO] Дизасембльовано інструкцій: {len(instructions)}"]
            for instr in instructions[:50]:
                lines.append(f"0x{instr.address:x}: {instr.mnemonic} {instr.op_str}")
            ask_save_to_file("disasm.txt", lines)
        elif choice == "3":
            if instructions is None:
                instructions = disassemble_exe(exe_path)
            cfg = build_cfg(instructions)
            lines = [f"[INFO] Вершин у графі: {cfg.number_of_nodes()}", f"[INFO] Ребер у графі: {cfg.number_of_edges()}"]
            for u, v in list(cfg.edges())[:10]:
                lines.append(f"0x{u:x} -> 0x{v:x}")
            ask_save_to_file("cfg.txt", lines)
        elif choice == "4":
            if instructions is None:
                instructions = disassemble_exe(exe_path)
            if cfg is None:
                cfg = build_cfg(instructions)
            behaviors = extract_behavior_algebra(cfg, instructions)
            lines = []
            for i, block in enumerate(behaviors):
                lines.append(f"Behavior Block {i+1}:")
                for line in block:
                    lines.append(f"  {line}")
                lines.append("")
            ask_save_to_file("behavior_algebra.txt", lines)
        elif choice == "0":
            print("Вихід.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
