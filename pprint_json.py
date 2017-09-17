import json
import sys


def load_data(filepath):
    input_file = open(filepath, "r")
    raw_data = input_file.read()
    try:
        return json.loads(raw_data)
    except ValueError:
        print('JSON syntax error')
        raise SystemExit


def pretty_print_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True)


if __name__ == '__main__':
    filepath = sys.argv[1]
    print(pretty_print_json(load_data(filepath)))
