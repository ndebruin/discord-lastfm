from requests import get, post

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

payload = {
    'grant_type': "authorization_code",
    'code': 'BS0D8RNfXOchkFIXvfaiU9iaPmztxI',
    'redirect_uri': "http://localhost/thisdoesnotexist'",
    'client_id': '843977521795039242'
}

print(post('https://discord.com/api/oauth2/token', headers=headers, params=payload))