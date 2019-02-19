import os
import tempfile
import argparse
import json

# Get temp file
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear_storage():
    """
    Full clearing of storage
    """
    os.remove(storage_path)


def get_data():
    """
    Get dictionary in which still data from storage
    :return: Function will return dictionary for working with it
    :rtype: dict
    """
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        data = f.read()
        if data:
            return json.loads(data)

        return {}


def process_data(key, value=None):
    data = get_data()
    if value:
        if key in data:
            data[key].append(value)
        else:
            data[key] = [value]

        with open(storage_path, 'w') as f:
            f.write(json.dumps(data))
    else:
        return data.get(key)


if __name__ == '__main__':
    # Get args
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Add or get value by key")
    parser.add_argument("--value", "--val", help="Add value by key")
    parser.add_argument('--clear', action='store_true', help='Full clearing of storage')
    args = parser.parse_args()

    if args.clear:
        clear_storage()
    elif args.key:
        if args.value:
            process_data(args.key, args.value)
        else:
            result = process_data(args.key)
            print(*([None] if not result else result), sep=", ")
    else:
        parser.print_help()
