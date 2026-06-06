from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    raw_data_dir: Path
    status_file: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    transformed_data_path: Path


@dataclass(frozen=True)
class FeatureEngineeringConfig:
    root_dir: Path
    feature_data_path: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    sarima_model_path: Path
    lightgbm_model_path: Path


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    metric_file_name: Path


@dataclass(frozen=True)
class PredictionConfig:
    root_dir: Path
    prediction_file: Path