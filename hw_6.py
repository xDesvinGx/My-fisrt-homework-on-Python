my_dict = {'Evgeniy': 2000, 'Olesya': 1999, 'Maksim': 2001, 'Kseniya': 1998}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Evgeniy'))
print('Not existing value:', my_dict.get('Oleg'))
my_dict['Kristina'] = 1985
my_dict['Veronika'] = 2004
Max = my_dict.pop('Maksim')
print('Deleted value: ', Max)
print('Updated Dict: ', my_dict)

old_set = {24, 'Виноград', 'Машина', 13.55, 24, 'Виноград', 13.55, 'Машина'}
my_set = set(old_set)
print('Set: ', my_set)
my_set.add('Колесо')
my_set.add(4)
my_set.remove(13.55)
print('New set: ', my_set)
