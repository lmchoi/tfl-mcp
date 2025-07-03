from typing import Any
import httpx
from fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()

# Constants
TFL_API_BASE = "https://api.tfl.gov.uk"
# TFL_JOURNEY_OPEN_API_SPEC = "https://api-portal.tfl.gov.uk/developer/apis/Journey?export=true&api-version=2022-04-01-preview"
TFL_JOURNEY_OPEN_API_SPEC = "https://api.tfl.gov.uk/swagger/docs/v1"
USER_AGENT = "tfl-agent-app/1.0"

APP_KEY = os.environ["TFL_API_KEY"]

headers = {
    # "User-Agent": "Mozilla/5.0",
    # "Accept": "application/json",
    "app_key": APP_KEY,
}

# Create an HTTP client for your API
client = httpx.AsyncClient(base_url=TFL_API_BASE)

# print(headers)
# spec_content_2_0 = httpx.get(TFL_JOURNEY_OPEN_API_SPEC, headers=headers, follow_redirects=True).text
# print(spec_content_2_0)

# curl 'https://api-portal.tfl.gov.uk/developer/apis/Journey?export=true^&api-version=2022-04-01-preview' \
#   -H 'User-Agent: Mozilla/5.0' \
#   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
#   -H 'Accept-Language: en-GB,en;q=0.5' \
#   -H 'Accept-Encoding: gzip, deflate, br, zstd' \
#   -H 'Upgrade-Insecure-Requests: 1' \
#   -H 'Sec-Fetch-Dest: document' \
#   -H 'Sec-Fetch-Mode: navigate' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: _cfuvid=kRwvThIpHxyRsN9FWy8cCk5NjbopgTnQLgwKRzd0eqI-1751206661674-0.0.1.1-604800000; returnUrl=/; auth=s%3Ae%3A486dea26f1660982b9faf18a499a1dbe%3A14cd00c798b7db43ddb3df933252c01fb273df5a1169cf6d1914d687268ae6ba533f2deea74cc8f54341c286f8539f29b0e1d6c89dace63019ca0e06bcf850b53a4f8b8eef99086a06e81379d68663cf4efc4aa6b5e8f2f6245ef814e06db95fedd7e76c861da4eece921f5c1757df2397dd252543f38157486ff1df32e37a2bdf6257f1fbde9f89b12975f8ef699e35.4OYptb6cHJgNYHMln2MN79MbTWUS8pjHuJhjGE5OnsA'
# Load your OpenAPI spec 
openapi_spec = httpx.get(TFL_JOURNEY_OPEN_API_SPEC).json()

# Create the MCP server
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="TFL Journey Server"
)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()
    # mcp.run(transport="stdio")



# async def make_tfl_request(url: str) -> dict[str, Any] | None:
#     """Make a request to the TFL API."""
#     headers = {
#         "User-Agent": USER_AGENT,
#         "Cache-Control": "no-cache",
#         "app_key": APP_KEY,
#     }

#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers, timeout=30.0)
#             response.raise_for_status()
#             return response.json()
#         except Exception:
#             return None
        
# def format_yellow_message(message: dict) -> str:
#     return f"""
# Headline: {message.get("headline", "Unknown")}
# """

# @mcp.tool()
# async def get_yellow_banner_messages() -> str:
#     """Get TFL yellow banner messages"""
#     url = f"{TFL_API_BASE}/status/yellowbannermessages"
#     data = await make_tfl_request(url)

#     if not data or "messages" not in data:
#         return "Unable to fetch yellow banner messages or none found."

#     yellow_banners = [format_yellow_message(message) for message in data["messages"]]
#     return "\n---\n".join(yellow_banners)

