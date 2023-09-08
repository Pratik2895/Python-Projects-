from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get('/get_movie/')
def get_movie():
    return "Dr.Strange"


# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=8000):