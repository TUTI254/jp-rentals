# first test 
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import sql_database
from langchain_experimental.sql import SQLDatabaseChain

api_key='AIzaSyBOBlORAcFeHtJsuZ3-7KRCO19OQva2xn0'

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key,temperature=0.1)
db_user = "root"
db_password = ""
db_host = "localhost"
db_name = "jp-rentals"
# connecting db to project
db= sql_database.SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# questions to prompt 
qns1 = db_chain.invoke("How many rental units do i have that are located in Tokyo? give me a full break down of what they offer from rent the style the size of the unit.")
qns2 = db_chain.invoke("I'm looking for a rental unit that has an air conditioner what options are available and which locations are they in?")
qns3 = db_chain.invoke("what units are in Osaka that are furnished and what are the rates per month?")
