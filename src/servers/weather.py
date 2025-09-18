from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the weather for a given location.
    Args:
        location: The location to get the weather for.
    """
    return f"The weather in {location} is sunny."

if __name__ == "__main__":
    mcp.run()