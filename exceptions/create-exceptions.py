class MissingLabelError(KeyError):
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass


def login():
 raise IncorrectPasswordError

try:
    login()
except IncorrectPasswordError:
    print("Password error")
except IncorrectUsernameError:
    print("Username error")