class ExceptionConstants:

    def __init__(self, data_point):
        self.data_point = data_point

    def not_present_in_request(self):
        return f"{self.data_point} not present in request"

    def user_exist(self):
        return f"User Already Exist at {self.data_point}"
