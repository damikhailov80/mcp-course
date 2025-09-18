from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import pyautogui
import tempfile

mcp = FastMCP("Screenshot")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture a screenshot of the current screen.
    Args:
        None
    """
    screenshot = pyautogui.screenshot()
    
    # Create a temporary file to save the screenshot
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        screenshot.save(temp_file.name, format="PNG")
        return Image(temp_file.name)

if __name__ == "__main__":
    mcp.run()