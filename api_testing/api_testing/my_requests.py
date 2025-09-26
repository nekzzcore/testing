from base_request import BaseRequest, BASE_URL_PETSTORE


class UserRequests(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_PETSTORE)

    def create_user(self, user_data):
        response = self.request('POST', 'user', data=user_data)
        return response.json()

    def get_user(self, username):
        return self.get('user', username)

    def update_user(self, username, user_data):
        return self.put('user', username, user_data)

    def delete_user(self, username):
        return self.delete('user', username)


class StoreRequests(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_PETSTORE)

    def get_inventory(self):
        response = self.request('GET', 'store/inventory')
        return response.json()

    def place_order(self, order_data):
        response = self.request('POST', 'store/order', data=order_data)
        return response.json()

    def get_order(self, order_id):
        return self.get('store/order', order_id)

    def delete_order(self, order_id):
        return self.delete('store/order', order_id)


# Example usage
if __name__ == '__main__':
    user_req = UserRequests()
    store_req = StoreRequests()

    # Example for user
    user_data = {
        "id": 123,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }
    created_user = user_req.create_user(user_data)
    print("Created user:", created_user)

    user = user_req.get_user("testuser")
    print("Got user:", user)

    updated_user = user_req.update_user("testuser", {**user_data, "email": "updated@example.com"})
    print("Updated user:", updated_user)

    delete_msg = user_req.delete_user("testuser")
    print("Delete message:", delete_msg)

    # Example for store
    inventory = store_req.get_inventory()
    print("Inventory:", inventory)

    order_data = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-10-01T00:00:00.000Z",
        "status": "placed",
        "complete": False
    }
    placed_order = store_req.place_order(order_data)
    print("Placed order:", placed_order)

    order = store_req.get_order(1)
    print("Got order:", order)

    delete_order_msg = store_req.delete_order(1)
    print("Delete order message:", delete_order_msg)
