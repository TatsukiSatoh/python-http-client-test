import httpx

def test_httpx():
    response = httpx.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"httpx: {response.json()}")


def quick_start():
    r = httpx.get("https://httpbin.org/get")

    print(f"r: {r}")

    # CRUD + HEAD. OPTIONのリクエストのやり方
    r = httpx.post("https://httpbin.org/post", data={"key": "value"})
    r = httpx.put("https://httpbin.org/put", data={"key": "value"})
    r = httpx.delete("https://httpbin.org/delete")
    r = httpx.head("https://httpbin.org/get")
    r = httpx.options("https://httpbin.org/get")

    # クエリパラメータを渡すには、paramsを使う
    r = httpx.get("https://httpbin.org/get", params={"key1": "value1", "key2": "value2"})
    # urlエンコードされたurlを確認するには、urlでみれる
    print(f"url: {r.url}")
    # アイテムのリストを値として渡すこともできる
    params = {"key1": "value1", "key2": ["value2", "value3"]}
    r = httpx.get("https://httpbin.org/get", params=params)
    print(f"url: {r.url}")

    # Response
    print(f"r: {r.text}")
    print(f"r.encoding: {r.encoding}")
    print(f"r.content: {r.content}")
    print(f"r.json: {r.json()}")

    # Headers
    url = "https://httpbin.org/headers"
    headers = {"user-agent": "my-app/0.0.1"}
    r = httpx.get(url, headers=headers)


    # Request Body
    data = {"key1": "value1", "key2": "value2"}
    r = httpx.post("https://httpbin.org/post", data=data)
    ## ファイルを指定することも可能
    # files = {"file": open("image.png", "rb")}
    # r = httpx.post("https://httpbin.org/post", files=files)
    ## json encodeされたデータを送信することも可能
    r = httpx.post("https://httpbin.org/post", json=data)
    ## バイナリデータの送信も可能
    content = b"Hello, World"
    r = httpx.post("https://httpbin.org/post", content=content)

    # Response Status code
    ## 2XX以外のコードではない場合、例外を発生させることができる
    r = httpx.get("https://httpbin.org/status/404")
    # r.raise_for_status()
    ## raise_for_statusはレスポンスインスタンスを返すので、下記のように書くことも可能
    ## このようにインラインで書くことも可能
    data = httpx.get("https://httpbin.org/get").raise_for_status().json()

    # Headers
    print(r.headers)
    # 小文字と大文字を区別せずに自由に設定することが可能
    ## ただし、HTTP/2については、すべて小文字にする必要はあるらしい
    # data = httpx.get("https://httpbin.org/get", http2=True)
    # print(data.http_version)
    # print(data.headers["content-type"])
    # print(data.headers["Content-Type"])

    # import asyncio
    # async def async_request():
    #     async with httpx.AsyncClient(http2=True) as client:
    #         # Your code inside the async with statement
    #         response = client.get("https://www.example.com")
    
    # # Call the async function
    # asyncio.run(async_request())
        # response = client.get("https://www.example.com")


def async_request():
    import asyncio
    async def async_request():
        async with httpx.AsyncClient(http2=True) as client:
            # Your code inside the async with statement
            response = await client.get("https://www.example.com")
            print(response.headers)
            # HTTP/2では小文字にしようみたいなこと言われているが、一応どちらでも取れる
            print(response.headers["content-type"])
            print(response.headers["Content-Type"])
    
    # Call the async function
    asyncio.run(async_request())


if __name__ == "__main__":
    # test_httpx()
    # quick_start()
    async_request()
