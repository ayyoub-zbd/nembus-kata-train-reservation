import json
import requests

train_id = "express_2000"
session = requests.Session()

def init():
    response = session.post(f"http://127.0.0.1:8081/reset/{train_id}")
    response.raise_for_status()


def reserve(number = 1):
    
    for nombre in range(number):
        response = session.post(
            "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
        )
        assert response.status_code == 200, response.text
    
    return response
    

def test_reserve_seats_from_empty_train():

    init()
    reservation = reserve().json()
    assert reservation["train_id"] == train_id
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["1A", "2A", "3A", "4A"]


def test_reserve_four_additional_seats():

    init()
    reservation = reserve(2).json()
    assert reservation["train_id"] == train_id
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["5A", "6A", "7A", "8A"]
