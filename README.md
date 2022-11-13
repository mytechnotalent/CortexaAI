<a rel="me" href="https://ioc.exchange/@kevinthomas"></a>

![image](https://github.com/mytechnotalent/CortexaAI/blob/main/CortexaAI.jpg?raw=true)

# CortexaAI
An open-source Automation Engine that can perform full Front-End & Back-End Automation for scraping data in addition to Test Automation with Docker and Kubernetes integration.

## Step 1: Install Docker Desktop
Docker Desktop [Instructions](https://docs.docker.com/desktop/mac/install)

## Step 2: Install Minikube
```bash
brew install minikube
```

## Step 3: Install Helm
```bash
brew install helm
```

## Step 4: Setup Local Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 5: Setup Voice Recognition
[Instructions](https://support.apple.com/en-us/HT210539)

## Step 6: Build App Locally
```bash
cd app/website
docker build --tag cortexaai:latest .
docker run -d --name cortexaai --publish 5000:5000 cortexaai
cd ..
cd ..
```

## Step 7: Install Ansible Galaxy kubernetes.core.k8s
```bash
pip install openshift pyyaml kubernetes
cd /Applications/Python\ <version>
./Install\ Certificates.command
ansible-galaxy collection install kubernetes.core
cd <repo>
```

## Step 8: Deploy & Run App to Kubernetes
```bash
cd app
minikube delete
minikube start
helm install website .
minikube service website-cortexaai [terminal 1]
kubectl port-forward --address 0.0.0.0 service/website-cortexaai 30000:80 [terminal 2]
```

## Step 9: Run Docker Compose (Selenium Grid)
```bash
docker-compose -f ./docker-compose.yml up --scale chrome=1 -d
```

## Step 10: Observe Selenium Grid Run (Including Built-In VNC Viewer)
```
http://localhost:4444/ui/index.html#/sessions
```

## CortexaAI (Results Populated In `items.csv`)
```bash
export BROWSER=chrome && python cortexaai_cli.py
```

## Run Front-End Tests (Including Snapshot Images)
```bash
export BROWSER=chrome URL=http://<internal-ip>:30000 && python -m unittest discover
```

## Run Back-End Tests
```bash
ansible-playbook -i hosts roles/tests/main.yml
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
