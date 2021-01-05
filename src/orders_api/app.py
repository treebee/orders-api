from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="orders",
        description="Simple API to order products from different stores.",
        version="1.0",
    )

    @app.get("/health")
    async def health() -> str:
        return "ok"

    return app
