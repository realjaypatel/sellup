from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
import requests as rs
import ast
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix='/startup',
    tags=['product']
)

data = {
    
}




@router.get('/{startup_id}', status_code=status.HTTP_200_OK)
async def return_home(startup_id,request: Request):
    print(startup_id)
    data = rs.get('https://excel2api.vercel.app/api/1BSOoMb-j3ALwi56lgSW8x7q17iNGSbuq1gpi9vV_ZOQ')
    data = data.json()

    for json in data:
        # print(json['Id'], str(startup_id),type(json['Id']),str(json['Id']) == startup_id)
        if str(json['Id']) == str(startup_id):
            json['other_img'] =ast.literal_eval(json['other_img'])
            print(json)
            return templates.TemplateResponse("product.html", {"request": request,"data":json})

    return 'not found'

