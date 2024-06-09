import pytest
import jsonschema
from tests.utils.schemas import capture_image_schema, get_result_schema

def test_capture_image_and_validate_defect(client):
    # Step 1: Capture an image with a defect
    capture_response = client.post('/capture_image', json={
        "with_defect": True,
        "low_lighting": False
    })
    assert capture_response.status_code == 200
    capture_data = capture_response.get_json()
    image_uuid = capture_data['image_UUID']
    
    # Validate JSON schema
    jsonschema.validate(instance=capture_data, schema=capture_image_schema)
    
    # Ensure defect_detected is True in the capture response
    assert capture_data['defect_present'] is True

    # Step 2: Fetch the result using the image_uuid
    get_response = client.get(f'/get_result/{image_uuid}')
    assert get_response.status_code == 200
    result_data = get_response.get_json()

    # Validate JSON schema
    jsonschema.validate(instance=result_data, schema=get_result_schema)

    # Ensure the defect_detected is 1 (True) in the get_result response
    assert result_data['defect_detected'] == 1
    assert result_data['with_defect'] == 1  # Adjusted for SQLite integer storage
    assert result_data['low_lighting'] == 0  # Adjusted for SQLite integer storage

def test_capture_image_and_validate_no_defect(client):
    # Step 1: Capture an image without a defect
    capture_response = client.post('/capture_image', json={
        "with_defect": False,
        "low_lighting": False
    })
    assert capture_response.status_code == 200
    capture_data = capture_response.get_json()
    image_uuid = capture_data['image_UUID']
    
    # Validate JSON schema
    jsonschema.validate(instance=capture_data, schema=capture_image_schema)

    # Ensure defect_detected is False in the capture response
    assert capture_data['defect_present'] is False

    # Step 2: Fetch the result using the image_uuid
    get_response = client.get(f'/get_result/{image_uuid}')
    assert get_response.status_code == 200
    result_data = get_response.get_json()

    # Validate JSON schema
    jsonschema.validate(instance=result_data, schema=get_result_schema)

    # Ensure the defect_detected is 0 (False) in the get_result response
    assert result_data['defect_detected'] == 0
    assert result_data['with_defect'] == 0  # Adjusted for SQLite integer storage
    assert result_data['low_lighting'] == 0  # Adjusted for SQLite integer storage
