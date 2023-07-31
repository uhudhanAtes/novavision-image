# NovaVision Image
Docker based ML / CV project skeleton for NovaVision
## Create Development Environment in PyCharm
Clone new project and create run/debug configurations with below settings in PyCharm
### Add Docker Server
Open Preferences > Build,Execution,Deployment > Docker : Add docker server (Name: Docker)
### Create Dockerfile Configuration and Build Image 
Create new run/debug configuration from Dockerfile template with below settings: 
(You should change image tag, container name and project root directory name according to repo name)
- Name: novavision-image build
- Server: Docker
- Image Tag: novavision-image
- Container name: novavision-image
- Context folder: .
- Dockerfile:Dockerfile.dev
- Bind ports: 8888:8888
- Bind mounts: {project-root-path}:/opt/project
- Run build image: checked  

Run this file to build image
### Creating Container From Image
Create new run/debug configuration Docker Image with below settings: 
- Name: novavision-image container
- Server: Docker
- Image ID or name: novavision-image
- Contanier name: (must be blank)
- Bind ports: 8888:8888
- Bind mounts: {project-root-path}:/opt/project
- Run options: --name novavision-image

Run this file to build container 
### Create Docker Remote Interpreter
**_Image building should be finished for create docker remote interpreter._**  
Open Preferences > Project > Python interpreter > Add Python Interpreter : Select "Docker" and set "Image name" as "image" then click "Ok"  
Configure "Path mappings" setting in Python Interpreter: Open "Edit Project Path Mappings" dialog window  
Add new Path Mappings with below settings:
- Local path: {project-root-path}
- Remote path: /opt/project
### Create Fast Api Configuration and Start (service.py)
Create new run/debug configuration from "FastAPI" template with below settings:
(You should change Python Interpreter according to image tag)
- Application file: {project-root-path}/service.py
- Application name: <detect automatically> 
- Unicorn options: --reload --host 0.0.0.0 --port 8000
- Environment variables: PYTHONUNBUFFERED=1
- Python Interpreter: novavision-image:latest
- Docker container settings
    - Port bindings: 
      - Host Port: 8000
      - Container Port: 8000
      - Host IP: 0.0.0.0
      - Protocol: tcp
    - Volume bindings: 
      - Host path: {project-root-path}
      - Container path: /opt/project
    - Run options : --entrypoint= --rm --name=novavision-image-service

Run this file to start FastAPI on container
### Create Git Submodules Configuration 
Add the submodules included in the project by typing the following command in the terminal
```console
git submodule update --init --recursive
```
Run the following command in terminal to add a different submodule (cap-ocr-text-detection)
```console
git submodule add https://github.com/novavision-ai/cap-ocr-text-detection.git capsules/OcrTextDetection
```   
Run the following command in terminal to remove a submodule (cap-ocr-text-detection)
```console    
git rm capsules/OcrTextDetection
rm -rf .git/modules/capsules/OcrTextDetection
```

### Run Python App on Running Container in PyCharm
Right click on running container at "Services" window and then select option to "Create terminal" or "Exec"  
Write that command template for run python app in exec or terminal: "python {path-of-app-file}"
```console
python capsules/capsule/apps/client.py
```
