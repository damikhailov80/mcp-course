Test MCP servers.

Useful commands:
- uv init - to init repo
- uv venv - to create a new virtual enviroment
- uv run mcp dev servers/resources.py - run dev server
- uv run mcp install servers/resources.py - add server to claude
-  uvx --from git+https://github.com/damikhailov80/mcp-course.git mcp-server  - download and run from githgub repo


```json
{
  "mcpServers": {
    "Crypto": {
      "command": "/Users/denm/.local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/damikhailov80/mcp-course.git",
        "mcp-server"
      ]
    }
  }
```