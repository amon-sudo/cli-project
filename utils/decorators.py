def require_login(func):
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            print("Please login first!")
            return
        return func(self, *args, **kwargs)

    return wrapper