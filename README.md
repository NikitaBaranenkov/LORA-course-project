# Full Fine-Tuning vs LoRA for Financial Sentiment Classification

Курсовой ML-проект посвящён сравнению полного дообучения (`full fine-tuning`) и
параметрически эффективного дообучения LoRA для языковых моделей на задаче
классификации тональности финансовых текстов.

**Исследовательский вопрос:** может ли LoRA дать качество, сопоставимое с полным
дообучением на financial sentiment classification, при существенно меньшем числе
обучаемых параметров и меньших требованиях к ресурсам?

## Текущее состояние

В репозитории сохранены уже полученные результаты классического baseline
`TF-IDF + Logistic Regression` и экспериментальный ноутбук для
`DistilBERT` full fine-tuning. Файл ноутбука ранее имел имя, указывающее на LoRA,
но его код и заголовок реализуют именно полное дообучение, поэтому он размещён
как `distilbert_full_finetuning.ipynb`.

## Структура репозитория

```text
.
├── README.md
├── requirements.txt
├── configs/                         # конфигурации будущих воспроизводимых запусков
├── data/
│   └── README.md                    # источник данных, схема и правила хранения
├── artifacts/
│   └── README.md                    # локальные модели/checkpoints, не для Git
├── notebooks/
│   └── experiments/
│       └── distilbert_full_finetuning.ipynb
├── reports/
│   ├── figures/                     # графики для анализа и курсовой
│   └── tables/
│       └── baseline/                # уже полученные baseline-метрики
├── src/                             # переиспользуемый Python-код по мере выделения
└── legacy/
    └── chatgpt_data_audit_context.md
```

## Данные

Используется датасет Hugging Face
[`zeroshot/twitter-financial-news-sentiment`](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment).
Целевые метки:

| Label | Class |
| ---: | --- |
| 0 | Bearish |
| 1 | Bullish |
| 2 | Neutral |

По выполненному аудиту официальный `validation` split используется как финальный
test set, а validation для выбора модели формируется стратифицированно из
исходного train после устранения пересечений и нормализованных дубликатов:

| Split | Rows |
| --- | ---: |
| train | 8,105 |
| validation | 1,431 |
| test | 2,388 |

Подробный сохранённый отчёт аудита находится в
[`legacy/chatgpt_data_audit_context.md`](legacy/chatgpt_data_audit_context.md).
Локальные подготовленные CSV следует хранить как `data/processed/train.csv`,
`data/processed/validation.csv` и `data/processed/test.csv`; они исключены из Git.

## План экспериментов

Основные сравниваемые режимы должны использовать одинаковые split, label mapping
и сопоставимые метрики (`accuracy`, `macro F1`, `weighted F1`):

| Model | Full fine-tuning | LoRA |
| --- | --- | --- |
| DistilBERT | ноутбук сохранён | запланировано |
| BERT | запланировано | запланировано |
| FLAN-T5-base | запланировано | запланировано |

Существующий `TF-IDF + Logistic Regression` служит классическим baseline.
Для итогового сравнения также следует фиксировать время обучения, общее и
обучаемое число параметров, гиперпараметры и seed.

## Установка

Из корня репозитория:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Для GPU-экспериментов установку `torch` при необходимости следует адаптировать
к версии CUDA используемого окружения.

## Запуск экспериментов

Текущий доступный neural experiment запускается из корня проекта в Jupyter:

```bash
jupyter lab
```

Откройте `notebooks/experiments/distilbert_full_finetuning.ipynb`. Перед
выполнением обучающих ячеек подготовьте три split-файла в `data/processed/`.
Ноутбук содержит полноценное обучение модели и рассчитан на среду с GPU; этот
запуск не является лёгкой проверкой.

По мере появления повторно используемых пайплайнов их следует переносить в
`src/`, а значения гиперпараметров - в `configs/`, оставляя ноутбукам анализ и
визуализацию результатов.

## Результаты и артефакты

- Уже сохранённые baseline-таблицы находятся в `reports/tables/baseline/`.
- Ноутбук DistilBERT записывает новые CSV-метрики в
  `reports/tables/distilbert_full_ft/`.
- Графики для отчёта следует сохранять в `reports/figures/`.
- Checkpoints и сохраненная модель DistilBERT записываются в
  `artifacts/distilbert_full_ft/` и не должны коммититься.

Большие датасеты, веса моделей, checkpoints и логи экспериментов исключены
правилами `.gitignore`.
