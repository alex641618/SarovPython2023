import numpy as np
import json
import os

save_dir = 'saves'
file_name = 'config.json'

#item 1
def create_dirs(N):

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    for n in range(N):
        data = f'data_{n}'
        if not os.path.exists(os.path.join(save_dir, data)):
            os.mkdir(os.path.join(save_dir, data))
            
            if not os.path.exists(os.path.join(save_dir, data, file_name)):
                save_dict(create_dict(n), os.path.join(save_dir, data, file_name))     


#item 2
def create_dict(n):
    return dict(number=n)

#item 3
def save_dict(arg_dict, path):

    with open(path, 'w') as f:
        f.write(json.dumps(arg_dict))
