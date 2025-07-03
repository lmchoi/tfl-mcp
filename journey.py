from typing import Any
import httpx
from fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()

TFL_API_BASE = "https://api.tfl.gov.uk"
TFL_JOURNEY_OPEN_API_SPEC = "https://api.tfl.gov.uk/swagger/docs/v1"
USER_AGENT = "tfl-agent-app/1.0"
APP_KEY = os.environ["TFL_API_KEY"]

openapi_spec = httpx.get(TFL_JOURNEY_OPEN_API_SPEC).json()

headers = {
    "app_key": APP_KEY,
}

client = httpx.AsyncClient(
    base_url=TFL_API_BASE, 
    headers=headers
)

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="TFL Journey Server"
)

if __name__ == "__main__":
    mcp.run()
