import asyncio, re
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# MCP Server SSE URL
SSE_URL = "https://oppaai-job-search-mcp-server.hf.space/gradio_api/mcp/sse"
server = MCPServerHTTP(url=SSE_URL)

# Ollama LLM wrapped as OpenAIModel
ollama_model = OpenAIModel(
    model_name="qwen3:1.7b-q8_0",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1")
)

# Create Agent with MCP Server
agent = Agent(
    model=ollama_model,
    mcp_servers=[server],
    instructions="""
    Your name is Jobcy. You are an AI assistant designed to help users to find remote jobs by searching through job listings from various sources, including the Jobicy API and other platforms.
    You will list the job listings in a structured format, including the job title, company, location, and the google search link.
    """
    )

async def main():
    async with agent.run_mcp_servers():
        print("✅ Connected to MCP server. Type 'exit' or 'quit' to stop.")
        while True:
            user_input = input("😊 You: ").strip()
            print("\n")
            if user_input.lower() in {"exit", "quit"}:
                print("👋 Goodbye!")
                break
            result = await agent.run(user_input)

            # Remove <think>...</think> blocks
            cleaned_output = re.sub(r"<think>.*?</think>", "", result.output, flags=re.DOTALL).strip()

            print("🤖  AI:", cleaned_output)
            print("\n")

if __name__ == "__main__":
    asyncio.run(main())