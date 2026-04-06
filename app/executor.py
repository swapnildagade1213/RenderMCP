
# app/executor.py

from app.tools.functions import echo, add

TOOL_HANDLERS = {
    "echo": echo,
    "add": add,
}

def execute(tool_name: str, args: dict):
    if tool_name not in TOOL_HANDLERS:
        raise ValueError(f"Unknown tool: {tool_name}")

    return TOOL_HANDLERS[tool_name](**args)
