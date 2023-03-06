
# ## ---- define the variables by locals() AND globals()
x1 = 12
x2 = 4
x3 = 7
x4 = 66
x5 = 16
names = locals()
for i in range(5):
    names['l_' + str(i + 1) + str(i + 1)] = (i + 1) * 2

# ## ---- call the variables
for i in range(5):
    xx = names.get('x' + str(i + 1))
    ll = names.get('l_{}{}'.format(i + 1, i + 1))
    print(xx, ll)
    # print()

# ## ---- exec
for i in range(5):
    exec('for_{}={}'.format(i, 2 * i))

for i in range(5):
    exec('for_2_{}=2*for_{}'.format(i, i))
for i in range(5):
    exec('print(for_2_{},for_{})'.format(i, i))
# print(for_0, for_1, for_2, for_3)
# for i in range(5):
#     exec('print("l_{}{}=",l_{}{})'.format(i + 1, i + 1, i + 1, i + 1))
#     exec('print("for_{}=",for_{})'.format(i, i))
