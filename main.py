# main.py
from fastmcp import FastMCP
from app.tools.functions import echo, add

mcp = FastMCP("Render-MCP")

@mcp.tool(
    name="echo",
    description="Echo text"
)
def echo_tool(text: str) -> str:
    return echo(text)

@mcp.tool(
    name="add",
    description="Add two numbers"
)
def add_tool(a: int, b: int) -> int:
    return add(a, b)

# Expose FastAPI app to Render
app = mcp.fastapi_app
