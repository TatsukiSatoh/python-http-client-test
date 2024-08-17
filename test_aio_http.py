import aiohttp
import asyncio

async def test_aiohttp():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts/1') as response:
            json_response = await response.json()
            print(f"aiohttp: {json_response}")

def main():
    asyncio.run(test_aiohttp())

if __name__ == "__main__":
    main()