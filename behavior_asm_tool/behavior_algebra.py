# behavior_algebra.py
# Перетворення control flow graph у алгебру поведінок (Behavior Algebra)

def extract_behavior_algebra(cfg, instructions):
    """
    Створює простий опис поведінки на основі графу переходів та дизасембльованих інструкцій.
    Повертає список блоків-поведінок (функцій/гілок) у вигляді псевдокоду.
    """
    addr_to_instr = {instr.address: instr for instr in instructions}
    behaviors = []
    visited = set()
    for node in cfg.nodes:
        if node in visited:
            continue
        block = []
        current = node
        while True:
            instr = addr_to_instr.get(current)
            if not instr:
                break
            block.append(f"0x{instr.address:x}: {instr.mnemonic} {instr.op_str}")
            visited.add(current)
            # Якщо є тільки один наступник — йдемо далі
            succ = list(cfg.successors(current))
            if len(succ) == 1 and succ[0] not in visited:
                current = succ[0]
            else:
                break
        if block:
            behaviors.append(block)
    return behaviors

def print_behavior_algebra(behaviors):
    for i, block in enumerate(behaviors):
        print(f"Behavior Block {i+1}:")
        for line in block:
            print(f"  {line}")
        print()
