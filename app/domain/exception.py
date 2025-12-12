class ErrorInRedis(Exception):
    def __init__(self, message: str = "Redis operation failed"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"RedisError: {self.message}"