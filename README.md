# Vexoo Labs Assignment

## Part 1: Document System
- Uses sliding window chunking
- Builds a 4-layer knowledge pyramid
- Retrieves answers using similarity

## Run Part 1
cd part1_ingestion
python main.py

## Part 2: Model Training
- Simulated GSM8K dataset using local JSON
- Trained using distilgpt2

## Run Part 2
cd part2_gsm8k
python train.py

## Note
Due to API limits, a small local dataset was used to simulate GSM8K training.
