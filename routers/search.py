from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
import requests as rq
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix='/search',
    tags=['search']
)

data = {
    
}




@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request):
    data = rq.get('https://excel2api.vercel.app/api/1BSOoMb-j3ALwi56lgSW8x7q17iNGSbuq1gpi9vV_ZOQ')
    data = data.json()
    
    return templates.TemplateResponse("search.html", {"request": request,"data":data})
    

