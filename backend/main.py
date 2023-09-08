from fastapi import FastAPI
app=FastAPI()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return f"Welcome to FAT Server {cuisine}"

@app.get("/get_movie")
def get_movie():
    return "Dr.Strange"
