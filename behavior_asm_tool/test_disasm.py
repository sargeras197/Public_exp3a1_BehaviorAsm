# test_disasm.py
# Тест для дизасемблювання exe-файлу

from disasm import disassemble_exe

if __name__ == "__main__":
    # Замість 'test.exe' вкажіть шлях до реального exe-файлу для тесту
    instructions = disassemble_exe('test.exe')
    for instr in instructions[:50]:  # Вивести перші 50 інструкцій
        print(f"0x{instr.address:x}: {instr.mnemonic} {instr.op_str}")
    print(f"[INFO] Всього інструкцій: {len(instructions)}")
