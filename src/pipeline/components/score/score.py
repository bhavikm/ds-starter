import argparse
import json
from pathlib import Path
from pprint import pprint
from typing import Optional

import mlflow


def evaluate(
    inferences_json_file: str,
    aml_aggregate_metrics_file_output_path: Optional[str] = None,
    local_output_folder: Path = Path("outputs"),
):
    print("Hello! In the evaluation step.")

    # Load the generations JSONL file
    inferences = []
    with open(inferences_json_file, "r") as file:
        for line in file:
            inferences.append(json.loads(line))
    print("Inferences loaded:")
    pprint(inferences)

    # calculate metrics
    correct_answers = 0
    total_answers = 0
    for inference in inferences:
        total_answers += 1
        if inference["generated_answer"] == inference["expected_answer"]:
            correct_answers += 1
    accuracy = correct_answers / total_answers if total_answers > 0 else 0.0
    print(f"Accuracy: {accuracy}")
    aggregate_metrics_calculations = {
        "accuracy": accuracy,
        "total_answers": total_answers,
        "correct_answers": correct_answers,
    }

    # example metrics logging with Mlfow
    mlflow.autolog()
    mlflow.log_param("model_temperature", 1.0)  # log som experiment parameter
    mlflow.log_metrics(aggregate_metrics_calculations)

    # Save the metrics JSON and inferences file locally
    with open(local_output_folder / "aggregate_metrics.json", "w") as file:
        json.dump(aggregate_metrics_calculations, file)
    with open(local_output_folder / "inferences.jsonl", "w") as file:
        for inference_result in inferences:
            file.write(json.dumps(inference_result) + "\n")
    print(f"Saved aggregate metrics and inferences to {local_output_folder}")

    # Save the metrics file the AML job output path
    if aml_aggregate_metrics_file_output_path:
        with open(aml_aggregate_metrics_file_output_path, "w") as file:
            json.dump(aggregate_metrics_calculations, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inferences_json_file", type=str, required=True)
    parser.add_argument("--local_output_folder", type=Path, default=Path("outputs"))
    parser.add_argument("--aggregate_metrics_file", type=str)
    args = parser.parse_args()
    evaluate(
        inferences_json_file=args.inferences_json_file,
        aml_aggregate_metrics_file_output_path=args.aggregate_metrics_file,
        local_output_folder=args.local_output_folder,
    )
