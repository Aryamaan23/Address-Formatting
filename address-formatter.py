from fastapi import FastAPI
app = FastAPI()
 
@app.get("/")
def first_example():
    
    return {"GFG Example": "FastAPI"}