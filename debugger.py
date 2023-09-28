import webbrowser
import traceback

def debugger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = traceback.format_exc().splitlines()[-1]
            print(f"Error: {error_msg}")
            webbrowser.open(f"https://stackoverflow.com/search?q={error_msg}")
            raise
    return wrapper


def canyoubaidu(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = traceback.format_exc().splitlines()[-1]
            print(f"Error: {error_msg}")
            webbrowser.open(f"https://baidu.leeay.com/?s={error_msg}")
            raise
    return wrapper
