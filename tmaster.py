#!/usr/bin/env python3

import data_message
import actions

        
class Controller():

    @staticmethod
    def handler(act):
        if act is 'R':
            actions.remove()
        elif act is 'C':
            actions.create()
        elif act is 'A':
            actions.add()
        elif act is 'E':
            actions.edit()
        else:
            print("Action error")
            main()
            
        
def main():
    templates = actions.Template().get_templates()

    print(data_message.welcome_message)
    for i in templates['templates']:
        print(i)

    print(data_message.menu)
    
    action = input("Choose action: ")
    Controller.handler(action)


if __name__ == "__main__":
    main()
