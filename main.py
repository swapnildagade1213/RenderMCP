from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("Render-MCP")

@mcp.tool
def echo(text: str) -> str:
    return f"Echo: {text}"

api = FastAPI()

@api.get("/health")
def health():
    return {"status": "ok"}

# ✅ Mount MCP explicitly
api.mount("/", mcp.http_app())

app = api
