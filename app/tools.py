# app/tools.py
from app.executor import AsyncToolExecutor, ToolInfo

def register_tools():
    executor = AsyncToolExecutor()

    # Example tool definitions
    return [
        ToolInfo.from_handler(
            name="echo",
            description="Echo text",
            handler=lambda text: f"Echo: {text}"
        ),
        ToolInfo.from_handler(
            name="add",
            description="Add two numbers",
            handler=lambda a, b: a + b
        )
    ]
