# main.py

from fastmcp import FastMCP
from app.tools import echo, add

# Create MCP server
mcp = FastMCP("Render-MCP")

# Register tools (FastMCP-native way)
mcp.tool(
    name="echo",
    description="Echo text back to the caller",
)(echo)

mcp.tool(
    name="add",
    description="Add two numbers",
)(add)

# Expose FastAPI app for Render
app = mcp.fastapi_app
