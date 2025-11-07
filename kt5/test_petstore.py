import pytest
import allure
from models import Pet, Category, Tag
from conftest import api_client, base_url, sample_pet

@allure.epic("Petstore API")
@allure.feature("Pet Management")
class TestPetAPI:

    @allure.story("Add new pet")
    @allure.title("Add a new pet to the store")
    @allure.description("Test adding a new pet with valid data")
    def test_add_pet(self, api_client, base_url, sample_pet):
        with allure.step("Prepare pet data"):
            pet_data = sample_pet.model_dump()

        with allure.step("Send POST request to add pet"):
            response = api_client.post(f"{base_url}/pet", json=pet_data)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            pet_response = Pet.model_validate(response_data)
            assert pet_response.name == sample_pet.name
            assert pet_response.status == sample_pet.status

    @allure.story("Get pet by ID")
    @allure.title("Retrieve pet by ID")
    @allure.description("Test retrieving a pet by its ID")
    def test_get_pet_by_id(self, api_client, base_url, sample_pet):
        pet_id = sample_pet.id

        with allure.step(f"Send GET request for pet ID {pet_id}"):
            response = api_client.get(f"{base_url}/pet/{pet_id}")
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            pet_response = Pet.model_validate(response_data)
            assert pet_response.id == pet_id

    @allure.story("Update pet")
    @allure.title("Update existing pet")
    @allure.description("Test updating an existing pet's information")
    def test_update_pet(self, api_client, base_url, sample_pet):
        updated_pet = sample_pet.model_copy(update={"name": "UpdatedTestPet", "status": "sold"})

        with allure.step("Prepare updated pet data"):
            pet_data = updated_pet.model_dump()

        with allure.step("Send PUT request to update pet"):
            response = api_client.put(f"{base_url}/pet", json=pet_data)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            pet_response = Pet.model_validate(response_data)
            assert pet_response.name == updated_pet.name
            assert pet_response.status == updated_pet.status

    @allure.story("Find pets by status")
    @allure.title("Find pets by status")
    @allure.description("Test finding pets by their status")
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_find_pets_by_status(self, api_client, base_url, status):
        with allure.step(f"Send GET request to find pets with status '{status}'"):
            response = api_client.get(f"{base_url}/pet/findByStatus", params={"status": status})
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            pets = [Pet.model_validate(pet) for pet in response_data]
            for pet in pets:
                assert pet.status == status

    @allure.story("Delete pet")
    @allure.title("Delete a pet")
    @allure.description("Test deleting a pet by ID")
    def test_delete_pet(self, api_client, base_url, sample_pet):
        pet_id = sample_pet.id

        with allure.step(f"Send DELETE request for pet ID {pet_id}"):
            response = api_client.delete(f"{base_url}/pet/{pet_id}")
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"

@allure.epic("Petstore API")
@allure.feature("Store Management")
class TestStoreAPI:

    @allure.story("Get inventory")
    @allure.title("Get pet inventory")
    @allure.description("Test retrieving the pet inventory")
    def test_get_inventory(self, api_client, base_url):
        with allure.step("Send GET request to get inventory"):
            response = api_client.get(f"{base_url}/store/inventory")
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate that response is a dictionary with integer values
            assert isinstance(response_data, dict)
            for key, value in response_data.items():
                assert isinstance(value, int)

    @allure.story("Place order")
    @allure.title("Place an order for a pet")
    @allure.description("Test placing an order for a pet")
    def test_place_order(self, api_client, base_url, sample_order):
        with allure.step("Prepare order data"):
            order_data = sample_order.model_dump()

        with allure.step("Send POST request to place order"):
            response = api_client.post(f"{base_url}/store/order", json=order_data)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            order_response = Order.model_validate(response_data)
            assert order_response.petId == sample_order.petId
            assert order_response.quantity == sample_order.quantity

    @allure.story("Get order by ID")
    @allure.title("Retrieve order by ID")
    @allure.description("Test retrieving an order by its ID")
    def test_get_order_by_id(self, api_client, base_url, sample_order):
        order_id = sample_order.id

        with allure.step(f"Send GET request for order ID {order_id}"):
            response = api_client.get(f"{base_url}/store/order/{order_id}")
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            order_response = Order.model_validate(response_data)
            assert order_response.id == order_id

@allure.epic("Petstore API")
@allure.feature("User Management")
class TestUserAPI:

    @allure.story("Create user")
    @allure.title("Create a new user")
    @allure.description("Test creating a new user")
    def test_create_user(self, api_client, base_url, sample_user):
        with allure.step("Prepare user data"):
            user_data = sample_user.model_dump()

        with allure.step("Send POST request to create user"):
            response = api_client.post(f"{base_url}/user", json=user_data)
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            # Note: The API might not return the created user data, so we just check the status

    @allure.story("Get user by username")
    @allure.title("Retrieve user by username")
    @allure.description("Test retrieving a user by username")
    def test_get_user_by_username(self, api_client, base_url, sample_user):
        username = sample_user.username

        with allure.step(f"Send GET request for user '{username}'"):
            response = api_client.get(f"{base_url}/user/{username}")
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # Validate response using Pydantic
            user_response = User.model_validate(response_data)
            assert user_response.username == username

    @allure.story("Login user")
    @allure.title("User login")
    @allure.description("Test user login functionality")
    def test_login_user(self, api_client, base_url, sample_user):
        username = sample_user.username
        password = sample_user.password

        with allure.step(f"Send GET request to login user '{username}'"):
            response = api_client.get(f"{base_url}/user/login", params={"username": username, "password": password})
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            allure.attach(str(response_data), name="Response Data", attachment_type=allure.attachment_type.JSON)

            # The response should contain a session token or similar
            assert "message" in response_data or isinstance(response_data, str)

    @allure.story("Logout user")
    @allure.title("User logout")
    @allure.description("Test user logout functionality")
    def test_logout_user(self, api_client, base_url):
        with allure.step("Send GET request to logout user"):
            response = api_client.get(f"{base_url}/user/logout")
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Verify response"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
