import requests
import random

BASE_URL = "https://qa-internship.avito.com"
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def generate_seller_id():
    return random.randint(111111, 999999)


def test_1_create_item():
    print("Test 1: Create item")

    seller_id = generate_seller_id()
    data = {
        "sellerID": seller_id,
        "name": "Test Item",
        "price": 1500,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
    }

    response = requests.post(f"{BASE_URL}/api/1/item", headers=HEADERS, json=data)
    assert response.status_code == 200
    result = response.json()
    assert "status" in result

    print("Item created successfully")
    print(f"Server response: {result['status']}")
    print(f"Seller ID: {seller_id}")


def test_2_get_item_by_id():
    print("\nTest 2: Get item by ID")

    seller_id = generate_seller_id()
    data = {
        "sellerID": seller_id,
        "name": "Test Item",
        "price": 2000,
        "statistics": {
            "likes": 5,
            "viewCount": 50,
            "contacts": 2
        }
    }

    create_response = requests.post(f"{BASE_URL}/api/1/item", headers=HEADERS, json=data)
    status_text = create_response.json()["status"]
    item_id = status_text.split(" - ")[1]

    response = requests.get(f"{BASE_URL}/api/1/item/{item_id}", headers=HEADERS)
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)

    print("Item retrieved successfully")
    print(f"Item ID: {item_id}")
    print(f"Items found: {len(items)}")


def test_3_get_items_by_seller():
    print("\nTest 3: Get all seller items")

    seller_id = generate_seller_id()

    data1 = {
        "sellerID": seller_id,
        "name": "First Item",
        "price": 1000,
        "statistics": {"likes": 1, "viewCount": 10, "contacts": 1}
    }

    data2 = {
        "sellerID": seller_id,
        "name": "Second Item",
        "price": 2000,
        "statistics": {"likes": 2, "viewCount": 20, "contacts": 2}
    }

    requests.post(f"{BASE_URL}/api/1/item", headers=HEADERS, json=data1)
    requests.post(f"{BASE_URL}/api/1/item", headers=HEADERS, json=data2)

    response = requests.get(f"{BASE_URL}/api/1/{seller_id}/item", headers=HEADERS)
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)

    print("Seller items retrieved successfully")
    print(f"Seller ID: {seller_id}")
    print(f"Items count: {len(items)}")


def test_4_get_statistics():
    print("\nTest 4: Get item statistics")

    seller_id = generate_seller_id()
    data = {
        "sellerID": seller_id,
        "name": "Test Item",
        "price": 3000,
        "statistics": {
            "likes": 15,
            "viewCount": 150,
            "contacts": 8
        }
    }

    create_response = requests.post(f"{BASE_URL}/api/1/item", headers=HEADERS, json=data)
    status_text = create_response.json()["status"]
    item_id = status_text.split(" - ")[1]

    response = requests.get(f"{BASE_URL}/api/1/statistic/{item_id}", headers=HEADERS)
    assert response.status_code == 200
    stats = response.json()
    assert isinstance(stats, list)

    print("Statistics retrieved successfully")
    print(f"Item ID: {item_id}")
    print(f"Statistics records: {len(stats)}")


if __name__ == "__main__":
    test_1_create_item()
    test_2_get_item_by_id()
    test_3_get_items_by_seller()
    test_4_get_statistics()
    print("\nAll tests completed successfully")