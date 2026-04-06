# app/tools.py
from app.executor import AsyncToolExecutor, ToolInfo

def register_tools():
    executor = AsyncToolExecutor()

    return [
        ToolInfo(
            tool={
                "name": "echo",
                "description": "Echo text",
                "handler": lambda text: f"Echo: {text}",
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
                "handler": lambda a, b: a + b,
            },
            category="general",
            tags=["math"],
            version="1.0",
            author="system",
            visible=True
        )
    ]
