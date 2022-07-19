from typing import List

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.login = True

class Solution:
    table = dict()

    def register(self, username: str, password: str) -> str:
        if username not in self.table:
            new_user = User(username, password)
            self.table[username] = new_user
            return 'Registered Susccessfully'
        return 'Username already exists'
    
    def login(self, username: str, password: str) -> str:
        user = self.table[username]
        if username in self.table and user.password == password and not user.login:
            user.login = True
            return 'Logged In Successfully'
        return 'Login Unsuccessful'
    
    def logout(self, username: str) -> str:
        user = self.table[username]
        if username in self.table and user.login:
            user.login = False
            return 'Logged Out Successfully'
        return 'Logout Unsuccessful'

class SolutionII:
    def implementAPI(self, logs: List[str]) -> List[str]:
        table = dict()
        login = dict()
        ans = []

        for log in logs:
            # split string into parts
            commands = log.split(' ')
            i = 0
            while i < len(commands) - 1:
                # register
                if commands[i] == 'register':
                    if commands[i+1] not in table:
                        table[commands[i+1]] = commands[i+2]
                        login[commands[i+1]] = True
                        ans.append('Registered Susccessfully')
                    else:
                        ans.append('Username already exists')
                    i += 2

                # login
                elif commands[i] == 'login':
                    if commands[i+1] in table and table[commands[i+1]] == commands[i+2] and not login[commands[i+1]]:
                        login[commands[i+1]] = True
                        ans.append('Logged In Successfully')
                    else:
                        ans.append('Login Unsuccessful')
                    i += 2

                # logout
                elif commands[i] == 'logout':
                    if commands[i+1] in table and login[commands[i+1]]:
                        login[commands[i+1]] = False
                        ans.append('Logged Out Successfully')
                    else:
                        ans.append('Logout Unsuccessful')
                    i += 1
        return ans

execution = SolutionII()
result = execution.implementAPI(["login harry 1234", "register harry 1234", "logout harry", "register harry harrycool"])
print(result)