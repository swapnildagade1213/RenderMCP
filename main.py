from fastmcp import FastMCP
from app.tools import register_tools

# Create MCP instance – only name is allowed now
mcp = FastMCP("Render-MCP")

# Load tools
tools = register_tools()

# Register tools into fastmcp
for t in tools:
    tool_kwargs = {
        "name": t.tool["name"],
        "description": t.tool.get("description", "")
    }

    if "parameters" in t.tool:
        tool_kwargs["parameters"] = t.tool["parameters"]

    mcp.tool(**tool_kwargs)(t.handler)

# Expose FastAPI app to Render
app = mcp.fastapi_app
