import json
import pytest
from app import database

def test_capture_image(client):
    response = client.post('/capture_image', json={
        "with_defect": True,
        "low_lighting": False
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'raw_image' in data
    assert 'image_UUID' in data
    assert 'defect_present' in data

def test_get_result(client):
    capture_response = client.post('/capture_image', json={
        "with_defect": True,
        "low_lighting": False
    })
    assert capture_response.status_code == 200
    capture_data = capture_response.get_json()
    image_uuid = capture_data['image_UUID']

    get_response = client.get(f'/get_result/{image_uuid}')
    assert get_response.status_code == 200
    result_data = get_response.get_json()
    assert 'id' in result_data
    assert 'image_id' in result_data
    assert 'defect_detected' in result_data
    assert 'with_defect' in result_data
    assert 'low_lighting' in result_data

def test_get_result_not_found(client):
    response = client.get('/get_result/nonexistent-uuid')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
