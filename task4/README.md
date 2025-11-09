# Tasks4 – OpenAI Chat Completions API Experiment

## Description
This standalone experiment uses the OpenAI Chat Completions API (gpt-5-mini) to summarize paragraph-length task descriptions into short phrases.

## How it works
1. Two sample task descriptions are defined in `main.py`.
2. The program sends each to the OpenAI API.
3. It prints a short summary for each task.

## Run instructions
Make sure your OpenAI API key is set:

```bash
export OPENAI_API_KEY="your_api_key_here"
uv run tasks4
**
