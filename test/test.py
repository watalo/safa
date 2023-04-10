import os
from far import _config

dirpath = ''.join([_config.Path.root, '/safa/input'])

print(os.listdir(dirpath)[0].split('.')[0])