import json
from student import Student

def load_students_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            students_data = json.load(file)
            return [Student(**data) for data in students_data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading students from JSON: {e}")
        return []
