# Djangoでのアプリ開発練習

## 目的
- [x] Djangoによるアプリケーション開発の手法を学ぶ
- [x] Pythonのpackage管理システム・仮想環境について学ぶ
- [x] Dockerによる環境構築手法を学ぶ
- [x] Pythonの型システムについて学ぶ
- [x] Pythonのテスト手法について学ぶ

## チュートリアル
[はじめてのDjango](https://docs.djangoproject.com/ja/5.0/intro/tutorial01/) </br>
djangoのチュートリアルサイトで投票アプリケーションを作成

## クイズアプリ
/quizでクイズができる

## uv
package管理ツールを今まで使っていたpoetryからuvへ

https://docs.astral.sh/uv/

```bash
uv init

uv add django-admin

# 仮想環境に入らずに実行
uv run program.py
uv run mysite/manage.py runserver

# 仮想環境に入る
source .venv/bin/activate

# 仮想環境出る
deactivate
```