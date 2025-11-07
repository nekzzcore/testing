import requests
import json

BASE_URL = "https://dog.ceo/api"

def test_list_all_breeds():
    """Test 1: List all breeds"""
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert isinstance(data["message"], dict)
    print("Test 1 passed: List all breeds")

def test_list_all_breeds_structure():
    """Test 2: Check structure of breeds list"""
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    data = response.json()
    breeds = data["message"]
    # Check that some known breeds exist
    assert "hound" in breeds
    assert "retriever" in breeds
    # Check that sub-breeds are arrays
    assert isinstance(breeds["hound"], list)
    print("Test 2 passed: Breeds list structure")

def test_random_image():
    """Test 3: Random image"""
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert data["message"].startswith("https://")
    assert data["message"].endswith(".jpg")
    print("Test 3 passed: Random image")

def test_random_image_multiple():
    """Test 4: Multiple random images"""
    response = requests.get(f"{BASE_URL}/breeds/image/random/3")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) == 3
    for img in data["message"]:
        assert img.startswith("https://")
        assert img.endswith(".jpg")
    print("Test 4 passed: Multiple random images")

def test_images_by_breed():
    """Test 5: Images by breed"""
    breed = "hound"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) > 0
    for img in data["message"]:
        assert img.startswith("https://")
        assert img.endswith(".jpg")
    print("Test 5 passed: Images by breed")

def test_random_image_by_breed():
    """Test 6: Random image by breed"""
    breed = "hound"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://")
    assert data["message"].endswith(".jpg")
    print("Test 6 passed: Random image by breed")

def test_random_multiple_images_by_breed():
    """Test 7: Multiple random images by breed"""
    breed = "hound"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random/2")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) == 2
    for img in data["message"]:
        assert img.startswith("https://")
        assert img.endswith(".jpg")
    print("Test 7 passed: Multiple random images by breed")

def test_sub_breeds():
    """Test 8: Sub-breeds list"""
    breed = "hound"
    response = requests.get(f"{BASE_URL}/breed/{breed}/list")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    print("Test 8 passed: Sub-breeds list")

def test_random_image_by_sub_breed():
    """Test 9: Random image by sub-breed"""
    breed = "hound"
    sub_breed = "afghan"
    response = requests.get(f"{BASE_URL}/breed/{breed}/{sub_breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://")
    assert data["message"].endswith(".jpg")
    print("Test 9 passed: Random image by sub-breed")

def test_images_by_sub_breed():
    """Test 10: Images by sub-breed"""
    breed = "hound"
    sub_breed = "afghan"
    response = requests.get(f"{BASE_URL}/breed/{breed}/{sub_breed}/images")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) > 0
    for img in data["message"]:
        assert img.startswith("https://")
        assert img.endswith(".jpg")
    print("Test 10 passed: Images by sub-breed")

def test_invalid_breed():
    """Test 11: Invalid breed"""
    response = requests.get(f"{BASE_URL}/breed/invalidbreed/images/random")
    assert response.status_code == 404
    data = response.json()
    assert data["status"] == "error"
    assert "Breed not found" in data["message"]
    print("Test 11 passed: Invalid breed")

def test_invalid_sub_breed():
    """Test 12: Invalid sub-breed"""
    breed = "hound"
    response = requests.get(f"{BASE_URL}/breed/{breed}/invalidsub/images/random")
    assert response.status_code == 404
    data = response.json()
    assert data["status"] == "error"
    assert "Breed not found" in data["message"]
    print("Test 12 passed: Invalid sub-breed")

def test_breed_without_sub_breed():
    """Test 13: Breed without sub-breeds"""
    breed = "beagle"  # Known to have no sub-breeds
    response = requests.get(f"{BASE_URL}/breed/{breed}/list")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"] == []
    print("Test 13 passed: Breed without sub-breeds")

def test_random_image_format():
    """Test 14: Check image URL format"""
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()
    url = data["message"]
    # Check if URL contains breed name
    assert "https://images.dog.ceo/breeds/" in url
    assert url.endswith(".jpg")
    print("Test 14 passed: Image URL format")

def test_all_breeds_have_images():
    """Test 15: Ensure all breeds have at least one image"""
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    breeds_data = response.json()["message"]
    for breed, sub_breeds in breeds_data.items():
        # Test main breed
        img_response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
        assert img_response.status_code == 200
        img_data = img_response.json()
        assert img_data["status"] == "success"
        # Test sub-breeds if any
        for sub in sub_breeds:
            sub_img_response = requests.get(f"{BASE_URL}/breed/{breed}/{sub}/images/random")
            assert sub_img_response.status_code == 200
            sub_img_data = sub_img_response.json()
            assert sub_img_data["status"] == "success"
    print("Test 15 passed: All breeds have images")

if __name__ == "__main__":
    # Run all tests
    test_list_all_breeds()
    test_list_all_breeds_structure()
    test_random_image()
    test_random_image_multiple()
    test_images_by_breed()
    test_random_image_by_breed()
    test_random_multiple_images_by_breed()
    test_sub_breeds()
    test_random_image_by_sub_breed()
    test_images_by_sub_breed()
    test_invalid_breed()
    test_invalid_sub_breed()
    test_breed_without_sub_breed()
    test_random_image_format()
    test_all_breeds_have_images()
    print("All tests passed!")
