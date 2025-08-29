import redis

# Подключение (по умолчанию localhost:6379)
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# -- Ключ-значение (строки)
# Записать
r.set(name="firstKey", value="Hello")
r.set(name="secondKey", value="World")

# Получить
print(r.get("firstKey"))  # Hello
print(r.get("secondKey"))  # World

# Проверка существования
print(r.exists("firstKey"))  # 1 или 0

# Удалить
r.delete("firstKey")


# -- Счётчики
r.set("counter", 0)
r.incr("counter")  # +1
r.decr("counter")  # -1
print(r.get("counter"))  # 0


# -- Списки (list)
# Добавление
r.rpush("mylist", "one", "two", "three")
r.lpush("mylist", "zero")

# Получение диапазона
print(r.lrange("mylist", 0, -1))  # ['zero', 'one', 'two', 'three']

# Извлечение элемента
print(r.lpop("mylist"))  # zero


# --Множества (set)
r.sadd("tags", "python", "fastapi", "redis")
print(r.smembers("tags"))  # {'python', 'fastapi', 'redis'}
print(r.sismember("tags", "go"))  # False
r.srem("tags", "fastapi")


# -- Хэши (hash)
r.hset("user:1", mapping={"name": "Ruslan", "age": "29"})
print(r.hget("user:1", "name"))  # Ruslan
print(r.hgetall("user:1"))  # {'name': 'Ruslan', 'age': '29'}


# -- Время жизни ключа
r.set("tempKey", "will expire", ex=10)  # TTL 10 секунд
print(r.ttl("tempKey"))


# -- Работа с ключами
print(r.keys("*"))  # все ключи
print(r.keys("user:*"))  # выборка по шаблону
