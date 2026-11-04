def isibiodata(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


Biodata = isibiodata(
    'Ahmad', 'Haykal',
    location='surakarta',
    field='informatika',
    hobby='membaca',
)
print(Biodata)