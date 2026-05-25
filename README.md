🎥 Course Video

👉 Watch the full crash course here: https://youtu.be/vUbMnAHWlKU



# LangGraph Crash Course 

This comprehensive 5-hour crash course covers LangGraph from basics to advanced concepts, culminating in a full "Smart Support Agent" project using the Groq API.

## Course Structure

### 1. Basics (1 hour)
- **LangChain Recap**: Agents, chains, tools with examples
- **What is LangGraph?**: Stateful workflows, branching logic, use cases
- **Graph vs Simple Chain**: Detailed comparison with diagrams
- **Installation and Setup**: Environment setup, API keys

**Goal**: Solid foundation in LangGraph concepts.

### 2. Core Concepts (1.5 hours)
- **Nodes**: Types of nodes, implementation
- **Edges**: Flow control, conditional edges
- **State**: Managing state, persistence
- **Conditional Routing**: If-else, complex conditions
- **Loops**: Retry mechanisms, iterative agents
- **Demo**: Simple Q&A agent with memory
- **Exercises**: Build your own simple graph

### 3. Intermediate Concepts (1 hour)
- **Advanced State Management**: TypedDict, validation
- **Multi-actor Graphs**: Multiple agents interacting
- **Error Handling**: Try-except in nodes
- **Persistence**: Saving state to disk
- **Human-in-the-Loop**: User interventions
- **Practice**: Extend the Q&A agent

### 4. Hands-on Build (1 hour)
- **Planning the Agent**: Requirements, design
- **Building Components**: Nodes, edges, state
- **Testing**: Unit tests for nodes
- **Debugging**: Common issues and fixes
- **Full Agent**: User input, LLM, memory, conditional branch

### 5. Project: Smart Support Agent (1 hour)
- **Features Deep Dive**: Conversation memory, tool integration, looping
- **Streamlit UI**: Building the interface
- **Deployment**: Running locally
- **Enhancements**: Add more tools, improve logic

## Project: Smart Support Agent

**Features**:
- User query input
- Decide: normal reply or tool call (e.g., FAQ lookup)
- Maintain memory (conversation context)
- Loop until proper answer is obtained

**Tech Stack**:
- LangGraph
- Groq API (LLM)
- Simple JSON-based memory

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Set up Groq API key (see notebooks for details)
3. Follow the notebooks in order

## Files
- `README.md`: This file
- `requirements.txt`: Python dependencies
- `01_basics.ipynb`: Basics (1 hour)
- `02_core_concepts.ipynb`: Core concepts (1.5 hours)
- `03_intermediate.ipynb`: Intermediate concepts (1 hour)
- `04_hands_on_build.ipynb`: Hands-on build (1 hour)
- `smart_support_agent.py`: Project with Streamlit UI (1 hour)
- `optional_research_agent.ipynb`: Multi-step research agent
- `optional_decision_bot.ipynb`: Decision-making bot

## Running the Project
Run the Streamlit app: `streamlit run smart_support_agent.py`

## Prerequisites
- Python 3.8+
- Basic Python knowledge
- Groq API account

## Tips
- Take breaks between sections
- Experiment with code
- Join discussions for questions

## Troubleshooting
- API key issues: Check Groq dashboard
- Import errors: Reinstall packages
- Notebook issues: Restart kernel
