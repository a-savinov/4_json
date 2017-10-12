import json
import sys


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_json_data = json.load(input_file)
    return raw_json_data


def pretty_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            json_data = load_data(filepath)
        except ValueError as e:
            print(e)
            raise SystemExit
        else:
            print(pretty_json(load_data(filepath)))
    else:
        print('No JSON data to prettify')
