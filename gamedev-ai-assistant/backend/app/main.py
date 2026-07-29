from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings
from .database import db,create_indexes
from .routes import dashboard_routes,project_routes,analysis_routes,task_routes,report_routes,qa_routes,activity_routes
@asynccontextmanager
async def lifespan(app):
 try: await create_indexes()
 except Exception as exc: print(f"MongoDB indisponível na inicialização: {exc}")
 yield
app=FastAPI(title="GameDev AI Assistant API",version="1.0.0",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=[get_settings().frontend_url],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
for route in (dashboard_routes,project_routes,analysis_routes,task_routes,report_routes,qa_routes,activity_routes): app.include_router(route.router,prefix="/api")
@app.get("/")
async def root(): return {"name":"GameDev AI Assistant API","status":"online","provider":get_settings().ai_provider}
@app.get("/health")
async def health():
 try: await db.command("ping"); return {"api":"healthy","mongodb":"connected"}
 except Exception: return JSONResponse({"api":"healthy","mongodb":"disconnected"},status_code=503)
@app.exception_handler(Exception)
async def error(request:Request,exc:Exception): return JSONResponse({"detail":"Erro interno. Verifique os logs do servidor."},status_code=500)
