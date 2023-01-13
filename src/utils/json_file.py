from pydantic import validate_arguments
import json

@validate_arguments
def write(content, file_path: str):
    with open(file_path, "w+", encoding="utf-8") as file:
        json.dump(content, file)

@validate_arguments
def read(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        content = json.load(file)
        return content

__all__ = [ write, read ]