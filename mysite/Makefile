all: typecheck run
	@echo "make all called"
#	lint typecheck test run

run:
	uv run manage.py runserver

lint:
	uv run ruff check .

format:
	uv run ruff format .

type:
	uv run mypy ./quiz/views.py

# TODO: テストライブラリとか調べる
test:
	uv run pytest

# ------------ 例なので実際には使わない ------------
target_name: 依存関係
	command_to_execute

ターゲット: 依存関係
	コマンド

main.o: main.c
	gcc -c main.c

program: main.o
	gcc main.o -o program
# ----------------------------------------------

.PHOONY: run type test lint format
