import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp_use import MCPAgent,MCPClient

import os


async def run_memory_chat():
    """Run a chat using MCPAgent built-in conversation memory"""

    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    ## config the path-change to your config file

    config_file="browser_mcp.json"
    print("Inirializing Chat...")
    ## create MCP client and agent with memory enabled
    client=MCPClient.from_config_file(config_file)
    llm=ChatGroq(model="llama-3.3-70b-versatile")

    ## create agent with memory_enabled=True
    agent=MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )
    
    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("=================================\n")

    try:
        # Main chat loop
        while True:
            # Get user input
            user_input = input("\nYou: ")

            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Get response from agent
            print("\nAssistant: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        # Clean up
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())




# print("App Started")
# import asyncio
# import os

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from mcp_use import MCPAgent, MCPClient


# async def run_memory_chat():

#     load_dotenv()

#     groq_api_key = os.getenv("GROQ_API_KEY")

#     if not groq_api_key:
#         raise ValueError("GROQ_API_KEY not found")

#     print("Initializing Chat...")

#     config_file = "browser_mcp.json"

#     client = MCPClient.from_config_file(config_file)
#     print("MCP Client Connected")

#     llm = ChatGroq(
#         model="llama-3.3-70b-versatile",
#         api_key=groq_api_key
#     )

#     print("LLM Initialized")

#     agent = MCPAgent(
#         llm=llm,
#         client=client,
#         max_steps=15,
#         memory_enabled=True,
#     )

#     print("\n===== Interactive MCP Chat =====")

#     try:
#         while True:

#             user_input = input("\nYou: ")

#             if user_input.lower() in ["exit", "quit"]:
#                 print("Ending conversation...")
#                 break

#             print("\nAssistant: ", end="", flush=True)

#             try:
#                 response = await agent.run(user_input)
#                 print(response)

#             except Exception as e:
#                 print(f"\nError: {e}")

#     finally:

#         if client and client.sessions:
#             await client.close_all_sessions()


# if __name__ == "__main__":
#     asyncio.run(run_memory_chat())