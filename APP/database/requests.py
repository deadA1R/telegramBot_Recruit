from APP.database.models import async_session
from APP.database.models import Recruit, User
from sqlalchemy import select, update, delete


async def set_recruit(tg_id: int) -> None:
    async with async_session() as session:
        recruit = await session.scalar(select(Recruit).where(Recruit.tg_id == tg_id))
        if not recruit:
            session.add(Recruit(tg_id=tg_id))
            await session.commit()

async def set_user(data):
    async with async_session() as session:
        session.add(User(
            name=data["name"],
            status=data["status"],
            age=data["age"],
            address=data["address"],
            number=data["number"],
            previous_work_status=data["previous_work_status"],
            previous_work_discription=data["previous_work_discription"],
            comment=data["comment"],
            parent_id=data["parent_id"],
        ))
        await session.commit()

async def set_user_not_releable(data):
    async with async_session() as session:
            session.add(User(
                name=data["name"],
                status=data["status"],
                parent_id=data["parent_id"],
            ))
            await session.commit()

async def get_users(parent_id):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.parent_id == parent_id))
        users = result.scalars().all()
        
        users_list = [user.__dict__ for user in users]
        for user in users_list:
            user.pop('_sa_instance_state', None)
        return users_list
    
async def delete_user(user_id, parent_id):
    async with async_session() as session:
        query = delete(User).where(User.id == user_id, User.parent_id == parent_id)
        await session.execute(query)
        await session.commit()

async def delete_all_users(parent_id):
    async with async_session() as session:
        query = delete(User).where(User.parent_id == parent_id)
        await session.execute(query)
        await session.commit()

async def get_recruit_id_by_tg_id(tg_id):
    async with async_session() as session:
        result = await session.scalar(select(Recruit.id).where(Recruit.tg_id == tg_id))
        return result
          