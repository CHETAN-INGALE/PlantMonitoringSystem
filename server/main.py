from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from config import load_config
from connectdb import insertSensorData, lastTemp, lastHumidity, lastMoisture, lastSensorData

db_config = load_config()

class SensorData(BaseModel):
    temp: int
    humidity: int
    moisture: int

app = FastAPI(
    title="Plant Monitring System",
    version="0.1",
    description="Hello, Welcome to our Plant Monitoring system"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/readSensor/", tags=["For Sensor"])
async def readSensor(data: SensorData):
    insertSensorData(db_config, int(data.temp), int(data.humidity), int(data.moisture))

@app.get("/data", tags=["For User"])
async def get_data():
    return lastSensorData(db_config)

@app.get("/temp", tags=["For User"])
async def get_temp():
    return lastTemp(db_config)

@app.get("/humidity", tags=["For User"])
async def get_humidity():
    return lastHumidity(db_config)

@app.get("/moisture", tags=["For User"])
async def get_moisture():
    return lastMoisture(db_config)