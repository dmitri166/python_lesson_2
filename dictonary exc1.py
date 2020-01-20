users = [
    {'admin': True, 'active': True, 'name': 'kevin'},
    {'admin': True, 'active': False, 'name': 'John'},
    {'admin': False, 'active': True, 'name': 'Mike'},
    {'admin': False, 'active': False, 'name': 'Ryan'},
]
for var in users:
    if var['admin']:
        print("ADMIN " + users.get('name'))
    elif var['active']:
        print('ACTIVE ' + users.get('name'))
    elif var['admin' and 'active']:
        print("ACTIVE-ADMIN " + users.get('name'))
    else:
        print('name')
