import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
import uvicorn
from fastapi import FastAPI,Request

import json
from capsules.capsule.src.executors.segmentation import UnetInferrer
from capsules.capsule.src.executors.trainer import Train
from sdks.novavision.src.base.service import Service
from sdks.novavision.src.base.bootstrap import Bootstrap
app = FastAPI()


executors ={'Segmentation':{"Segmentation":UnetInferrer, "Train" : Train}
            }

btstrp = Bootstrap(executors)
bootstrap = btstrp.run()



@app.post('/api')
async def api(request: Request):
    json_data = await request.json()
    json_data = json.dumps(json_data)
    resp = Service(json_data, executors, bootstrap).run()
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
