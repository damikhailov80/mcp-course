from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("LocalNotes")
file_path = Path(__file__).parent.parent / "notes.txt"

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Add user's note to the local file.
    Args:
        content: The content of the note to add.
    """

    try:
        with open(file_path, "a") as file:
            file.write(content + "\n")
        return f"Note added to local file"
    except Exception as e:
        return f"Error adding note to local file: {e}"

@mcp.tool()
def read_notes() -> str:
    """
    Read user's notes from the local file.
    """

    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        return f"Error reading notes from local file"

if __name__ == "__main__":
    mcp.run()