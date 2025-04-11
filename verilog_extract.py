import json

# Define parameters for splitting the code
CONTEXT_LINES = 20  # Number of lines to use as context (prompt)
COMPLETION_LINES = 5  # Number of lines to predict (completion)

# Read the list of Verilog files
with open("verilog_files.txt", "r") as f:
    files = [line.strip() for line in f.readlines()]

dataset = []
for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Generate context-completion pairs using a sliding window
        for i in range(len(lines) - CONTEXT_LINES - COMPLETION_LINES):
            prompt = "".join(lines[i : i + CONTEXT_LINES]).strip()
            completion = "".join(lines[i + CONTEXT_LINES : i + CONTEXT_LINES + COMPLETION_LINES]).strip()

            if prompt and completion:
                dataset.append({
                    "messages": [
                        {"role": "user", "content": f"{prompt}"},
                        {"role": "assistant", "content": f"{completion}"}
                    ]
                })

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Save dataset to JSONL file
output_file = "verilog_autocomplete.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for entry in dataset:
        f.write(json.dumps(entry) + "\n")

print(f"Autocomplete dataset saved to {output_file}")