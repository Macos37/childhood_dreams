import uvicorn

#from source.logger import *
from src.services.main import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, log_config='logging.conf')