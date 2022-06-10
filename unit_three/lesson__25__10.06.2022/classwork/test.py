import asyncio

async def task1():
    print("Задача 1 старт")
    await asyncio.sleep(1)
    print("Задача 1 финиш")

async def task2():
    print("Задача 2 старт")
    await asyncio.sleep(3)
    print("Задача 2 финиш")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())


