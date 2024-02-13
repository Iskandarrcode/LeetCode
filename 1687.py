command = "G()()()()(al)"

def good(command):
    command = command.replace("()", "o")
    command = command.replace("(al)", "al")
    return command
    
            
            
print(good(command))