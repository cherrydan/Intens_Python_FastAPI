#########################################################
#               Submenu menu Data-Access-Layer             #
#########################################################
from typing import List, Optional

from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.menu import Submenu


class SubmenuDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_submenu(self, title: str, description: str, submenu_id: str) -> Submenu:
        new_submenu = Submenu(title=title, description=description, submenu_id=submenu_id)
        self.db_session.add(new_submenu)
        await self.db_session.flush()
        return new_submenu

    async def get_all_submenus_by_menu_id(self, menu_id) -> List[Submenu]:
        q = await self.db_session.execute(select(Submenu).where(Submenu.submenu_id == menu_id))
        return q.scalars().all()

    async def get_submenu_by_id(self, menu_id: str, s_id: str) -> Submenu:
        await self.db_session.execute(select(Submenu).where(Submenu.submenu_id == menu_id))
        q = await self.db_session.execute(select(Submenu).where(Submenu.id == s_id))
        return q.scalars().one()

    async def update_submenu_by_id(self, s_id: str, title: Optional[str], description: Optional[str]):
        q = update(Submenu).where(Submenu.id == s_id)
        if title:
            q = q.values(title=title)
        if description:
            q = q.values(description=description)

        q.execution_options(asynchronize_session="fetch")
        await self.db_session.execute(q)
        q = await self.db_session.execute(select(Submenu).where(Submenu.id == s_id))
        return q.scalars().one()

    #
    async def delete_submenu_by_s_id(self, s_id: str):
        await self.db_session.execute(delete(Submenu).where(Submenu.id == s_id))
        return {"msg": f"Submenu with ID {s_id} has been deleted"}
