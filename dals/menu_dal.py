#########################################################
#               Main menu Data-Access-Layer             #
#########################################################
from typing import List

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
