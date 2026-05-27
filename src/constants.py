"""Shared constants for reproducible financial sentiment experiments."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATASET_NAME = "zeroshot/twitter-financial-news-sentiment"
BASE_MODEL_DISTILBERT = "distilbert-base-uncased"
BASE_MODEL_BERT = "bert-base-uncased"

SEED = 42
MAX_LENGTH = 128
SELECTION_METRIC = "macro_f1"
FINAL_TEST_EVALUATION_ONLY = True

DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
TRAIN_CSV_PATH = PROCESSED_DATA_DIR / "train.csv"
VALIDATION_CSV_PATH = PROCESSED_DATA_DIR / "validation.csv"
TEST_CSV_PATH = PROCESSED_DATA_DIR / "test.csv"
REPORTS_TABLES_DIR = PROJECT_ROOT / "reports" / "tables"

id2label = {
    0: "Bearish",
    1: "Bullish",
    2: "Neutral",
}
label2id = {label: class_id for class_id, label in id2label.items()}


__all__ = [
    "BASE_MODEL_BERT",
    "BASE_MODEL_DISTILBERT",
    "DATASET_NAME",
    "DATA_DIR",
    "FINAL_TEST_EVALUATION_ONLY",
    "MAX_LENGTH",
    "PROCESSED_DATA_DIR",
    "PROJECT_ROOT",
    "REPORTS_TABLES_DIR",
    "SEED",
    "SELECTION_METRIC",
    "TEST_CSV_PATH",
    "TRAIN_CSV_PATH",
    "VALIDATION_CSV_PATH",
    "id2label",
    "label2id",
]
