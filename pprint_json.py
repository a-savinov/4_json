import json
import sys


def check_json_data(input_json):
    try:
        return json.loads(input_json)
    except ValueError:
        print('JSON syntax error')
        raise SystemExit


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_data = check_json_data(input_file.read())
    return raw_data


def pretty_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print(pretty_json(load_data(filepath)))
    else:
        print('No JSON data to prettify')
