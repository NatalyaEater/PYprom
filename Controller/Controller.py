import Model.Program
import View.View as v

def run():
    num = ''
    while num != '5':
        v.menu()
        num = input().strip()
        if num == '1':
            Model.Program.add()
        if num == '2':
            Model.Program.show(1)
        if num == '3':
            Model.Program.show(1)
            Model.Program.edit_show(1)
        if num == '4':
            Model.Program.show(1)
            Model.Program.edit_show(2)
        if num == '5':
            v.exit()
            break
