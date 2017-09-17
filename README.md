# Prettify JSON

This script outputs json data from a file in an easy-to-read format

# Quickstart


Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

```
Output example

```#!bash
$ python pprint_json.py raw.json
[
    {
        "Cells": {
            "Address": "...",
            "AdmArea": "...",
...
...
            "geoData": {
                "coordinates": [
                    37.58803599964753,
                    55.89020100016689
                ],
                "type": "Point"
            },
            "global_id": 14937274
        },
        "Id": "a16c8154-09d8-4207-8e13-cb8db654e95c",
        "Number": 3
    }
]

Process finished with exit code 0
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
