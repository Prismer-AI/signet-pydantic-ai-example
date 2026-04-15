# Signet + Pydantic AI Example

Add cryptographic signing to every tool call in Pydantic AI agents.

## Install

```bash
pip install signet-auth pydantic-ai
```

## Quick Start

```python
from pydantic_ai import Agent
from signet_auth import SigningAgent
from signet_auth.pydantic_ai_integration import signet_tool_middleware

signer = SigningAgent.create("pydantic-bot", owner="team")

agent = Agent("openai:gpt-4")

@agent.tool
@signet_tool_middleware(signer)
def search(query: str) -> str:
    """Search the web."""
    return f"Results for: {query}"

result = agent.run_sync("Search for AI security news")
# Every tool call is signed with Ed25519
```

## Verify

```bash
signet audit --since 1h
signet audit --verify
```

## Links

- [Signet](https://github.com/Prismer-AI/signet) — Cryptographic action receipts for AI agents
- [PyPI: signet-auth](https://pypi.org/project/signet-auth/)
- [Pydantic AI](https://ai.pydantic.dev/)
