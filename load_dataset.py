from datasets import load_dataset
import json

print("Loading dataset...")
dataset = load_dataset("dmarsili/Omni3D-Bench")
train = dataset["train"]

questions = []
for row in train:
    questions.append({
        "image_index":    row["image_index"],
        "question_index": row["q_index"],
        "question":       row["question"],
        "answer_type":    row["answer_type"],
        "answer":         row["answer"],
    })

with open("annotations.json", "w") as f:
    json.dump({"questions": questions}, f, indent=4)

print(f"Saved {len(questions)} entries to annotations.json")
