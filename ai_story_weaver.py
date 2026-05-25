import streamlit as st
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


# Load .env
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# ---------------- UI ----------------
st.set_page_config(page_title="AI Story Weaver", page_icon="📖")

st.title("📖 AI Story Weaver")
st.write("Create a story step by step with AI")


genre = st.selectbox("Choose Genre", ["Fantasy", "Sci-Fi", "Mystery"])
chapters_limit = st.slider("Number of Chapters", 1, 5, 3)


# ---------------- STATE ----------------
def init_state(state):
    state["chapter"] = 1                                #start with chapter 1 
    state["story"] = f"Genre: {state['genre']}\n"       # initialize story with genre
    return state                                        # return the state

def generate(state):
    llm = ChatGroq(model="llama-3.1-8b-instant")

    prompt = f"""
    Write Chapter {state['chapter']} of a {state['genre']} story.

    Story so far:
    {state['story']}

    User idea:
    {state['user_input']}
    """

    response = llm.invoke(prompt)

    state["story"] += f"\nChapter {state['chapter']}:\n{response.content}\n"
    return state


def update(state):
    state["chapter"] += 1
    return state

# ---------------- GRAPH ----------------
graph = StateGraph(dict)

graph.add_node("init", init_state)
graph.add_node("generate", generate)
graph.add_node("update", update)

graph.set_entry_point("init")

graph.add_edge("init", "generate")
graph.add_edge("generate", "update")
graph.add_edge("update", END)

app = graph.compile()


# ---------------- SESSION ----------------
if "state" not in st.session_state:
    st.session_state.state = None



# ---------------- START FLOW (FIXED) ----------------
user_input = st.text_input("👉 Start your story idea (what should happen first?)")

if st.button("Start Story") and user_input:

    state = {
        "genre": genre,
        "chapter": 1,
        "story": "",
        "user_input": user_input   # 👈 NOW INPUT COMES FIRST
    }

    result = app.invoke(state)
    st.session_state.state = result


# ---------------- DISPLAY ----------------
if st.session_state.state:

    story = st.session_state.state["story"]

    st.text_area(
        "📖 Story (Latest View)",
        story[-1000:],
        height=300
    )

    # NEXT INPUT (optional continuation)
    next_input = st.text_input("👉 What happens next?")

    if st.button("Next Chapter") and next_input:
        st.session_state.state["user_input"] = next_input
        result = app.invoke(st.session_state.state)
        st.session_state.state = result
        st.rerun()

