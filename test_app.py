import pytest
import os
from unittest.mock import patch, MagicMock
from app import app, get_gemma_response, input_image_setup

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route returns 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_settings_route(client):
    """Test the settings route returns 200."""
    response = client.get('/settings')
    assert response.status_code == 200

def test_analytics_route(client):
    """Test the analytics route returns 200."""
    response = client.get('/analytics')
    assert response.status_code == 200

def test_save_api_key_missing_data(client):
    """Test save API key endpoint with missing data."""
    response = client.post('/save-api-key', 
                          json={}, 
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_save_api_key_success(client):
    """Test save API key endpoint with valid data."""
    with client.session_transaction() as sess:
        response = client.post('/save-api-key', 
                              json={'api_key': 'test-key'}, 
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data

def test_test_api_key_missing_data(client):
    """Test test API key endpoint with missing data."""
    response = client.post('/test-api-key', 
                          json={}, 
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

@patch('app.genai.configure')
@patch('app.genai.GenerativeModel')
def test_test_api_key_success(mock_model, mock_configure, client):
    """Test test API key endpoint with valid data."""
    mock_model.return_value = MagicMock()
    
    response = client.post('/test-api-key', 
                          json={'api_key': 'test-key'}, 
                          content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data

def test_analyze_invoice_no_file(client):
    """Test analyze invoice endpoint with no file."""
    response = client.post('/analyze', 
                         data={'input_text': 'test question'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_analyze_invoice_no_api_key(client):
    """Test analyze invoice endpoint with no API key."""
    # Create a test file
    test_file = (io.BytesIO(b'test image data'), 'test.jpg')
    
    response = client.post('/analyze', 
                         data={'image': test_file, 'input_text': 'test question'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_input_image_setup_valid_file():
    """Test input_image_setup with valid file."""
    from PIL import Image
    import io
    
    # Create a test image
    img = Image.new('RGB', (100, 100), color='red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    result = input_image_setup(img_byte_arr)
    assert isinstance(result, Image.Image)

def test_input_image_setup_no_file():
    """Test input_image_setup with no file."""
    with pytest.raises(FileNotFoundError):
        input_image_setup(None)

if __name__ == '__main__':
    pytest.main([__file__])
