import json

class StorageService:
    @staticmethod
    def save_as_json(data, filename="funny_moments.json"):
        """Saves dictionary data to a JSON file with UTF-8 support."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Data successfully saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
