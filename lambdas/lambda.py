# l = lambda x: x > 5
#
# # def l(x):
# #     return x > 5
# print(l(1))

def alter(values, check):
    # return list(filter(check, values))
    return [val for val in values if check(val)]

my_list = [1, 2, 4, 5, 212, 123]
another_list = alter(my_list, lambda x: x < 15)

print(another_list)

# a = [1, 2, 3, 5, 12, 210]
# lines = [val for val in a if val < 15]
# print(lines)

def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)

print(remove_numbers("he1231l5lo12 World"))
print(skip_letter("hello", "e"))