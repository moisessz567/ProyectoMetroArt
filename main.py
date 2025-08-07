from museo import Museo
from API import pull_departamentos

def main():
    museo = Museo(pull_departamentos())
    museo.start()
    
main()
