<div align="center">

# 🧪 Quantum Experiment Agent

### Hybrid quantum optimization powered by IBM Granite

[![Development](https://img.shields.io/badge/status-active_development-F1C21B)](https://github.com/BrUn3y/quantum-experiment-agent)
[![IBM Granite](https://img.shields.io/badge/model-Granite_4.2_8B-6929C4)](https://www.ibm.com/granite)
[![Agent Stack](https://img.shields.io/badge/runtime-Agent_Stack-0F62FE)](https://agentstack.beeai.dev/)
[![A2A](https://img.shields.io/badge/protocol-A2A-24A148)](https://github.com/a2aproject/A2A)

Design, optimize, validate, and visualize hybrid quantum experiments through a dedicated A2A service.

</div>

> [!WARNING]
> This agent is in active development. The currently implemented execution workflow is p=1 QAOA Max-Cut for graphs containing 2–8 nodes. VQE and error-mitigation workflows are planning capabilities and are not yet executed automatically.

## What works today

| Capability | Result |
|---|---|
| QAOA Max-Cut | Optimizes a p=1 variational circuit with deterministic grid search |
| Exact validation | Compares QAOA against the exact classical optimum |
| Sampling | Produces reproducible shot distributions and top partitions |
| Experiment Canvas | Shows graph partition, convergence, approximation ratio, and outcomes |
| Optional QPU evaluation | Sends the optimized final circuit to Quantum Computing Agent through A2A |
| Research planning | Uses IBM Granite 4.2 8B for VQE, mitigation, and experimental-design requests |

## Architecture

```text
Quantum Lab Agent :8000
          │ A2A
          ▼
Quantum Experiment Agent :8004
     ├── local QAOA optimizer
     ├── exact Max-Cut validator
     ├── Canvas dashboard
     └── Quantum Computing Agent :8003 ──► IBM Quantum QPU
```

## Quick start

```bash
git clone https://github.com/BrUn3y/quantum-experiment-agent.git
cd quantum-experiment-agent
uv sync
ollama pull granite4.2:8b
cp .env.example .env
./start.sh
```

The A2A agent card is available at:

```text
http://127.0.0.1:8004/.well-known/agent-card.json
```

## Try it

```text
Use QAOA to solve Max-Cut on a 5-node graph using the local simulator
```

```text
Run QAOA for a 4-node graph with edges (0,1), (1,2), (2,3), (3,0) using the local simulator
```

```text
Compare a 5-node QAOA Max-Cut baseline with real IBM Quantum hardware
```

Simulator requests stay local. Explicit hardware comparison requests send the optimized final circuit once to the Computing Agent, which creates a fresh IBM Quantum job.

## Test

```bash
uv run python -m unittest discover -s tests -v
uv run python -m compileall -q src
```

## Related public agents

| Repository | Role |
|---|---|
| [Quantum Lab Agent](https://github.com/BrUn3y/quantum_lab_agent) | Main orchestrator |
| [Quantum Developer Agent](https://github.com/BrUn3y/quantum-developer-agent) | Code generation |
| [Quantum Status Agent](https://github.com/BrUn3y/quantum-status-agent) | Backend and job monitoring |
| [Quantum Computing Agent](https://github.com/BrUn3y/quantum-computing-agent) | Circuit execution |

## Roadmap

- Multi-layer and optimizer-pluggable QAOA
- VQE execution for small molecular Hamiltonians
- Error-mitigation comparisons
- Automatic simulator-versus-QPU reports
- Multi-job convergence tracking
