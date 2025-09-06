#!/usr/bin/env python3
"""
Script2 - ejemplo de script auxiliar
Genera `output/log.txt` con un mensaje de ejemplo.
"""
import os


def main():
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'log.txt'), 'w', encoding='utf-8') as f:
        f.write('Script2 ejecutado correctamente\n')
    print('Script2: resultados en output/log.txt')


if __name__ == '__main__':
    main()
