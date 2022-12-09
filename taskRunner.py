import shlex
import subprocess

shell_cmd = "main.py"
    
subprocess_cmd = shlex.split(shell_cmd)
subprocess.call(subprocess_cmd)