from fastapi import FastAPI,Depends,Request,HTTPException
from starlette.responses import RedirectResponse
from fastapi.security import APIKeyHeader
import uvicorn

import http.client
import json
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# from user import Users_id,UserInDB,User
# from test import scraper_1
from scraper.nandan import scraper_1
from scraper.tirupati import scraper_2
from scraper.mahabali import scraper_3


app = FastAPI()
# server origin
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:30000",
    "https://erp.techtonions.com",
    "https://oms.techtonions.com",
    "https://accounts.techtonions.com",
    "https://techtonions.com",
    "https://www.techtonions.com",
    "https://techtonions.com",
    "https://www.techtonions.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
nandan=scraper_1()
tirupati=scraper_2()
mahabali=scraper_3()
# author
API_KEY = "pratyanj"
# API_KEY = "12c666fe-6fcc-4e25-aa32-5d398ac6dfdf70d28731-5377-41b7-ab83-8ce1a710f0dcd5b52729-74e6-4837-886a-c5a5fbea8d77"

# Create an instance of the APIKeyHeader security scheme
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

# Define a dependency that will check the API key
async def check_api_key(api_key: str = Depends(api_key_header)):
    # if not api_key or api_key != f"Bearer {API_KEY}":
    if not api_key or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Enter invalid API key")

# # Define a protected route that requires the API key
# @app.get("/login for TO", dependencies=[Depends(check_api_key)])
# def protected():
#     return {"message": "login successful!"}
# *************************************scraper***********************************
@app.get("/tirupaticourier/{cid}",dependencies=[Depends(check_api_key)])
async def scraper_runner(cid:int):
    return tirupati.scrapedata(cid)

@app.get("/nandancourier/{cid}",dependencies=[Depends(check_api_key)])
async def scraper_runner(cid:int):
    return nandan.scrapedata(cid)
    
@app.get("/mahabalicourier/{cid}",dependencies=[Depends(check_api_key)])
async def scraper_runner(cid:int):
    return mahabali.scrapedata(cid)
# **********************************scraper********************************************
# **********************************GST api********************************************
@app.get("/GST/{GST}", dependencies=[Depends(check_api_key)])
async def GST(GST):
    if len(GST) == 15:
        conn = http.client.HTTPSConnection("apisetu.gov.in")
        headers = {'X-APISETU-CLIENTID': "com.techtonions", 'X-APISETU-APIKEY': 'xiMFQwOQCexT3svwmaeGu31Blc4sl9Sr'}
        conn.request("GET", f"/gstn/v2/taxpayers/{GST}", headers=headers)
        res = conn.getresponse()
        
        if res.status == 200:
            data = res.read()
            response = data.decode("utf-8")
            # Assuming response is a JSON string, parse it into a Python dictionary
            json_response = json.loads(response)
            return JSONResponse(content=json_response)
        else:
            # Handle non-200 status codes as needed
            raise HTTPException(status_code=res.status, detail="API request failed")
    else:
        raise HTTPException(status_code=401, detail="Enter a valid GST number")
# **********************************GST api********************************************
# --------------main page as docs----------------------------
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    response = RedirectResponse(url='/docs')
    return response
# ------------------------------------------------------------

#   If in server then comment belove code 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
