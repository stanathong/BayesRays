# Obtain camera transforms using ns-export first
# ns-export cameras --load-config PATH/TO/config.yml --output-dir PATH/TO/OUTPUT/DIR

import json
import numpy as np
from pathlib import Path

def ind(c2w):
    # I believe there is an extra conversion?
    if len(c2w) == 3:
        c2w += [[0, 0, 0, 1]]
    return c2w

# from ns-export
transforms = json.loads(open('BayesRays/script/transforms_train.json').read())

out = {
        'camera_type': 'perspective',
        'render_height': 1080,
        'render_width': 1920,
        'seconds': len(transforms),
        'camera_path': [
            {'camera_to_world': ind(pose['transform']), 'fov': 50, 'aspect': 1, 'file_path': pose['file_path']}
            for pose in transforms
            ]
        }

# camera path for rendering
outstr = json.dumps(out, indent=4)
with open('BayesRays/script/gen_camera_path.json', mode='w') as f:
    f.write(outstr)
