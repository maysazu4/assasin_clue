import json
def load_file(file):
    try:
        with open(file) as user_file:
            file_contents = user_file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print("Error:", e)
    parsed_json = json.loads(file_contents)
    return parsed_json