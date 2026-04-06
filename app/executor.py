# app/executor.py

TOOL_HANDLERS = {
    "echo": echo,
    "add": add,
}


def execute(tool_name: str, args: dict):
    return TOOL_HANDLERS[tool_name](**args)
