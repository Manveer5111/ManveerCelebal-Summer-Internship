from state import AgentState
from router import execute


def main():
    print("=" * 50)
    print("      Smart Query Router Agent")
    print("=" * 50)

    query = input("\nEnter your query: ")

    state = AgentState(query)

    state = execute(state)

    print("\n----- Pipeline Result -----")
    print(f"Detected Intent : {state.intent}")
    print(f"Response        : {state.response}")


if __name__ == "__main__":
    main()