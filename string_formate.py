# introduction for string formatting



# style 1
# printf : like C style
name = 'Roger'
x = 100
y = 3.14
print('hi %s' % name)
print('hi %d' % x)
print('hi %f' % y)
print('hi %s, my number is %d' % (name, x))


# style 2
print('hi {}, my number is {}'.format(name, x))

# style 3 after python3.6+ with
print(f'hi {name}, my number is {y}')

print(f'hi {name:>10}, my number is {y}') # 可以印固定長度
print(f'hi {name:<10}, my number is {y}') # 可以印固定長度

