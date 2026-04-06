# test_cfg.py
# Тест для побудови графу переходів

from disasm import disassemble_exe
from cfg import build_cfg

if __name__ == "__main__":
    # Замість 'test.exe' вкажіть шлях до реального exe-файлу для тесту
    instructions = disassemble_exe('test.exe')
    G = build_cfg(instructions)
    print(f"[INFO] Вершин у графі: {G.number_of_nodes()}")
    print(f"[INFO] Ребер у графі: {G.number_of_edges()}")
    # Вивести перші 10 ребер
    for u, v in list(G.edges())[:10]:
        print(f"0x{u:x} -> 0x{v:x}")
