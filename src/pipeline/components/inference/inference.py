import argparse
import json
from pprint import pprint


def inference(
    evaluation_data_file: str,
    inferences_json_file: str,
):
    print("Hello! In the inference step.")

    # Load the evaluation data json file
    with open(evaluation_data_file, "r") as file:
        evaluation_data = json.load(file)
    pprint(evaluation_data)

    evaluation_inferences = []
    for data in evaluation_data:
        data["generated_answer"] = "Tokyo"
        evaluation_inferences.append(data)

    # output JSONL file
    with open(inferences_json_file, "w") as file:
        for inference in evaluation_inferences:
            file.write(json.dumps(inference) + "\n")
    print(f"Saved inferences to {inferences_json_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--evaluation_data_file", type=str, required=True)
    parser.add_argument("--inferences_file", type=str, required=True)
    args = parser.parse_args()
    inference(
        evaluation_data_file=args.evaluation_data_file,
        inferences_file=args.inferences_file,
    )
