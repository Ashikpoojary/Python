# built-in library that provides a way to interact with the operating system.
import os 

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want to me to speak or 'q' to quit: ")
        if x == "q":
            break
        command = f'powershell -command "Add-Type -AssemblyName System.Speech; $speech = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speech.Speak(\'{x}\')"'
        os.system(command)


"""
Explanation of the PowerShell command:

powershell -command "...": This tells the os.system function to execute the following string as a PowerShell command.

Add-Type -AssemblyName System.Speech: This loads the necessary .NET assembly that contains the Text-to-Speech functionality.

$speech = New-Object System.Speech.Synthesis.SpeechSynthesizer: This creates an instance of the SpeechSynthesizer object and stores it in the $speech variable.

$speech.Speak(\'{x}\'): This calls the .Speak() method on the $speech object, passing your input string x as the text to be spoken. Note the use of single quotes (\') to enclose the variable x within the double-quoted string, which is necessary for the PowerShell command to work correctly.
"""