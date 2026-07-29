from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings
settings=get_settings(); client=AsyncIOMotorClient(settings.mongodb_url, serverSelectionTimeoutMS=3000); db=client[settings.mongodb_database]
async def create_indexes():
    await db.projects.create_index("name", unique=True)
    for name in ("tasks","reports","analyses","qa_tests","activities","saved_responses"):
        await db[name].create_index("projectId"); await db[name].create_index("createdAt")
    for name in ("projects","tasks","qa_tests"): await db[name].create_index("status")
    for name in ("tasks","qa_tests"):
        await db[name].create_index("category"); await db[name].create_index("priority")
