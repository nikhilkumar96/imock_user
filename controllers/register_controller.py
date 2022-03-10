from dto.register_dto import RegisterDTO


class RegisterController:

    def __init__(self, user_id=None, user_data=None):
        self.user_id = user_id
        self.user_data = user_data

    async def save_data(self):
        if await self.check_user():
            return "User Already Exist"
        return await RegisterDTO().add_user(self.user_data)

    async def check_user(self):
        pass

    async def get_user_data(self):
        pass

    def update_user_data(self):
        pass
