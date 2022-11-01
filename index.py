from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.index import user, job, role, apps
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="HelpDesk App - API")
app.mount("/static", StaticFiles(directory="logoaplikasi"), name="logoaplikasi")


@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    # Change here to LOGGER
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

app.include_router(job)
app.include_router(user)
app.include_router(role)
app.include_router(apps)

if __name__ == '__main__':
    uvicorn.run('index:app', reload=True)
