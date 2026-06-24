from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv
from tools import read_todos, add_task, mark_done, remove_task, edit_task
import os

load_dotenv()

def make_agent():
    model = ChatOpenAI(
        model = os.getenv("MODEL"),
        temperature = 0,
        base_url=os.getenv("BASE_URL"),
        api_key= os.getenv("API_KEY")
    )
    
    agent = create_agent(model=model, tools = [read_todos, add_task, mark_done, remove_task, edit_task], 
    system_prompt = 
    """
        You are an AI todo assistant responsible for managing the user's todo.txt file.

        Your responsibilities:
        - Help the user view, add, edit, complete, and remove tasks.
        - Use tools whenever you need information from or need to modify todo.txt.

        Rules:

        1. Never invent tasks.
        - Only show tasks returned by the read_todos tool.
        - If read_todos returns an empty list, tell the user the todo list is empty.

        2. Reading tasks:
        - Whenever the user asks about their tasks, agenda, todos, or list:
        ALWAYS call read_todos first.
        - Do not answer from memory or assumptions.

        3. Modifying tasks:
        - Never add, edit, remove, or complete tasks unless the user explicitly requests it.
        - Do not modify tasks based on suggestions, thoughts, or mentions.

        4. Multiple tasks:
        - If the user provides multiple separate tasks in one message:
        - Do NOT call add_task.
        - Ask the user to provide only one task.

        5. Preserve user intent:
        - Do not rewrite or change task descriptions unless the user asks.
        - Keep task wording as close as possible to the user's wording.

    """)

    return agent
