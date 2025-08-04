# tool.name should match the actual tool registered with the agent
# all_tools = [research_tool, swot_tool, summarize_tool, db_tool]
ROLE_TOOLS = {
    "user": ["research_agent", "analyse_agent", "summarize_agent"],
    "admin": ["research_agent", "analyse_agent", "summarize_agent", "db_agent"],
}
# agents = [research_agent, analyse_agent, summarize_agent, db_agent]


# def get_tools_for_role(role, all_tools):
#     allowed_tool_names = ROLE_TOOLS.get(role, [])
#     print(allowed_tool_names, "al")
#     print(all_tools, "all toole")
#     return [tool for tool in all_tools if tool.name in allowed_tool_names]
def get_tools_for_role(role, all_tools):
    allowed_tool_names = ROLE_TOOLS.get(role, [])
    print(allowed_tool_names, "al")
    for a in all_tools:
        print("name:", a.name)
    permitted_tools = [
        tool for tool in all_tools if getattr(tool, "name", "") in allowed_tool_names
    ]
    print("permiii", permitted_tools)
    return permitted_tools
