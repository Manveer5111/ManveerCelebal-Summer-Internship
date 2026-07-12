from tools import calculator_tool, keyword_tool, general_tool


def detect_intent(query):
    """
    Detects which tool should handle the query.
    """

    q = query.lower()

    if any(symbol in q for symbol in ["+", "-", "*", "/", "calculate"]):
        return "calculator"

    elif "keyword" in q or "keywords" in q:
        return "keyword"

    else:
        return "general"


def execute(state):
    """
    Routes the query to the appropriate tool.
    """

    state.intent = detect_intent(state.query)

    if state.intent == "calculator":
        state.response = calculator_tool(state.query)

    elif state.intent == "keyword":
        state.response = keyword_tool(state.query)

    else:
        state.response = general_tool(state.query)

    return state    