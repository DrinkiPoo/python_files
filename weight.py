weight = input('Weight: ')
scale = input('(L)bs or (K)g: ')

if scale in 'Kk':
    conversion = 2.204623
    new_scale = 'pounds'
elif scale in 'Ll':
    conversion = 0.45
    new_scale = 'kilograms'
else:
    print('Error: invalid scale')

print(f'You are {int(weight) * conversion} {new_scale}')