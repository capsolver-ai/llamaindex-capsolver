# LlamaIndex + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/llamaindex-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/llamaindex-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable LlamaIndex `FunctionAgent` examples powered directly by [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent).

> Examples only: no `llamaindex-capsolver` PyPI package, duplicated SDK, or independent release lifecycle.

## Repository scope

The demo converts ordinary async Python functions into LlamaIndex tools. Those functions delegate every operation to the shared CapSolver executor, keeping schemas, solving behavior, error handling, and browser support centralized.

## Quick start

```bash
git clone https://github.com/capsolver-ai/llamaindex-capsolver.git
cd llamaindex-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Export the keys in [`.env.example`](.env.example), then run `python examples/quickstart.py`.

## Key integration code

```python
from capsolver_agent import create_executor
from llama_index.core.agent.workflow import FunctionAgent

capsolver = create_executor()

async def get_capsolver_balance() -> str:
    return str(await capsolver.execute("get_balance", {}))

agent = FunctionAgent(tools=[get_capsolver_balance], llm=llm)
```

See [`examples/quickstart.py`](examples/quickstart.py) for solving and balance tools.

## Project layout

```text
examples/quickstart.py   LlamaIndex FunctionAgent demo
requirements.txt         Shared SDK repositories and LlamaIndex
tests/test_demo.py        Offline validation
.github/workflows/ci.yml  Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver for AI agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [LlamaIndex agents](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/)

## Responsible use

Use the example only for lawful, user-authorized workflows that respect target-site terms. Never commit secrets or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

LlamaIndex is a third-party project. This repository is maintained by CapSolver and is not affiliated with or endorsed by LlamaIndex.
