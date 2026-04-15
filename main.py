"""Signet + Pydantic AI: Sign every tool call with Ed25519."""

from signet_auth import SigningAgent

agent = SigningAgent.create("pydantic-bot", owner="team")

# --- Use with Pydantic AI ---
# from pydantic_ai import Agent
# from signet_auth.pydantic_ai_integration import signet_tool_middleware
#
# ai = Agent("openai:gpt-4")
#
# @ai.tool
# @signet_tool_middleware(agent)
# def search(query: str) -> str:
#     return f"Results for: {query}"
#
# result = ai.run_sync("Search for AI security")

# --- Or sign manually ---
receipt = agent.sign("search", params={"query": "AI agent security"})
print(f"Signed: {receipt.id}")
print(f"Tool:   {receipt.action.tool}")
print(f"Verify: {agent.verify(receipt)}")

print("\nDone. Run 'signet audit --since 1h' to see the audit log.")
