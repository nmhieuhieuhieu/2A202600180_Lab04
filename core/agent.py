from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Đọc System Prompt
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prompt_path = os.path.join(BASE_DIR, "config", "system_prompt.txt")

with open(prompt_path, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# 2. Khai báo State 
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node (Hàm xử lý chính của AI)
def agent_node(state: AgentState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    response = llm_with_tools.invoke(messages)
    
    # LOGGING
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"\n[LOG] ⚙️ AI đang gọi công cụ: {tc['name']} với đầu vào: {tc['args']}")
    else:
        print("\n[LOG] 💬 AI đang trả lời trực tiếp...")
        
    return {"messages": [response]}


# 5. Xây dựng Graph 
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges("agent", tools_condition)

builder.add_edge("tools", "agent")

graph = builder.compile()
# 6. Chat loop (Vòng lặp tương tác với người dùng)
if __name__ == "__main__":
    print("=" * 60)
    print("🛫 TravelBuddy - Trợ lý Du lịch Thông minh")
    print("   Gõ 'quit' hoặc 'q' để thoát chương trình")
    print("=" * 60)

    while True:
        user_input = input("\n👤 Bạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Hẹn gặp lại!")
            break
            
        if not user_input:
            continue

        print("🤖 TravelBuddy đang suy nghĩ...")
        result = graph.invoke({"messages": [("human", user_input)]})
        final = result["messages"][-1]
        print(f"\n🤖 TravelBuddy:\n{final.content}")