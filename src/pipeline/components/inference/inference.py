import argparse
import json
from pprint import pprint


def inference(query: str) -> str:
    if query == "What is the capital of France?":
        return "Paris"
    elif query == "What is the capital of Germany?":
        return "Tokyo"  # bad model answer
    else:
        return "I don't know."


def run_inference(
    evaluation_data_file: str,
    inferences_json_file: str,
):
    print("Hello! In the inference step.")

    # Load the evaluation data JSONL file
    evaluation_data = []
    with open(evaluation_data_file, "r") as file:
        for line in file:
            evaluation_data.append(json.loads(line))
    pprint(evaluation_data)

    evaluation_inferences = []
    for data in evaluation_data:
        data["generated_answer"] = inference(query=data["query"])
        evaluation_inferences.append(data)

    # output JSONL file
    with open(inferences_json_file, "w") as file:
        for inference_result in evaluation_inferences:
            file.write(json.dumps(inference_result) + "\n")
    print(f"Saved inferences to {inferences_json_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--evaluation_data_file", type=str, required=True)
    parser.add_argument("--inferences_file", type=str, required=True)
    args = parser.parse_args()
    run_inference(
        evaluation_data_file=args.evaluation_data_file,
        inferences_file=args.inferences_file,
    )
