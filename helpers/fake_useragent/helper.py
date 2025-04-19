from fake_useragent import UserAgent

UA = UserAgent(browsers="chrome", os=["windows", "macos"], platforms="pc")


def get_random_user_agent() -> str:
    return UA.random
