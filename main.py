import notion
import os
from notion.client import NotionClient
from dotenv import load_dotenv


load_dotenv()


print("hi there")

client = NotionClient(token_v2=os.getenv("TOKEN_V2"))

page = client.get_block("https://www.notion.so/d310069be80e463aa5a75f907b09b59b?v=97a53a79783445ddb9b2da11f1a6020c")

print("the page title is:", page.title)
