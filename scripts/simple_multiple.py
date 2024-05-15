import json
import subprocess

if __name__ == "__main__":
    input_models_path = "./car_model_paths.json"

    # Add items to the queue
    with open(input_models_path, "r") as f:
        model_paths = json.load(f)
    for item in model_paths:
        command = (
            f"python scripts/blender_script.py --object_path={item}"
        )
        subprocess.run(command, shell=True)