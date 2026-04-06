# test_utils.py
# Тест для функції extract_imports

from utils import extract_imports

if __name__ == "__main__":
    # Замість 'test.exe' вкажіть шлях до реального exe-файлу для тесту
    imports = extract_imports('test.exe')
    for dll, funcs in imports.items():
        print(f"{dll}:")
        for func in funcs:
            print(f"  {func}")
