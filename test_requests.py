import requests
from requests import Request


# Test Function
def test_requests():
    response: Request = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"status code: {response.status_code}") # 200
    print(f"headers: {response.headers}")
    print(f"content-type: {response.headers['content-type']}")
    print(f"encoding: {response.encoding}")
    print(f"text: {response.text}")
    print(f"requests: {response.json()}")

# 公式DocのQuick Start
def quick_start():
    r_get = requests.get('https://api.github.com/events')

    r_post = requests.post('https://httpbin.org/post', data = {'key':'value'})
    r_put = requests.put("https://httpbin.org/put", data = {'key':'value'})
    r_delete = requests.delete("https://httpbin.org/delete")

    # head request: https://developer.mozilla.org/ja/docs/Web/HTTP/Methods/HEAD
    r_head = requests.head("https://httpbin.org/get")
    # options request: https://developer.mozilla.org/ja/docs/Web/HTTP/Methods/OPTIONS
    r_options = requests.options("https://httpbin.org/get")

    print(f"r_get: {r_get.json()}")
    print(f"r_post: {r_post.json()}")
    print(f"r_put: {r_put.json()}")
    print(f"r_delete: {r_delete.json()}")
    print(f"r_head: {r_head.text}")
    print(f"r_options: {r_options.text}")

    # クエリパラメータ paramsで指定する
    payload = {"key1": "value1", "key2": "value2"}
    r_query = requests.get('https://httpbin.org/get', params=payload)

    # バイナリデータの場合
    r_image = requests.get('https://httpbin.org/image/png')
    with open('image.png', 'wb') as f:
        f.write(r_image.content)

    # JSONレスポンスコンテンツの場合
    r_json = requests.get('https://api.github.com/events1')
    # ここでエラー判定をする
    # r_json.raise_for_status()
    # print(f"r_json: {r_json.json()}")

    # カスタムヘッダーの追加
    headers = {'user-agent': 'my-app/0.0.1'}
    r_custom_header = requests.get('https://api.github.com/events', headers=headers)

    # レスポンスヘッダーの取得
    r_header = requests.get('https://api.github.com/events')
    print(f"r_header: {r_header.headers}")
    # この時、RFC 7230によるとヘッダ名は大文字と小文字を区別しないので下記はどちらも同じ値を返すはず
    print(f"r_header: {r_header.headers['Content-Type']}")
    print(f"r_header: {r_header.headers['content-type']}")

    # リダイレクト処理を無効にする, (defaultでTrueになっていることに注意)
    r_redirect = requests.get("http://github.com", allow_redirects=False)
    print(f"r_redirect: {r_redirect.status_code}")
    print(f"r_redirect: {r_redirect.url}")
    # リダイレクトされる場合にはここにResponseオブジェクトが追加される
    print(f"r_redirect: {r_redirect.history}")

    # 最大リダイレクト数を変更する場合
    session = requests.Session()
    session.max_redirects = 5  # リダイレクトの上限を5回に設定

    try:
        response = session.get('http://example.com')
    except requests.exceptions.TooManyRedirects as e:
        print("Too many redirects:", e)


    # タイムアウトの設定
    r_timeout = requests.get('https://api.github.com/events', timeout=0.001)

    

if __name__ == "__main__":
    # test_requests()
    quick_start()