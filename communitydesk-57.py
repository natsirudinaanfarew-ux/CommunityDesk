# === Stage 57: Add structured result objects for command handlers ===
# Project: CommunityDesk
class Response:
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    @staticmethod
    def success(msg="OK"):
        return Response(200, msg)

    @staticmethod
    def error(msg="An error occurred"):
        return Response(400, msg)

    @staticmethod
    def not_found(msg="Resource not found"):
        return Response(404, msg)

    @staticmethod
    def conflict(msg="Conflict"):
        return Response(409, msg)

    @staticmethod
    def created(msg="Created"):
        return Response(201, msg)

    @staticmethod
    def accepted(msg="Accepted"):
        return Response(202, msg)

    def to_dict(self):
        return {"status_code": self.status_code, "message": self.message}
