import asyncio

async def fetchData(delay):
    print("Fetching Data...")
    await asyncio.sleep(delay)
    print("Data Fetched")
    return {"data": "Some data"}

async def main():
    print("Hemloo G")
    
    t1 = await asyncio.gather(fetchData(2), fetchData(3), fetchData(1))
    
    print(f"Received Result: {t1}")
    
asyncio.run(main())