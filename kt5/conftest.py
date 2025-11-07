import pytest
import requests
from models import Pet, User, Order

@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture
def api_client(base_url):
    return requests.Session()

@pytest.fixture
def sample_pet():
    return Pet(
        id=12345,
        name="TestPet",
        photoUrls=["http://example.com/photo.jpg"],
        status="available"
    )

@pytest.fixture
def sample_user():
    return User(
        id=12345,
        username="testuser",
        firstName="Test",
        lastName="User",
        email="test@example.com",
        password="password123",
        phone="1234567890"
    )

@pytest.fixture
def sample_order():
    return Order(
        id=12345,
        petId=12345,
        quantity=1,
        status="placed"
    )
