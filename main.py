from fastmcp import FastMCP
from app.tools import register_tools

mcp = FastMCP(
    name="Render-MCP",
    description="MCP Server running on Render using fastmcp"
)

# Load your tools from your registry
tools = register_tools()

# Register tools dynamically
for t in tools:
    mcp.tool(
        name=t.tool.name,
        description=t.tool.description,
        parameters=t.tool.parameters
    )(t.handler)

# Start WebSocket MCP server
app = mcp.fastapi_app
