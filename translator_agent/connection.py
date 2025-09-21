from agents import AsyncOpenAI, OpenAIChatCompletionsModel , RunConfig 
from dotenv import load_dotenv
import os 
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY: 
   raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")
 
provider = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/'
)
model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=provider
)

config = RunConfig(
    model = model,
    model_provider= provider,
    tracing_disabled=False
)