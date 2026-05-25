"""
This is a Smart Support Agent built using LangGraph.

Flow:
1. User gives input
2. Graph decides → use Tool or LLM
3. LLM or Tool generates response
4. Memory stores conversation history
5. Streamlit shows chat UI
6. Graph can loop if response is not good enough
"""
import streamlit as st
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, List
import os

# Load .env
load_dotenv()

# Streamlit page
st.set_page_config(
    page_title="Smart Support Agent",
    page_icon="🤖"
)

st.title("🤖 Smart Support Agent")
st.markdown("LangGraph + OpenRouter")

# State
class AgentState(TypedDict):
    user_input: str
    response: str
    memory: List[dict]
    need_tool: bool
    loop_count: int

# Input Node
def input_node(state):
    return state

# Decision Node
def decide_node(state):

    state["need_tool"] = any(
        word in state["user_input"].lower()
        for word in ["faq", "help", "support"]
    )

    return state

# LLM Node
def llm_node(state):

    llm = ChatOpenAI(
        #model="mistralai/mistral-7b-instruct:free",
        model="deepseek/deepseek-chat",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )

    context = "\n".join([
        f"Q: {m['input']} | A: {m['response']}"
        for m in state["memory"][-3:]
    ])

    prompt = f"""
Context:
{context}

User Question:
{state['user_input']}

Give a helpful answer.
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    state["memory"].append({
        "input": state["user_input"],
        "response": state["response"]
    })

    return state


# Tool Node
def tool_node(state):

    faqs = {
        "faq": "Here are the FAQs.",
        "help": "How can I help you?",
        "support": "Contact support@example.com"
    }

    found = False

    for key, answer in faqs.items():

        if key in state["user_input"].lower():
            state["response"] = answer
            found = True
            break

    if not found:
        state["response"] = "No FAQ matched."

    state["memory"].append({
        "input": state["user_input"],
        "response": state["response"]
    })

    return state

# Satisfaction Check
def check_satisfaction(state):

    state["loop_count"] += 1

    if "?" in state["response"] and state["loop_count"] < 3:
        return "decide"

    return END

# Graph
graph = StateGraph(AgentState)

graph.add_node("input", input_node)
graph.add_node("decide", decide_node)
graph.add_node("llm", llm_node)
graph.add_node("tool", tool_node)

graph.set_entry_point("input")

graph.add_edge("input", "decide")

graph.add_conditional_edges(
    "decide",
    lambda x: "tool" if x["need_tool"] else "llm"
)

graph.add_conditional_edges("llm", check_satisfaction)
graph.add_conditional_edges("tool", check_satisfaction)

app = graph.compile()

# Session State
if "memory" not in st.session_state:
    st.session_state.memory = []

if "loop_count" not in st.session_state:
    st.session_state.loop_count = 0

# User Input
user_input = st.text_input("Ask something")

# Submit
if st.button("Submit") and user_input:

    initial_state = {
        "user_input": user_input,
        "response": "",
        "memory": st.session_state.memory,
        "need_tool": False,
        "loop_count": st.session_state.loop_count
    }

    result = app.invoke(initial_state)

    st.session_state.memory = result["memory"]
    st.session_state.loop_count = result["loop_count"]

    st.subheader("Response")
    st.write(result["response"])

# Chat History
if st.session_state.memory:

    st.subheader("Conversation History")

    for i, msg in enumerate(st.session_state.memory):

        st.write(f"**Q{i+1}:** {msg['input']}")
        st.write(f"**A{i+1}:** {msg['response']}")
        st.write("---")

        