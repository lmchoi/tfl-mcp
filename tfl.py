from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("tfl")

# Constants
TFL_API_BASE = "https://api.tfl.gov.uk"
USER_AGENT = "tfl-agent-app/1.0"
APP_KEY = os.environ["TFL_API_KEY"]

async def make_tfl_request(url: str) -> dict[str, Any] | None:
    """Make a request to the TFL API."""
    headers = {
        "User-Agent": USER_AGENT,
        "Cache-Control": "no-cache",
        "app_key": APP_KEY,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        
def format_yellow_message(message: dict) -> str:
    return f"""
Headline: {message.get("headline", "Unknown")}
"""

@mcp.tool()
async def get_yellow_banner_messages() -> str:
    """Get TFL yellow banner messages"""
    url = f"{TFL_API_BASE}/status/yellowbannermessages"
    data = await make_tfl_request(url)

    if not data or "messages" not in data:
        return "Unable to fetch yellow banner messages or none found."

    yellow_banners = [format_yellow_message(message) for message in data["messages"]]
    return "\n---\n".join(yellow_banners)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
