# streamline-document-query-engine
*** 

### Overview
This project is a Streamlit-based Document Query Engine that allows users to upload multiple files, which are then indexed using LlamaIndex. Users can query the indexed documents, and the engine will return responses generated using OpenAI's GPT-3.5-turbo model. This tool is designed for efficient and user-friendly document searching, making it ideal for applications in research, business, or personal projects where large volumes of documents need to be queried.

### Features
- Streamlit Interface: User-friendly interface for uploading documents and querying the index.
- Document Indexing: Automatically indexes uploaded documents using VectorStoreIndex.
- Advanced Query Engine: Utilizes a RetrieverQueryEngine to search the indexed documents and return relevant responses.
- OpenAI Integration: Queries are processed using OpenAI's GPT-3.5-turbo model with adjustable temperature settings.
- Post-Processing: Filters query results to ensure relevance and eliminate duplicates.


### Prerequisites
- Python 3.x
- Streamlit
- OpenAI API Key
- Required Python libraries (listed in requirements.txt)


### Installation

- Clone the Repository:

```
git clone Clone https://github.com/toraaglobal/streamline-document-query-engine.git
cd streamline-document-query-engine
```

- Install Dependencies: Install the necessary Python packages:
```
pip install -r requirements.txt

```

- Set Up Environment Variables: Create a .env file to securely store your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

### Usage
- Run the Streamlit App: Start the Streamlit app by running:

```
streamlit run main.py

```


- Upload Documents:
    - Use the file uploader on the web interface to upload multiple files.
    - The documents will be saved to the data folder and indexed.


- Query the Documents:
    - Enter your query in the provided text area and click the "Submit" button.
    - The engine will process your query and display the most relevant response based on the indexed documents.

### Folder Structure
- `data/`: This folder stores the uploaded documents.
- `main.py`: The main script that runs the Streamlit app and handles document indexing and querying.
- `requirements.txt`: Contains all the Python dependencies required to run the project.


### Example Workflow
- Uploading Files:

    - Drag and drop files into the uploader or select them manually.
    - Confirm the successful upload message in the app.

- Running a Query:

    - Type a question or search query in the provided text area.
    - Click "Submit" to receive a response generated from the indexed documents.


### Customization
- Model Settings: Adjust the OpenAI model and temperature settings in the Streamlit sidebar to tailor the response generation.
- Similarity Settings: Modify the SimilarityPostprocessor parameters to refine how query results are filtered and processed.