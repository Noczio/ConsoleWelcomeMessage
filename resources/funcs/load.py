from typing import Any
import json


def load_json_file(file_path: str) -> Any:
    """Try to load file and set data, if error raise Error"""
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        raise FileNotFoundError("Path to JSON file was not found")
    except ValueError:
        raise ValueError("Data does not meet requirements to be considered a json file")
    except OSError:
        raise OSError("Invalid file. It needs a text extension")
    except Exception as e:
        raise Exception(str(e))
