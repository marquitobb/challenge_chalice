class GeneralResponse:

    @staticmethod
    def success(data=None, message=None, status_code=200):
        return {
            "data": data,
            "message": message or "Success"
        }, status_code

    @staticmethod
    def error(message=None, error_type="Internal Server Error", status_code=500):
        return {
            "message": message,
            "error": error_type
        }, status_code
