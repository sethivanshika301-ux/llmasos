# LLMs as Operating Systems: Agent Memory

A hands-on implementation of persistent, self-editing agent memory using [Letta](https://www.letta.com/) (formerly MemGPT), built while completing DeepLearning.AI's short course **["LLMs as Operating Systems: Agent Memory"](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory/)** taught by Charles Packer and Sarah Wooders.

This project demonstrates how an LLM agent can manage its own context window like an operating system manages memory — moving information between an active context (like RAM) and external storage (like disk) so the agent retains knowledge far beyond a single context window.

## What This Does

Based on the ideas in the [MemGPT paper](https://arxiv.org/abs/2310.08560) ("Towards LLMs as Operating Systems"), this project builds an agent that:

- Maintains **core memory** — persistent facts about itself, the user, and the task, kept always in context
- Maintains **archival memory** — a larger external store the agent can search and retrieve from as needed
- **Self-edits its own memory** using tool-calling, deciding what to keep, update, or move to archival storage
- Uses **multi-step reasoning** to decide when to write, read, or search memory rather than just generating text
- Supports **multi-agent collaboration**, where multiple agents can share and coordinate through memory

The example implemented here follows the course's research/HR agent scenario, where the agent needs to remember details across a long-running conversation that would otherwise exceed a normal context window.

## Prerequisites

- Python 3.9+
- An API key from at least one LLM provider:
  - [OpenAI API key](https://platform.openai.com/api-keys), and/or
  - [Anthropic API key](https://console.anthropic.com/settings/keys)
- (Optional) [Jupyter](https://jupyter.org/install) if you want to run the notebook interactively

## Installation

1. Clone the repository:
   ```bash
   git clone llmasos
   cd llmasos
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

Create a `.env` file in the project root with your API key(s):

```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

Make sure it's listed in `.gitignore` before pushing.

## Usage

Run the notebook:

```bash
jupyter notebook agent_memory_demo.ipynb
```

Or, if this is a standalone script:

```bash
python main.py
```

Walk through the notebook/script to:
1. Initialize a Letta agent with core memory blocks (persona and human info)
2. Send messages and observe how the agent updates its own memory
3. Query archival memory to retrieve information beyond the active context
4. (If included) Set up multiple agents and observe shared/coordinated memory

## Project Structure

```
.
├── agent_memory.ipynb   # Main notebook walking through the course exercises
├── requirements.txt          # Python dependencies
├── .env.example               # Template for required environment variables
├── .gitignore
└── README.md
```

## Key Concepts Covered

- Two-tier memory architecture (in-context vs. out-of-context)
- Turning agent state (memory + tools + messages) into prompts
- Core memory design and implementation
- Archival memory search and retrieval
- Multi-agent collaboration patterns

## Acknowledgments

- Course: [LLMs as Operating Systems: Agent Memory](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory/) by DeepLearning.AI, in partnership with Letta
- Instructors: Charles Packer and Sarah Wooders
- Framework: [Letta](https://github.com/letta-ai/letta)
- Research: [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)
