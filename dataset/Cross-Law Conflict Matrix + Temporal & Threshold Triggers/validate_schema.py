import json

crosslaw_path = "/opt/anaconda3/TCS-Finetuning-Ministral-Reasoning-2512/CrossLaw_dataset.jsonl"
triggers_path = "/opt/anaconda3/TCS-Finetuning-Ministral-Reasoning-2512/Triggers_dataset.jsonl"

def validate(fpath, expected_count):
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        
    if len(lines) < expected_count:
        print(f"ERROR: {fpath} has {len(lines)} lines, minimum expected {expected_count}")
        return False
        
    for i, line in enumerate(lines):
        try:
            data = json.loads(line)
            required_keys = {"instruction", "input", "output", "metadata"}
            if not required_keys.issubset(data.keys()):
                print(f"ERROR in {fpath} line {i+1}: Missing keys. Found {data.keys()}")
                return False
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error in {fpath} line {i+1}: {e}")
            return False
            
    print(f"SUCCESS: {fpath} passed validation. {len(lines)} total valid JSON lines.")
    return True

v1 = validate(crosslaw_path, 45)
v2 = validate(triggers_path, 20)
if v1 and v2:
    print("ALL VALIDATION PASSED!")
else:
    print("VALIDATION FAILED")
