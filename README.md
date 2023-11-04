![image](https://github.com/mytechnotalent/CortexaAI/blob/main/CortexaAI.jpg?raw=true)

# CortexaAI
An open-source Automation Engine that can perform full Front-End & Back-End Automation for scraping data in addition to Test Automation with Docker and Kubernetes integration.

## Step 1: Install Docker Desktop
Docker Desktop [Instructions](https://docs.docker.com/desktop)

## Step 2: Install Helm
Helm [Instructions](https://helm.sh/docs/intro/install)

## Step 3a: Setup Local Environment MAC/LINUX [OPTION 1]
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3b: Setup Local Environment Windows [OPTION 2]
```bash
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Step 4a: Build App Locally [OPTION 1]
```bash
cd app/website
docker build --tag cortexaai:latest .
docker run -d --name cortexaai --publish 5000:5000 cortexaai
cd ..
cd ..
```

## Step 4b: Deploy & Run App to Kubernetes [OPTION 2]
```bash
cd app
helm install website .
kubectl -n default get service website-cortexaai
```

## Step 5: Run Docker Compose (Selenium Grid)
```bash
docker compose up --scale chrome=2
```

## Step 6: Observe Selenium Grid Run (Including Built-In VNC Viewer)
```
http://localhost:4444/ui
```

## CortexaAI (Results Populated In `items.csv`)
```bash
export BROWSER=chrome
python cortexaai_cli.py
```

## Run Front-End Tests MAC/LINUX (Including Snapshot Images) [OPTION 1]
```bash
export BROWSER=chrome 
URL=http://localhost:<PORT>
python -m unittest discover
```

## Run Front-End Tests Windows (Including Snapshot Images) [OPTION 2]
```bash
$env:BROWSER="chrome"
$env:URL="http://host.docker.internal:<PORT>"
python -m unittest discover
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
