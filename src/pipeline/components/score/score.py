import argparse
import json
from pathlib import Path
from pprint import pprint

import mlflow


def evaluate(
    inferences_json_file: str,
    aggregate_metrics_file: str,
    local_output_folder: Path = Path("outputs"),
):
    # Load the generations JSONL file
    inferences = []
    with open(inferences_json_file, "r") as file:
        for line in file:
            inferences.append(json.loads(line))
    pprint(inferences)

    print("Hello! In the evaluation step.")

    aggregate_metrics_calculations = {
        "f1": 0.5,
        "recall": 0.4,
        "precision": 0.6,
    }

    # example metrics logging with Mlfow
    mlflow.autolog()
    mlflow.log_param("temperature", 1.0)
    mlflow.log_metrics(aggregate_metrics_calculations)

    with open(local_output_folder / aggregate_metrics_file, "w") as file:
        json.dump(aggregate_metrics_calculations, file)
    print(f"Saved aggregate metrics to {local_output_folder}/{aggregate_metrics_file}")

    with open(aggregate_metrics_file, "w") as file:
        json.dump(aggregate_metrics_calculations, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inferences_json_file", type=str, required=True)
    parser.add_argument("--local_output_folder", type=Path, default=Path("outputs"))
    parser.add_argument("--aggregate_metrics_file", type=str)
    args = parser.parse_args()
    evaluate(
        inferences_json_file=args.inferences_json_file,
        local_output_folder=args.local_output_folder,
        aggregate_metrics_file=args.aggregate_metrics_file,
    )
