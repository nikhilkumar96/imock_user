from dto.register_dto import RegisterDTO


class RegisterController:

    def __init__(self, user_id=None, user_data=None):
        self.user_id = user_id
        self.user_data = user_data

    async def save_data(self):
        user_check = await self.check_user()
        if user_check:
            return f"User Already Exist at {user_check}"
        return await RegisterDTO().add_user(self.user_data)

    async def check_user(self):
        return await RegisterDTO().check_user(self.user_id)

    async def get_user_data(self):
        pass

    def update_user_data(self):
        pass
