import json
from datetime import datetime

def validate_json(data):
    try:
        # Check if data is a valid JSON
        data = json.loads(data) if isinstance(data, str) else data

        # Validate 'id'
        if not (0 <= data.get("id", -1) <= 4294967295):
            return False, "Invalid 'id' value"

        # Validate 'eq'
        if not (0 <= data.get("eq", -1) <= 100):
            return False, "Invalid 'eq' value"

        # Validate 'MLoc' and 'LLoc'
        for loc in ["MLoc", "LLoc"]:
            if loc not in data or not isinstance(data[loc], dict):
                return False, f"Missing or invalid '{loc}' field"
            
            lat = data[loc].get("lat")
            lon = data[loc].get("lon")
            alt = data[loc].get("alt")

            if not (-90 <= lat <= 90):
                return False, f"Invalid latitude in '{loc}'"
            if not (-180 <= lon <= 180):
                return False, f"Invalid longitude in '{loc}'"
            if not (-1000 <= alt <= 3000):
                return False, f"Invalid altitude in '{loc}'"

        # Validate 'LLocE'
        if "LLocE" not in data or not isinstance(data["LLocE"], dict):
            return False, "Missing or invalid 'LLocE' field"
        
        major_aa = data["LLocE"].get("MajorAA")
        major_al = data["LLocE"].get("MajorAL")
        minor_al = data["LLocE"].get("MinorAL")

        if not (-6.2832 <= major_aa <= 6.2832):
            return False, "Invalid 'MajorAA' in 'LLocE'"
        if not (0 <= major_al <= 3.4E+38):
            return False, "Invalid 'MajorAL' in 'LLocE'"
        if not (0 <= minor_al <= 3.4E+38):
            return False, "Invalid 'MinorAL' in 'LLocE'"

        # Validate 'time'
        time_str = data.get("time")
        try:
            datetime.strptime(time_str, '%d.%m.%Y %H:%M:%S.%f')
        except (ValueError, TypeError):
            return False, "Invalid 'time' format"

        # If all validations pass
        return True, "JSON is valid"

    except (json.JSONDecodeError, TypeError) as e:
        return False, "Invalid JSON format"

# # Example usage:
# json_data = {
#     "id": 123456,
#     "eq": 100,
#     "MLoc": {"lat": 56.98, "lon": 45.12, "alt": 1230},
#     "LLoc": {"lat": 56.98, "lon": 45.12, "alt": 1230},
#     "LLocE": {"MajorAA": 3.14, "MajorAL": 1.0E+38, "MinorAL": 2.5E+38},
#     "time": "08.09.2024 12:34:56.00"
# }

# is_valid, message = validate_json(json_data)
# print(is_valid, message)
