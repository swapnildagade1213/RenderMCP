# app/executor.py

class AsyncToolExecutor:
    async def execute(self, tool_name, params):
        handler = self.handlers.get(tool_name)
        return await handler(**params)

    def register(self, name, handler):
        if not hasattr(self, "handlers"):
            self.handlers = {}
        self.handlers[name] = handler


class ToolInfo:
    def __init__(self, tool, category="general", tags=None, version="1.0", author="", visible=True):
        self.tool = tool
        self.category = category
        self.tags = tags or []
        self.version = version
        self.author = author
        self.visible = visible
