from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from alembic_migration.router import alembic_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Track your prompt evals",
        description="Prompts",
        version="0.1.0",
    )

    app.include_router(prompt_router)
    app.include_router(alembic_router)

    return app


app = create_app()
