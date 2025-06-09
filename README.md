# MCP-Client

This is a chatbot client that interacts with a remote job search MCP (Model Context Protocol) server. It utilizes a local LLM (Language Model) running in Ollama to process user queries and communicate with the server hosted on Hugging Face Spaces. 

My Remote Jobs Search MCP Server Link🔗: 
https://oppaai-job-search-mcp-server.hf.space

The client is designed to help users find remote jobs by querying the server with natural language.

## Setup Instructions

1.  **Prerequisites:**
    *   Python 3.12+
    *   Ollama installed and running locally
    *   The `qwen3:1.7b-q8_0` model downloaded in Ollama (`ollama pull qwen3:1.7b-q8_0`)

2.  **Install Dependencies:**

    ```bash
    pip install pydantic_ai asyncio
    ```

3.  **Configuration:**
    *   Ensure Ollama is running on `http://localhost:11434`.  If it's running on a different port, you'll need to modify the `MCP-client.py` file.

4.  **Run the Client:**

    ```bash
    python MCP-client.py
    ```

## Usage

Run the client and enter your job search query (e.g., "remote data science jobs"). The client will process your query and return relevant job listings from the remote server.

## MCP

MCP (Model Context Protocol) is used to facilitate communication between the client and server, allowing for efficient and scalable job searching.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/OppaAI/MCP-Client/blob/main/LICENSE) file for details.
