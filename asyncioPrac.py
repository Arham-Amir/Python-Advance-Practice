import asyncio

async def fetchData(delay):
    print("Fetching Data...")
    await asyncio.sleep(delay)
    print("Data Fetched")
    return {"data": "Some data"}

async def main():
    print("Hemloo G")
    
    t1 = asyncio.create_task(fetchData(2))
    t2 = asyncio.create_task(fetchData(3))
    t3 = asyncio.create_task(fetchData(1))
    
    r1 = await t1
    r2 = await t2
    r3 = await t3
    
    print(f"Received Result: {r1}")
    
asyncio.run(main())