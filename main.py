from typing import Union, Dict
from fastapi import FastAPI, Depends
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="🍒 CHERI",
    description="외국인 관광객을 위한 관광 코스 도우미",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def root():
    return "Hello! This is dev_ewha's API Server";