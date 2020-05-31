print('please input your name: ')
name=input()
print('please input your marital status: ')
status=input()
print('please input your sex: ')
sex=input()
print('please input your age: ')
age=input()
if status =='married':
    print('congratulations', name,'you are insured')
elif status == 'unmarried' and sex == 'male' and age >= '30':
    print('congratulations', name, 'you are insured')
elif status == 'unmarried' and sex == 'female' and age >= '25':
    print('congratulations', name, 'you are insured')
else:
    print('sorry',name,'you are not eligible for insurance')
