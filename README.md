### JP Rentals  is a real estate platform where users can get to know the available units both furnished and not furnished depending on the location they want .

* The Rental Units data is stored in a MySQL database
* We will build an LLM based question and answer 
  
system that will use following,
GoogleGenerativeAI(Google Palm LLM )
Hugging face embeddings
Langchain framework
Chromadb as a vector store
Few shot learning (improve the accurancy for our AI model  with progressive learning)
Streamlit for UI (simple UI integration)

tech stack:
Python

# Get started
- create a virtual enviroment for you project

  ### guide for windows

  - cd to project directory
  - run `python -m venv <venv-name>`
  - then activate by running `. <venv-name>/Scripts/activate`

  ### guide for macos

  - cd to project directory
  - run `python3 -m venv <venv-name>`
  - then activate by running `source <venv-name>/bin/activate`

  - create a `.env` file then request the necessary enviroment variables from existing member.please use `.env.example` fo this
  
- then run `pip install -r requirements.txt` to install all neccessary dependancies
- 
- start server : `streamlit run app.py`
