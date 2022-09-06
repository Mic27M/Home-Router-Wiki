import os
from pathlib import Path 

cwd = Path(os.getcwd())
os.chdir(f'{cwd}/geekdoc/sites')
cwd = Path(os.getcwd())
os.system('hugo server -D')


