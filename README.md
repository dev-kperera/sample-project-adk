<!-- @format -->

# 🚀 Agent Development Kit (ADK) Samples

Welcome to the Agent Development Kit (ADK) Samples repository! This collection of samples is designed to help you get started with building your own agents and multi-agent systems using the Google Agent Development Kit (ADK).

Whether you're a seasoned developer or just starting, these examples provide a hands-on approach to learning the ADK.

## 🤖 Agent Inventory

This project includes the following agents:

Sure! Here's your markdown table converted into a numbered list:

1. **google\_search\_agent**
   An agent designed to interact with Google Search and Google GenAI using the "google\_search" tool.

2. **app\_agent**
   This agent interacts with Google Search and Google GenAI, handles queries, logs responses, and manages events. It uses a Pydantic schema to define the output structure, which means it cannot use tools or agent transfers.

3. **llm\_auditor**
   An agent that audits LLM responses using `critic` and `reviser` sub-agents to evaluate and improve the quality of the responses. This agent demonstrates a human-in-the-loop pattern using a `SequentialAgent` workflow.

4. **parent\_and\_subagents**
   A parent agent that manages multiple sub-agents, each responsible for different tasks. This sample showcases how to create a multi-agent system where the parent agent delegates tasks to its sub-agents.

5. **workflow\_agents**
   A collection of agents that work together in a workflow. This sample demonstrates how to orchestrate multiple agents to achieve a common goal, showcasing the power of collaboration in agent-based systems.




## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) installed. `uv` is a fast, next-generation Python package installer.

### Installation

1.  **Create a virtual environment:**

    ```shell
    uv venv
    ```

2.  **Install the dependencies:**
    - For **Linux**:
      ```shell
      uv pip install -r requirements-linux.txt
      ```
    - For **macOS**:
      ```shell
      uv pip install -r requirements-mac.txt
      ```

### Configuration

The ADK requires authentication to make model API calls. You can configure this in one of two ways by updating the `.env` file in the root of this project:

1.  **Use a Gemini API Key:**

    - [Get your free API key](https://aistudio.google.com/apikey) and add it to the `.env` file.

2.  **Use Google Cloud Authentication:**
    - Authenticate your environment with Google Cloud credentials.
    - Associate your model API calls with a Vertex AI project and location in the `.env` file.

## 🚀 Running the Agents

You can run the agents in this project using any of the following methods:

- **Method 1: ADK Dev UI**

  ```shell
  # Run on the default port (8000)
  adk web

  # Run on a different port
  adk web --port 8001
  ```

- **Method 2: Programmatically**

  ```shell
  python3 app_agent/agent.py
  ```

- **Method 3: Command-Line Interface**
  ```shell
  adk run my_Google Search_agent
  ```

## 💡 Pro Tips

Look for `#TODO` in the code to find areas that need your attention to get things working.

Search for `#NOTE` to find helpful explanations and insights into the code.

## 🤝 Contributing

Contributions are welcome!

If you have suggestions for improvements or new samples, please feel free to open an issue or submit a pull request.

# ⁉ Questions

Find me on LinkedIn, I'm happy to answer any questions you may have.

LinkedIn link on my GitHub profile.
