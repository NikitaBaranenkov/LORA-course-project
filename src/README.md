# Source Code

Каталог зарезервирован для переиспользуемых модулей проекта: подготовки данных,
общих метрик, обучения и оценки моделей. Реализация нейросетевого эксперимента
пока сохранена в ноутбуке без преждевременного рефакторинга.

Файл `constants.py` фиксирует общие для сравнимых экспериментов значения:
датасет, базовые модели DistilBERT и BERT, seed, `max_length`, основную
метрику, label mapping и стандартные пути данных/таблиц.

Из ноутбука, запускаемого из корня репозитория, константы можно импортировать
так:

```python
from src.constants import (
    BASE_MODEL_BERT,
    BASE_MODEL_DISTILBERT,
    MAX_LENGTH,
    SEED,
    TRAIN_CSV_PATH,
    VALIDATION_CSV_PATH,
    TEST_CSV_PATH,
    id2label,
    label2id,
)
```
