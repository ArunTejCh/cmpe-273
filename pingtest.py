import subprocess


host = "yahoo.com"

ping = subprocess.Popen(
    ["ping", "-c", "3", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print out
