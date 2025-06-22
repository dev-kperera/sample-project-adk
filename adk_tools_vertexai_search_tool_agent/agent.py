import os
import sys
sys.path.append("..")

from google.adk import Agent
# from agents.tools.retrieval import VertexAISearchTool
from google.adk.tools import VertexAiSearchTool

from dotenv import load_dotenv

# Load environment variables from the agent directory's .env file
load_dotenv()
project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
datastore_id = os.getenv("DATASTORE_ID")

# The data_store_id path follows the same format as the datstore parameter
# of google.genai.types.VertexAISearch. View its documentation here:
# https://googleapis.github.io/python-genai/genai.html#genai.types.VertexAISearch

# Create your vertexai_search_tool and update its path below
vertexai_search_tool = VertexAiSearchTool(
   data_store_id=f"projects/{project_id}/locations/global/collections/default_collection/dataStores/{datastore_id}"
)


root_agent = Agent(
   # A unique name for the agent.
   name="adk_tools_vertexai_search_agent",
   # The Large Language Model (LLM) that agent will use.
   model="gemini-2.0-flash-001",
   # A short description of the agent's purpose, so other agents
   # in a multi-agent system know when to call it.
   description="Answer questions using your data store access.",
   # Instructions to set the agent's behavior.
   instruction="You analyze new planet discoveries and engage with the scientific community on them.",
   # Add the vertexai_search_tool tool to perform search on your data.
   tools=[vertexai_search_tool]
)
