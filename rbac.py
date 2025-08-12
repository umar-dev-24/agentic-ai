ROLE_TOOLS = {
    "user": ["research_agent", "analyse_agent", "summarize_agent"],
    "admin": ["research_agent", "analyse_agent", "summarize_agent", "db_agent"],
}


def get_tools_for_role(role, all_tools):
    allowed_tool_names = ROLE_TOOLS.get(role, [])
    permitted_tools = [
        tool for tool in all_tools if getattr(tool, "name", "") in allowed_tool_names
    ]
    return permitted_tools
