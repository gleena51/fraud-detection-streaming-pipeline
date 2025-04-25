import json

def parse_transaction(raw):
    try:
        return json.loads(raw)
    except Exception as e:
        print(f"Error parsing transaction: {e}")
        return {}
