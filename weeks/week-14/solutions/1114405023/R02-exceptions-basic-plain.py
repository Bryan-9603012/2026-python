import traceback

def parse_value(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f'[14.6] 解析失敗 {type(e).__name__}: {e}')
        return None

def safe_run(func, *args):
    try:
        return func(*args)
    except Exception as e:
        print(f'[14.7] 發生例外 {type(e).__name__}: {e}')
        traceback.print_exc()

class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class ConnectionTimeout(NetworkError):

    def __init__(self, host, seconds):
        super().__init__(f'連線 {host} 超過 {seconds} 秒')
        self.host = host
        self.seconds = seconds

def connect(host, timeout):
    if host == '':
        raise HostnameError('主機名稱為空')
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f'connected to {host}'
if __name__ == '__main__':
    print('--- 14.6 ---')
    parse_value('abc')
    parse_value(None)
    print('\n--- 14.7 ---')
    safe_run(lambda: 1 / 0)
    print('\n--- 14.8 ---')
    for host, t in [('example.com', 5), ('', 5), ('slow.com', 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            print(f'接到 {type(e).__name__}: {e}')
