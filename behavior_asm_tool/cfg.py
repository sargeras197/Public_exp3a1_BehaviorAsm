# cfg.py
# Побудова графу переходів (Control Flow Graph) для дизасембльованого коду

import networkx as nx

# Інструкції, які можуть змінювати потік виконання
JUMP_MNEMONICS = {"jmp", "je", "jne", "jg", "jl", "jge", "jle", "ja", "jb", "jae", "jbe", "call", "ret"}


def build_cfg(instructions):
    G = nx.DiGraph()
    addr_to_idx = {instr.address: idx for idx, instr in enumerate(instructions)}
    for idx, instr in enumerate(instructions):
        G.add_node(instr.address, mnemonic=instr.mnemonic, op_str=instr.op_str)
        # Якщо це умовний/безумовний перехід або call
        if instr.mnemonic in JUMP_MNEMONICS:
            # call/jmp/je ...
            try:
                target = int(instr.op_str, 16)
                if target in addr_to_idx:
                    G.add_edge(instr.address, target)
            except Exception:
                pass
            # Якщо не ret/call/jmp — додати ребро на наступну інструкцію (fallthrough)
            if instr.mnemonic not in {"jmp", "ret", "call"}:
                if idx + 1 < len(instructions):
                    G.add_edge(instr.address, instructions[idx + 1].address)
        else:
            # Звичайна інструкція — перехід на наступну
            if idx + 1 < len(instructions):
                G.add_edge(instr.address, instructions[idx + 1].address)
    return G
