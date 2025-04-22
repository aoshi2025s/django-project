all: typecheck run
	@echo "make all called"
#	lint typecheck test run

run:
	python manage.py runserver

# TODO: いい感じのlinter調べる
lint:
	flake8 or ruff?

typecheck:
	mypy quiz/*.py

# TODO: テストライブラリとか調べる
test:
	pytest

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

.PHOONY: run type test lint
