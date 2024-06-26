import pytest
import jsonschema
from tests.utils.schemas import capture_image_schema, get_result_schema

def test_capture_image_and_validate_defect(client):
    capture_response = client.post('/capture_image', json={
        "with_defect": True,
        "low_lighting": False
    })
    assert capture_response.status_code == 200
    capture_data = capture_response.get_json()
    image_uuid = capture_data['image_UUID']
    
    jsonschema.validate(instance=capture_data, schema=capture_image_schema)
    
    assert capture_data['defect_present'] is True

    get_response = client.get(f'/get_result/{image_uuid}')
    assert get_response.status_code == 200
    result_data = get_response.get_json()

    jsonschema.validate(instance=result_data, schema=get_result_schema)

    assert result_data['defect_detected'] == 1
    assert result_data['with_defect'] == 1
    assert result_data['low_lighting'] == 0

def test_capture_image_and_validate_no_defect(client):
    capture_response = client.post('/capture_image', json={
        "with_defect": False,
        "low_lighting": False
    })
    assert capture_response.status_code == 200
    capture_data = capture_response.get_json()
    image_uuid = capture_data['image_UUID']
    
    jsonschema.validate(instance=capture_data, schema=capture_image_schema)

    assert capture_data['defect_present'] is False

    get_response = client.get(f'/get_result/{image_uuid}')
    assert get_response.status_code == 200
    result_data = get_response.get_json()

    jsonschema.validate(instance=result_data, schema=get_result_schema)

    assert result_data['defect_detected'] == 0
    assert result_data['with_defect'] == 0
    assert result_data['low_lighting'] == 0
