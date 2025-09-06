#!/usr/bin/env python3
"""
Script4 - placeholder
Escribe `output/notes.txt` con una nota.
"""
import os


def main():
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'notes.txt'), 'w', encoding='utf-8') as f:
        f.write('Script4: nota de ejemplo')
    print('Script4: resultados en output/notes.txt')


if __name__ == '__main__':
    main()
