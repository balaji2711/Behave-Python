import subprocess
if __name__ == '__main__':
    s = subprocess.run('behavex -tWeb --parallel-processes 3 --parallel-scheme feature')
