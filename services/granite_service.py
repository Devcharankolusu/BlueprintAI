import os

from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials, APIClient
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

credentials = Credentials(
    url=os.getenv("IBM_URL"),
    api_key=os.getenv("IBM_API_KEY")
)

project_id = os.getenv("IBM_PROJECT_ID")

client = APIClient(credentials=credentials)

client.set.default_project(project_id)

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    api_client=client,
    project_id=project_id,
    params={
        "max_new_tokens": 1200,
        "temperature": 0.5
    }
)

def test_connection(prompt):

    response = model.generate_text(
    prompt=prompt
)

    return response