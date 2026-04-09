import json
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# Load local dataset
with open("data.json", "r") as f:
    data = json.load(f)

# Convert to format
texts = [item["question"] + " Answer: " + item["answer"] for item in data]

# Model
model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# Tokenize
encodings = tokenizer(texts, truncation=True, padding=True, return_tensors="pt")

class Dataset:
    def __init__(self, encodings):
        self.encodings = encodings

    def __len__(self):
        return len(self.encodings["input_ids"])

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        
        # ✅ ADD THIS LINE
        item["labels"] = item["input_ids"]

        return item


train_dataset = Dataset(encodings)

# Training setup
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    logging_steps=1,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

trainer.train()

# Test output
input_text = "If I have 3 apples and get 2 more, how many?"
inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**inputs, max_length=30,do_sample=True,
    temperature=0.7)
print("\nModel Output:")
print(tokenizer.decode(outputs[0]))
