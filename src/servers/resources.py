from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Return an overview of the inventory.
    Args:
        None
    """

    overview = """
    Inventory Overview:
    - Coffee
    - Tea
    - Water
    - Milk
    - Cookies
    """

    return overview.strip()

if __name__ == "__main__":
    mcp.run()