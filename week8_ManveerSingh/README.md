# Smart Query Router Agent

## Project Overview

This project demonstrates a simple Agentic AI pipeline using a single-agent architecture.

The system:

- Accepts a user query.
- Detects the query's intent.
- Routes the query to the appropriate tool.
- Returns the generated response.

---

## Tools Included

1. Calculator Tool
   - Solves simple mathematical expressions.

2. Keyword Extraction Tool
   - Extracts words longer than five characters.

3. General Response Tool
   - Handles all remaining queries.

---

## Project Structure

agent_pipeline/

├── main.py

├── router.py

├── tools.py

├── state.py

└── README.md

---

## Run

```bash
python main.py