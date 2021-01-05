from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="orders",
        description="Simple API to order products from different stores.",
        version="1.0",
    )

    @app.get("/health")
    async def health() -> str:
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        debugpy.wait_for_client()
        breakpoint()
        return "ok"

    return app
