class AgentState:
    """
    Stores the state of the agent throughout the pipeline.
    """

    def __init__(self, query):
        self.query = query
        self.intent = None
        self.response = None