# utils.py
# Допоміжні функції для аналізу PE-файлів та дизасемблювання

import pefile

def extract_imports(exe_path):
    pe = pefile.PE(exe_path)
    imports = {}
    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll = entry.dll.decode('utf-8')
            funcs = [imp.name.decode('utf-8') if imp.name else f'ordinal_{imp.ordinal}' for imp in entry.imports]
            imports[dll] = funcs
    return imports
