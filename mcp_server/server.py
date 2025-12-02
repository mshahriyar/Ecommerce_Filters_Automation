from mcp.server import Server
from mcp.types import Tool, ToolResult
import json
import os
from tools.create_pom import create_pom_class
from tools.generate_filter_tests import generate_filter_test
from tools.fix_locators import fix_locators

server = Server("qa-mcp-server")

# --- Register Tools ---

@server.tool(
    name="generate_filters_test",
    description="Generate a new filter test file for any category (e.g., Electronics, Real Estate)."
)
def generate_filters_test(category: str):
    return ToolResult(
        content=generate_filter_test(category),
        mime_type="text/plain"
    )


@server.tool(
    name="create_pom_page",
    description="Create a new Page Object Model class for a category."
)
def create_pom_page(name: str, fields: str):
    fields = json.loads(fields)
    return ToolResult(
        content=create_pom_class(name, fields),
        mime_type="text/plain"
    )


@server.tool(
    name="fix_broken_locators",
    description="Analyze failing locators and propose fixed versions."
)
def fix_broken_locators(failure_log: str):
    return ToolResult(
        content=fix_locators(failure_log),
        mime_type="text/plain"
    )


if __name__ == "__main__":
    server.start()
