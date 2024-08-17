import requests

def test_requests():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"requests: {response.json()}")


if __name__ == "__main__":
    test_requests()