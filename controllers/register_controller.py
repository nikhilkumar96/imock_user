from sanic import exceptions

from dto.register_dto import RegisterDTO
from exceptions.exception_constants import ExceptionConstants


class RegisterController:

    def __init__(self, user_id=None, user_data=None):
        self.user_id = user_id
        self.user_data = user_data

    async def save_data(self):
        user_check = await self.check_user()
        if user_check:
            raise exceptions.InvalidUsage(ExceptionConstants(user_check).user_exist())
        return await RegisterDTO().add_user(self.user_data)

    async def check_user(self):
        return await RegisterDTO().check_user(self.user_id)

    async def get_user_data(self):
        return await RegisterDTO().get_filtered_user(self.user_id)

    async def update_user_data(self):
        return await RegisterDTO().update_user(self.user_id, self.user_data)

    async def delete_user_data(self):
        return await RegisterDTO().delete_user(self.user_id)
