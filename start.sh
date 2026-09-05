#!/bin/bash
export EXPERIMENT_MODEL="${EXPERIMENT_MODEL:-ollama:granite4.2:8b}"
export EXPERIMENT_HOST="${EXPERIMENT_HOST:-127.0.0.1}"
export EXPERIMENT_PORT="${EXPERIMENT_PORT:-8004}"
echo "🧪 Starting Quantum Experiment Agent (Development)"
echo "Model: $EXPERIMENT_MODEL"
echo "URL: http://$EXPERIMENT_HOST:$EXPERIMENT_PORT"
uv run python -m quantum_experiment_agent.agent
