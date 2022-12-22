from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.index import user, job, role, apps, jt, task, login
from fastapi.responses import JSONResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="HelpDesk App - API")
app.mount("/static", StaticFiles(directory="logoaplikasi"), name="logoaplikasi")
origins = [
    "http://localhost:3002",
    "localhost:3002"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    # Change here to LOGGER
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

app.include_router(job)
app.include_router(user)
app.include_router(role)
app.include_router(apps)
app.include_router(jt)
app.include_router(task)
app.include_router(login)

if __name__ == '__main__':
    uvicorn.run('index:app', reload=True)
