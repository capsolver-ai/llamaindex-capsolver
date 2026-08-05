"""Wrap CapSolver Agent execution as LlamaIndex FunctionAgent tools."""

import json
import os

from capsolver_agent import create_executor
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI


capsolver = create_executor()


async def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
    """Solve a supported CAPTCHA in a lawful, user-authorized workflow."""
    result = await capsolver.execute(
        "solve_captcha",
        {
            "captcha_type": captcha_type,
            "website_url": website_url,
            "website_key": website_key,
        },
    )
    return json.dumps(result, ensure_ascii=False)


async def get_capsolver_balance() -> str:
    """Return the current CapSolver account balance."""
    return json.dumps(await capsolver.execute("get_balance", {}), ensure_ascii=False)


async def main() -> None:
    workflow = FunctionAgent(
        tools=[solve_captcha, get_capsolver_balance],
        llm=OpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini")),
        system_prompt="Use CapSolver only for lawful, user-authorized workflows.",
    )
    response = await workflow.run(
        os.getenv("DEMO_PROMPT", "Check my CapSolver balance using the available tool.")
    )
    print(response)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
