from fastmcp import FastMCP
from app.tools import echo, add

mcp = FastMCP("Render-MCP")

@mcp.tool(
    name="echo",
    description="Echo text back to the caller",
)
def echo_tool(text: str) -> str:
    return echo(text)

@mcp.tool(
    name="add",
    description="Add two numbers",
)
def add_tool(a: int, b: int) -> int:
    return add(a, b)

# ✅ ONLY correct ASGI export across versions
app = mcp.http_app()
