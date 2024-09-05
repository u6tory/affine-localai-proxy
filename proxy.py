from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx
import json
import os
from pydantic import BaseModel, HttpUrl, Optional

# Define the ApiConfig model
class ApiConfig(BaseModel):
    llm_api_endpoint: HttpUrl
    default_model: str = None
    api_key: Optional[str] = None
    overwrite_system_prompt: Optional[str] = ""
    append_system_prompt: Optional[str] = ""

# Load the API configuration from environment variables
api_config = ApiConfig(
    llm_api_endpoint=os.getenv("LLM_API_ENDPOINT"),
    default_model=os.getenv("DEFAULT_MODEL"),
    api_key=os.getenv("API_KEY", None),
    overwrite_system_prompt=os.getenv("OVERWRITE_SYSTEM_PROMPT", ""),
    append_system_prompt=os.getenv("APPEND_SYSTEM_PROMPT", ""),
)

# Create the FastAPI app
app = FastAPI()

# Extract configuration from the api_config object
API_ENDPOINT = api_config.llm_api_endpoint
MODEL = api_config.default_model
OVERWRITE_SYSTEM_PROMPT = api_config.overwrite_system_prompt
APPEND_SYSTEM_PROMPT = api_config.append_system_prompt

# Rest of your code remains the same

@app.post("/chat/completions")
async def handle_chat_completions(request: Request):
    # Read the incoming JSON
    incoming_data = await request.json()

    # Modify the model field
    if 'model' in incoming_data:
        incoming_data['model'] = MODEL  # Replace with the model you want
    if OVERWRITE_SYSTEM_PROMPT and OVERWRITE_SYSTEM_PROMPT != "":
        if incoming_data['messages'][0]['role'] == 'system':
            incoming_data['messages'][0]['content'] = OVERWRITE_SYSTEM_PROMPT
        else:
            incoming_data['messages'] = [{"role" : "system", "content" : OVERWRITE_SYSTEM_PROMPT}] + incoming_data['messages']
    elif APPEND_SYSTEM_PROMPT and APPEND_SYSTEM_PROMPT != "":
        incoming_data['messages'][0]['content'] = incoming_data['messages'][0]['content'] + '\\n' + APPEND_SYSTEM_PROMPT

    # Define a generator to stream the response back to the client
    async def proxy_stream():
        async with httpx.AsyncClient() as client:
            # Send the request to the Ollama API
            async with client.stream("POST", API_ENDPOINT, json=incoming_data) as response:
                async for chunk in response.aiter_text():
                    # Stream the chunk to the client
                    print(chunk)
                    yield chunk

    # Return a streaming response
    return StreamingResponse(proxy_stream(), media_type="application/json")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)