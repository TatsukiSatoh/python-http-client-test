import test_httpx

def test_httpx():
    response = test_httpx.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"httpx: {response.json()}")

if __name__ == "__main__":
    test_httpx()