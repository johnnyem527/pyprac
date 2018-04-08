'''函数内部如果需要访问全局变量
则需要在函数内部用global关键字声明一次变量'''
g_var = "Emma"

def change_global_1():
    g_var = "Chloe"

change_global_1()
print(g_var)

def change_global_2():
    global g_var
    g_var = "Chloe"

change_global_2()
print(g_var)

# nonlocal用于内嵌函数访问外部包裹函数
def outer():
    local_var = "A"
    def inner1():
        # nonlocal local_var
        # local_var = "B"
        pass
        def inner2():
            nonlocal local_var
            local_var = "C"
        inner2()
    inner1()
    print(local_var)

outer()





