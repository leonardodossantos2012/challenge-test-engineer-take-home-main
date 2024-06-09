capture_image_schema = {
    "type": "object",
    "properties": {
        "raw_image": {
            "type": "array",
            "items": {"type": "array", "items": {"type": "integer"}}
        },
        "image_UUID": {"type": "string"},
        "defect_present": {"type": "boolean"}
    },
    "required": ["raw_image", "image_UUID", "defect_present"]
}

get_result_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "image_id": {"type": "string"},
        "defect_detected": {"type": "integer"},
        "with_defect": {"type": "integer"},
        "low_lighting": {"type": "integer"}
    },
    "required": ["id", "image_id", "defect_detected", "with_defect", "low_lighting"]
}
