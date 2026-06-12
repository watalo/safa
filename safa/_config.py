
'''路径配置文件'''

import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INPUT_PATH = os.path.join(ROOT_PATH, 'input')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'output')
IMG_PATH = os.path.join(ROOT_PATH, 'img')
DB_PATH = os.path.join(ROOT_PATH, 'db')
# MODEL_PATH = os.path.join(ROOT_PATH, 'THUDM', 'chatglm-6b')