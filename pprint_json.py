# -*- coding: utf-8 -*-

import json
import sys


def load_data(filepath):
    f = open(filepath, "r")
    raw_data = f.read()
    try:
        return json.loads(raw_data)
    except ValueError:
        print('JSON syntax error')
        raise SystemExit


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


if __name__ == '__main__':
    filepath = sys.argv[1]
    print(pretty_print_json(load_data(filepath)))
