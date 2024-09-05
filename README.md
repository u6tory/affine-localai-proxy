# AFFiNE Local AI Proxy

This Project aims to be a simple way to configure AFFiNE copilot requests from your local instance to local models you own. Although you may use it for custom online endpoints as Groq, Meta or even OpenAI but with other models

## 1. Set Environment

The first step is to create a .env file, use the .env.example as a template for yours.

```bash
LLM_API_ENDPOINT="http://your_domain_or_ip:port/chat/endpoint" # For ollama http://ip:11434/v1/chat/completions
DEFAULT_MODEL="your_model:tag" # Examples : llava, llama3, llama3.1:8B
API_KEY="if_applicable-your-api-key" # sk-asddfasdadasdasdasdasfbnvnvnserfsdgjnmvlrwjmasfvjnscmasdfjmasdfnasdcjmascnm for OpenAI, none for ollama default config
OVERWRITE_SYSTEM_PROMPT="" # if set it will overwrite the affine system prompt
APPEND_SYSTEM_PROMPT="" # if set(and OVERWRITE_SYSTEM_PROMPT not) it will append to the affine system prompt
```

## 2. Run docker

```bash
docker compose up -d
```
