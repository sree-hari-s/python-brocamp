class vscode:
    def execute(self):
        print("compiling")
        print("Running")
    
class pycharm:
    def execute(self):
        print("compiling")
        print("spell check")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()
        
        
ide=pycharm()
lap=Laptop()
lap.code(ide)