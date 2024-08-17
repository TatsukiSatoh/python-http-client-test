import httpx

def test_httpx():
    response = httpx.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"httpx: {response.json()}")

if __name__ == "__main__":
    test_httpx()