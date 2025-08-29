freeze:
	uv pip freeze > requirements.txt

install:
	uv pip install -r requirements.txt

run:
	uv run main.py