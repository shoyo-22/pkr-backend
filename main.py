import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='PKR Backend',
    version='1.0.0'
)


@app.get("/")
async def root():
    return {'project': 'pkr'}


if __name__ == '__main__':
    uvicorn.run("main:app")
