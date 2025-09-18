from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Prompt")

@mcp.prompt()
def get_research_prompt(topic: str) -> str:
    """
    Get a research prompt for a given topic.
    Args:
        topic: The topic to get a research prompt for.
    """

    return f"Do a detailed research on {topic}"

@mcp.prompt()
def get_summary_prompt(topic: str, amount_of_words: int = 30) -> str:
    """
    Get a summary prompt for a given topic.
    Args:
        topic: The topic to get a summary prompt for.
        amount_of_words: The amount of words to summarize the research on.
    """
    return f"Summarize the research on {topic} in {amount_of_words} words"

if __name__ == "__main__":
    mcp.run()