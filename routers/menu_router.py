#########################################################
#               ROUTING FOR Main MENU DAL               #
#########################################################
from typing import List

from fastapi import APIRouter

from dals.menu_dal import MenuDAL
from db.config import async_session
from models.menu import Menu

router = APIRouter()


# create main menu
@router.post("/api/v1/menus")
async def create_main_menu(title: str, description: str):
    async with async_session() as session:
        async with session.begin():
            menu_dal = MenuDAL(session)
            return await menu_dal.create_menu(title, description)


# view main menu
@router.get("/api/v1/menus")
async def get_all_menus() -> List[Menu]:
    async with async_session() as session:
        async with session.begin():
            menu_dal = MenuDAL(session)
            return await menu_dal.get_all_menu()


@router.get("/api/v1/menus/{menu_id}")
async def get_one_menu_by_menu_id(menu_id: str) -> Menu:
    async with async_session() as session:
        async with session.begin():
            menu_dal = MenuDAL(session)
            return await menu_dal.get_menu_by_menu_id(menu_id)
