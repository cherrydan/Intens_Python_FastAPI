import uvicorn
from fastapi import FastAPI

from db.config import engine, Base
from routers import menu_router

app = FastAPI(title="YLab University Python Intense Course")
app.include_router(menu_router.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
