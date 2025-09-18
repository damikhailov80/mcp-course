"""MCP servers package."""

from .crypto import mcp as crypto_mcp
from .resources import mcp as resources_mcp
from .propt import mcp as propt_mcp
from .weather import mcp as weather_mcp
from .screenshot import mcp as screenshot_mcp
from .local import mcp as local_mcp

__all__ = [
    "crypto_mcp",
    "resources_mcp", 
    "propt_mcp",
    "weather_mcp",
    "screenshot_mcp",
    "local_mcp",
]
