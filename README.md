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

## 3. Change AFFiNE to use the API

Add the folowing lines on the file `/rooot/.affine/self-host/config/affine.js`

```js
AFFiNE.use('copilot', {
  openai: {
    baseURL: 'http://proxy_ip:port',
    apiKey: 'ANYTHING AT ALL, DONT REMOVE THIS LINE, you may leave it blank though', 
  },
})
```


# Project RoadMap and current restrictions and Caveats:

## Image generation:

Currently AFFiNE uses another endpoint to get images, i've not been able to track this down yet do a custom image generation server, so at this time it's not possible to generate images using AFFiNE ai and this proxy.
This is on my road map, feel free to reach out if you got any ideas of how to do so.

## Document tips for no limit ai and other necessary configurations

There are some tips on the backend and server side of affine that could be also documented here to help on a fully functional self-hosted solution