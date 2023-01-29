#########################################################
#               ROUTING FOR Main MENU DAL               #
#########################################################
from typing import List, Optional

from fastapi import APIRouter
from sqlalchemy.exc import NoResultFound

from dals.menu_dal import MenuDAL
from dals.submenu_dal import SubmenuDAL
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
async def get_one_menu_by_menu_id(menu_id: str):
    async with async_session() as session:
        async with session.begin():
            try:
                menu_dal = MenuDAL(session)
                return await menu_dal.get_menu_by_menu_id(menu_id)
            except NoResultFound:
                return {"msg": "No result"}


@router.put("/api/v1/menus/{menu_id}")
async def update_main_menu_by_menu_id(menu_id: str, title: Optional[str] = None, description: Optional[str] = None):
    async with async_session() as session:
        async with session.begin():
            menu_dal = MenuDAL(session)
            return await menu_dal.update_menu_by_menu_id(menu_id, title, description)


@router.delete("/api/v1/menus/{menu_id}")
async def delete_menu_by_menu_id(menu_id: str):
    async with async_session() as session:
        async with session.begin():
            menu_dal = MenuDAL(session)
            return await menu_dal.delete_menu_by_menu_id(menu_id)


@router.post("/api/v1/submenu/{menu_id}")
async def create_submenu(title: str, description: str, menu_id: str):
    async with async_session() as session:
        async with session.begin():
            submenu_dal = SubmenuDAL(session)
            return await submenu_dal.create_submenu(title, description, menu_id)


@router.get("/api/v1/menus/{menu_id}/submenus")
async def get_all_submenus_by_menu_id(menu_id: str):
    async with async_session() as session:
        async with session.begin():
            try:
                submenu_dal = SubmenuDAL(session)
                return await submenu_dal.get_all_submenus_by_menu_id(menu_id)
            except NoResultFound:
                return {"msg": "No result"}
