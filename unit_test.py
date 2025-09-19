# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os
import time
import requests
# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app instance from the main app file
from main import app 
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    # app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_posts(client):
    """Test the posts api ."""
    response = client.get('/posts')
    assert response.status_code == 200
    
def test_non_existent_post(client):
    """Test for a non-existent route."""
    response = client.get('/posts/234')
    assert response.status_code == 404

def test_existent_post(client):
    """Test for a non-existent route."""
    response = client.get('/posts/1')
    assert response.status_code == 200


def test_comments(client):
    """Test the comments api ."""
    start_time = time.perf_counter()
    response = client.get('/comments')
    end_time = time.perf_counter() 
    response_time = end_time - start_time
    print(f"\nResponse time for GET /comments  : {response_time:.4f} seconds")
    assert response.status_code == 200



def test_existent_comment(client):
    """Test for a non-existent route."""
    response = client.get('/comments/50')
    assert response.status_code == 200


def test_non_existent_comment(client):
    """Test for a non-existent route."""
    response = client.get('/comments/60000')
    assert response.status_code == 404
    




# SLA APIs
# todos API
def test_todos(client):
    """Test the todos api ."""
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/todos'}: {response_time:.4f} seconds")
    assert response.status_code == 200


def test_non_existent_todos(client):
    """Test for a non-existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/todos/989898")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/todos/989898'}: {response_time:.4f} seconds")
    assert response.status_code == 404

def test_existent_todos(client):
    """Test for an existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/todos/30")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/todos/30'}: {response_time:.4f} seconds")
    assert response.status_code == 200


#users API
def test_users(client):
    """Test the comments api ."""
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/users'}: {response_time:.4f} seconds")
    assert response.status_code == 200
   


def test_non_existent_users(client):
    """Test for a non-existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/comments/501")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/comments/501'}: {response_time:.4f} seconds")
    assert response.status_code == 404

def test_existent_users(client):
    """Test for an existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/users/10")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/users/10'}: {response_time:.4f} seconds")
    assert response.status_code == 200

#albums API
def test_albums(client):
    """Test the comments api ."""
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/albums'}: {response_time:.4f} seconds")
    assert response.status_code == 200


def test_non_existent_albums(client):
    """Test for a non-existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/albums/101")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/albums/101'}: {response_time:.4f} seconds")
    assert response.status_code == 404

def test_existent_albums(client):
    """Test for an existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/albums/40")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/albums/40'}: {response_time:.4f} seconds")
    assert response.status_code == 200

#photos API
def test_photos(client):
    """Test the comments api ."""
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/photos'}: {response_time:.4f} seconds")
    assert response.status_code == 200

    assert response_time < 1


def test_non_existent_photos(client):
    """Test for a non-existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/photos/5001")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/photos/5001'}: {response_time:.4f} seconds")
    assert response.status_code == 404

def test_existent_photos(client):
    """Test for an existent route."""
    response = requests.get("https://jsonplaceholder.typicode.com/photos/5000")
    response_time = response.elapsed.total_seconds()
    print(f"Response time for GET {'https://jsonplaceholder.typicode.com/photos/5000'}: {response_time:.4f} seconds")
    assert response.status_code == 200