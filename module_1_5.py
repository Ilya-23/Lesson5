immutable_var = tuple([4, 'home', [1, 2]])
#immutable_var[1] = 52  кортеж неизменяемый объект, поэтому элементы не изменить.
print(immutable_var)
immutable_var[2][1] = 52 #  если в кортеже содержится список, то элементы списка можем изменять
print('immutable_var:',immutable_var)
mutable_list = [7, 8.1, 'dog', 'cat']
mutable_list [2] = 9
mutable_list.append('frog')
print('mutable_list:',mutable_list)