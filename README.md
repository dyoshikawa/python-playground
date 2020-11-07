## テスト実行

```
pipenv shell
python src/**/test*.py
```

## Linter

```
pipenv run flake8 . --show-source
```

## 型チェック

```
pipenv run mypy .
```