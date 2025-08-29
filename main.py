"""Main module."""

# -- Imports

import asyncio
from settings import rediska

# --


async def main():

    # Set and Get
    await rediska.set(name="firstKey", value="Hello")
    first_key = await rediska.get("firstKey")
    print(first_key)  # 'Hello'

    # Удаление ключа
    await rediska.delete("firstKey")
    first_key = await rediska.get("firstKey")
    print(first_key)  # None

    # Работа со списками
    await rediska.rpush("mylist", "one", "two", "three")
    values = await rediska.lrange(name="mylist", start=0, end=-1)
    print(values)  # ['one', 'two', 'three']

    # Работа с множествами
    await rediska.sadd("myset", "a", "b", "c")
    members = await rediska.smembers("myset")
    print(members)  # {'a', 'b', 'c'}

    # Работа с хэшами
    await rediska.hset("myhash", mapping={"field1": "value1", "field2": "value2"})
    hash_values = await rediska.hgetall("myhash")
    print(hash_values)  # {'field1': 'value1', 'field2': 'value2'}

    # Очистка базы
    await rediska.flushdb()


if __name__ == "__main__":
    asyncio.run(main())
