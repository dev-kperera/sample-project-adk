# Agents
## root_agent
a root_agent named steering (its name is used to identify it in ADK's dev UI and command line interfaces). It asks the user a question (if they know where they'd like to travel or if they need some help deciding), and the user's response to that question will help this steering agent know which of its two sub-agents to steer the conversation towards. Notice that it only has a simple instruction that does not mention the sub-agents, but it is aware of its sub-agents' descriptions.

## travel_brainstormer
a travel_brainstormer that helps the user brainstorm destinations if they don't know where they would like to visit.

## attractions_planner
an attractions_planner that helps the user build a list of things to do once they know which country they would like to visit.


# Steps to test the workflow agents
1. Run `adk web` or `adk run`
2. Say `hello` to begin a new conversation.
3. When prompted, enter a "I would like to go to Japan."
4. Notice that you have been transferred to the other sub-agent, attractions_planner.
5. Reply with "Actually I don't know what country to visit."
6. Notice that you have been transferred to the other sub-agent, travel_brainstormer.
7. Reply with "exit" to end the conversation.