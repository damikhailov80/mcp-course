from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Crypto")

@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Get the price of a given cryptocurrency.
    Args:
        crypto: The cryptocurrency to get the price of.
    """

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": crypto.lower(),
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        data = response.json()
        if crypto.lower() not in data:
            return f"The cryptocurrency {crypto} is not found"
        return f"The price of {crypto} is {data[crypto]['usd']}"
    except Exception as e:
        return f"Error getting the price of {crypto}: {e}"

if __name__ == "__main__":
    mcp.run()