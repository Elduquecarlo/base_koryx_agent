#!/usr/bin/env python3
"""
Script3 - ejemplo simple
Escribe `output/result.json` con un ejemplo JSON.
"""
import os
import json


def main():
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    data = {'status': 'ok', 'items': 3}
    with open(os.path.join(out_dir, 'result.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('Script3: resultados en output/result.json')


if __name__ == '__main__':
    main()
