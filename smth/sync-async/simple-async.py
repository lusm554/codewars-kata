import asyncio
import time

async def f1(x):
    print(x**2)
    await asyncio.sleep(3)
    print("f1 done")

async def f2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print("f2 done")

async def main():
    x = 4
    task1 = asyncio.create_task(f1(x))
    task2 = asyncio.create_task(f2(x))

    await task1
    await task2


print("Start", time.strftime("%X"))
asyncio.run(main())
print("End", time.strftime("%X"))

