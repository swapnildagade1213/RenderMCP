
from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("Render-MCP")

@mcp.tool
def echo(text: str) -> str:
    return f"Echo: {text}"

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

# Outer FastAPI app
api = FastAPI()

@api.get("/")
def root():
    return {"ok": True}

@api.get("/health")
def health():
    return {"status": "ok"}

# Mount MCP explicitly
api.mount("/", mcp.http_app())

# ✅ THIS is what uvicorn serves
app = api
