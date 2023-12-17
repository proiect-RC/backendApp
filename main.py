import subprocess

proc1 = subprocess.Popen(['python', 'faceRecognitionApp.py'])
proc2 = subprocess.Popen(['python', 'authenticationApp.py'])

# Wait for the processes to finish
proc1.wait()
proc2.wait()