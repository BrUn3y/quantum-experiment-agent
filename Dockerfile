FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml README.md ./
COPY src ./src
RUN uv sync --no-dev

ENV EXPERIMENT_HOST=0.0.0.0
ENV EXPERIMENT_PORT=8004
EXPOSE 8004

CMD ["uv", "run", "python", "-m", "quantum_experiment_agent.agent"]
