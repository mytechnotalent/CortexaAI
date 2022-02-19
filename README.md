![image](https://github.com/mytechnotalent/CortexaAI/blob/main/CortexaAI.jpg?raw=true)

# CortexaAI
An open-source Automation Engine that can perform full Front-End & Back-End Automation for scraping data in addition to Test Automation with Docker and Kubernetes integration.

## Step 1: Install Docker Desktop
Docker Desktop [Instructions](https://docs.docker.com/desktop/mac/install)

## Step 2: Setup Local Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3: OPTIONAL Setup Voice Recognition (MAC Only)
Use Voice Control On MAC [Instructions](https://support.apple.com/en-us/HT210539).

## Step 4: Deploy & Run App to Kubernetes
```bash
minikube delete
minikube start --driver docker
kubectl apply -f deployment.yml
minikube start service: webapp
kubectl get all
minikube service webapp-service
cd ..
```

## Step 5: Run Docker Compose (Selenium Grid)
```bash
docker-compose -f ./docker-compose.yml up --scale chrome=1 -d
```

## Step 6: Observe Selenium Grid Run (Including Built-In VNC Viewer)
```
http://localhost:4444/ui/index.html#/sessions
```

## CortexaAI (Results Populated In `items.csv`)
```bash
export BROWSER=chrome && python cortexaai_cli.py
```

## Front-End Tests (Including Snapshot Images)
```bash
export BROWSER=chrome && python -m unittest discover
```

## Back-End Tests
```bash
ansible-playbook -i hosts roles/tests/main.yml
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
