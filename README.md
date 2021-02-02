# audio_file_serve_fast_api
### Follow below steps to setup locally

Step-1
``
git clone https://github.com/nirajparmar1988/audio_file_serve_fast_api.git
``

Step-2: Create virtual env
``
virtualenv venv
``
Step-3: Install requirements.txt
``
pip install -r requirement.txt
``
Step-4: Run fastapi app
``
uvicorn src.audio_file_server_app.main:app --reload
``
