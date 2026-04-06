# app/tools.py
from app.executor import ToolInfo
from app.tools.functions import echo, add

def register_tools():
    return [
        ToolInfo(
            tool={
                "name": "echo",
                "description": "Echo text",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"}
                    },
                    "required": ["text"]
                }
            },
            category="general",
            tags=["debug"],
            version="1.0",
            author="system",
            visible=True
        ),
        ToolInfo(
            tool={
                "name": "add",
                "description": "Add two numbers",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"]
                }
            },
            category="general",
            tags=["math"],
            version="1.0",
            author="system",
            visible=True
        )
    ]
