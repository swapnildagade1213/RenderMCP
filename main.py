from fastmcp import FastMCP
from app.tools import register_tools

# Create MCP instance – only name is allowed now
mcp = FastMCP("Render-MCP")

# Load tools
tools = register_tools()

# Register tools into fastmcp
for t in tools:
    mcp.tool(
        name=t.tool.name,
        description=t.tool.description,
        parameters=t.tool.parameters
    )(t.handler)

# Expose FastAPI app to Render
app = mcp.fastapi_app
