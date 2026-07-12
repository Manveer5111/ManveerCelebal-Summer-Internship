import re


def calculator_tool(query):
    """
    Evaluates simple mathematical expressions.
    """

    expression = re.findall(r"[0-9+\-*/(). ]+", query)

    if not expression:
        return "No mathematical expression found."

    try:
        result = eval(expression[0])
        return f"Result: {result}"
    except Exception:
        return "Invalid mathematical expression."


def keyword_tool(query):
    """
    Extracts words longer than five characters.
    """

    words = query.split()

    keywords = [word.strip(".,!?") for word in words if len(word.strip(".,!?")) > 5]

    if keywords:
        return "Keywords: " + ", ".join(keywords)

    return "No keywords found."


def general_tool(query):
    """
    Default response.
    """

    return f"General Response: I received your query -> '{query}'"