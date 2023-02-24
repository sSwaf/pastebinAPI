import requests

class API:
    key = "Your token"
    nickname = "Your account nickname"
    password = "Your account password"

    def login(self):
        login = {
            'api_dev_key': self.key,
            'api_user_name': self.nickname,
            'api_user_password': self.password
        }
        login = requests.post("https://pastebin.com/api/api_login.php", data=login)
        return login.text

    def post(self, text, title):
        postInfo = {
            'api_option': 'paste',
            'api_dev_key': self.key,
            'api_paste_code': text,
            'api_paste_name': title,
            'api_user_key': None,
        }
        postInfo['api_user_key'] = self.login()

        paste = requests.post("https://pastebin.com/api/api_post.php", data=postInfo)
        if paste.status_code == 200:
            print(f'Succesfuly post!\nLink post: {paste.text}')
        else:
            print(f'Oops! Error code: {paste.status_code}')

    def delpost(self, pastekey):
        delete = {
            'api_dev_key': self.key,
            'api_user_key': self.login(),
            'api_option': 'delete',
            'api_paste_key': pastekey
        }
        delpost = requests.post("https://pastebin.com/api/api_post.php", data=delete)
        if delpost.status_code == 200:
            print(f'Succesfuly!')
        else:
            print(f'Oops! Error code: {delpost.status_code}')


