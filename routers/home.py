from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
templates = Jinja2Templates(directory="templates")
import requests


router = APIRouter(
    # prefix='/',
    tags=['home']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request):
    data = requests.get('https://excel2api.vercel.app/api/1BSOoMb-j3ALwi56lgSW8x7q17iNGSbuq1gpi9vV_ZOQ')
    data = data.json()
    return templates.TemplateResponse("home.html", {"request": request,"Data":data})

