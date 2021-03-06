# linescraper

[![GitHub Super-Linter](https://github.com/haunt98/linescraper/workflows/Lint%20Code%20Base/badge.svg?branch=main)](https://github.com/marketplace/actions/super-linter)

For research purpose only.

## Require

- [requests](https://pypi.org/project/requests/)

## Guide

Example with [Peach Cat 4(JPN)](https://store.line.me/stickershop/product/8941816/en).

URL is `https://store.line.me/stickershop/product/8941816/en` so the ID is `8941816`.

Download sticker as zip:

```sh
python main.py 8941816
```

## Development

Use `venv`:

```sh
python3 -m venv venv
source ./venv/bin/activate
```

Install `requests`, `black`, `isort`:

```sh
python3 -m pip install requests black isort
```

After editing, formatting source codes:

```sh
black .
isort .
```
