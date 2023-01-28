#########################################################
#               Main menu Data-Access-Layer             #
#########################################################
from typing import List, Optional

from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.menu import Menu


class MenuDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_menu(self, title: str, description: str) -> Menu:
        new_menu = Menu(title=title, description=description)
        self.db_session.add(new_menu)
        await self.db_session.flush()
        return new_menu

    async def get_all_menu(self) -> List[Menu]:
        q = await self.db_session.execute(select(Menu).order_by(Menu.menu_id))
        return q.scalars().all()

    async def get_menu_by_menu_id(self, menu_id: str) -> Menu:
        q = await self.db_session.execute(select(Menu).where(Menu.menu_id == menu_id))
        return q.scalars().one()

    async def update_menu_by_menu_id(self, menu_id: str, title: Optional[str], description: Optional[str]):
        q = update(Menu).where(Menu.menu_id == menu_id)
        if title:
            q = q.values(title=title)
        if description:
            q = q.values(description=description)

        q.execution_options(asynchronize_session="fetch")
        await self.db_session.execute(q)
        q = await self.db_session.execute(select(Menu).where(Menu.menu_id == menu_id))
        return q.scalars().one()

    async def delete_menu_by_menu_id(self, menu_id: str):
        await self.db_session.execute(delete(Menu).where(Menu.menu_id == menu_id))
        return {"msg": f"Menu with ID {menu_id} has been deleted"}
