#!/usr/bin/env python3
"""
Validador de duplicados - script de ejemplo

Salidas: escribe un archivo `output/result.txt` con IDs duplicados (simulado).
"""
import os


def main():
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    result_path = os.path.join(out_dir, 'result.txt')
    # ejemplo: escribimos resultados simulados
    with open(result_path, 'w', encoding='utf-8') as f:
        f.write('id_1\nid_2\n')
    print(f'Resultados escritos en {result_path}')


if __name__ == '__main__':
    main()
