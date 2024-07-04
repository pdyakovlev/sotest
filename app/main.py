from app.api.endpoints import router as endp_router
from app.api.category import router as cat_router
from app.core.config import settings
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title=settings.app_title, description=settings.desc)
app.include_router(endp_router)
app.include_router(cat_router)
