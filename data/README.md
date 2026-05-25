# Data

Основной датасет проекта: Hugging Face
[`zeroshot/twitter-financial-news-sentiment`](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment).
Тексты размечены тремя классами: `0` = Bearish, `1` = Bullish,
`2` = Neutral.

## Принятая схема разбиения

Аудит данных зафиксирован в `../legacy/chatgpt_data_audit_context.md`.
Используемая стратегия:

1. Официальный split `validation` используется как финальный `test`.
2. Из исходного `train` удаляются пересечения с test и дубликаты
   нормализованных текстов.
3. Из очищенного train стратифицированно выделяется validation.

| Split | Rows |
| --- | ---: |
| train | 8,105 |
| validation | 1,431 |
| test | 2,388 |

## Локальные файлы

Подготовленные данные для ноутбуков размещаются локально так:

```text
data/
└── processed/
    ├── train.csv
    ├── validation.csv
    └── test.csv
```

Каждый CSV должен как минимум содержать столбцы `text`, `label` и
`label_name`. Файлы данных не коммитятся: каталог `data/processed/` добавлен в
`.gitignore`, чтобы не раздувать репозиторий и не дублировать источник данных.
