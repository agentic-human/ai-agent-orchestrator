import json
import re
from typing import List, Any
from crewai.tasks.task_output import TaskOutput

def clean_json_block(raw_str: str) -> str:
    """
    Strips markdown-style code fences from a raw string, if present.
    """
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw_str.strip())  # remove opening ```json
    cleaned = re.sub(r"\s*```$", "", cleaned)  # remove closing ```
    return cleaned.strip()


def parse_agent_specs_from_task_outputs(task_outputs: list[TaskOutput]) -> list[dict]:
    specs = []
    for idx, task_output in enumerate(task_outputs):
        raw_content = getattr(task_output, "raw", None)
        if not raw_content or not raw_content.strip():
            print(f"Warning: Task output {idx} has no 'raw' attribute or it's empty. Skipping.")
            continue
        
        # Clean the markdown wrapping
        cleaned_raw = clean_json_block(raw_content)
        
        try:
            data = json.loads(cleaned_raw)
            if isinstance(data, list):
                specs.extend(data)
            else:
                specs.append(data)
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON from task output {idx}: {e}")
            continue
    return specs


def parse_clean_json(raw_str: str):
    """
    Cleans a markdown-formatted JSON block and parses it into a Python object.
    Raises a JSONDecodeError if parsing fails.
    """
    cleaned_str = clean_json_block(raw_str)
    return json.loads(cleaned_str)
