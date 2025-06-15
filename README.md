# Agent Development Kit (ADK) Samples
This repository contains a collection of samples that demonstrate how to use the Google Agent Development Kit (ADK) to build agents and multi-agent systems.

# FIRST THINGS FIRST
Install following dependencies to run this project:

```shell
# Create a virtual environment
uv venv

# Install dependencies
uv pip install -r requirements-<CHANGE THIS TO MATCH YOUR OS>.txt
```

If you don't have `uv` installed, you can install it using: [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

Then...

When you run an agent, the ADK needs to know who is requesting the model API calls. You can provide this information in one of two ways. 

You can do one of the following and update the `.env` file in the root of this project:

1. Provide a Gemini API key. [Get your free API key](https://aistudio.google.com/apikey)
2. Authenticate your environment with Google Cloud credentials and associate your model API calls with a Vertex AI project and location.


# HINT
- Search for `#TODO` in the code to find the places where you need to update get this to work.

- Search for `#NOTE` in the code to find where I have added notes for you to understand the code better.


# How to run the Agents created in this project:

```shell

# METHOD 1: Run using ADK Dev UI
adk web # default port is 8000
adk web --port 8001 # to run with a different port

# METHOD 2: Run an agent programmatically
python3 app_agent/agent.py

# METHOD 3: Chat with an agent via the command-line interface
adk run my_google_search_agent

```

# Inventory of Agents in this project:

**google_search_agent**
- This agent is designed to interact with Google Search and Google GenAI using "google_search" tool.


**app_agent**
- This agent is designed to interact with Google Search and Google GenAI. 
- It can handle queries, log responses, and manage events.
- You can define an output schema for the agent, which allows you to specify the expected structure of the responses.
- Use Pydantic schema classes to define the output schema.
- When you define an output schema, you cannot use tools or agent transfers.


**llm_auditor**: 
- This agent is responsible for auditing the responses from the LLM. It uses sub-agents like critic and reviser to evaluate and improve the quality of the responses.
- critic  : This sub-agent evaluates the responses from the LLM and provides feedback.
- reviser : This sub-agent revises the responses based on the feedback provided by the critic sub-agent.
- Even though this agent uses a SequentialAgent workflow agent, you can think of this pattern as a human-in-the-loop pattern. When the SequentialAgent ends its sequence, the conversation goes back to its parent, the llm_auditor in this example, to get a new input turn from the user and then pass the conversation back around to the other agents.
