from typing import Any
import json


def load_json_file(file_path: str) -> Any:
    """Try to load file and return its data. If an error shows up, raise it"""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError("Path to JSON file was not found")
    except ValueError:
        raise ValueError("Data does not meet requirements to be considered a json file")
    except OSError:
        raise OSError("Invalid file. It needs a text extension")
    except Exception as e:
        raise Exception(str(e))
