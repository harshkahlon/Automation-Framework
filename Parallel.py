


import subprocess

subprocess.run("python -m pytest ClaritySmoke_test.py & python -m pytest SmartSmoke_test.py", shell=True)

