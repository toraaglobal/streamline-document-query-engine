# import packages
import streamlit as st
import os 
from dotenv import load_dotenv

# load llamandex
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core import get_response_synthesizer
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

## set up sreamlit app
st.set_page_config(page_title="Document Query Engine", page_icon=":mag:", layout="wide")
st.title("Document Query Engine")
st.subheader("Upload your files and query the document index")


## get temprature and top_k in the sidebar
temprature = st.sidebar.slider("Temprature", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
similarity_top_k = st.sidebar.slider("Similarity Top K", min_value=1, max_value=100, value=10, step=1)


# Set the OpenAI model and temperature
# The Settings is a bundle of commonly used resources used during the indexing and querying stage in a
# getting the api key from user input in streamlit
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

Settings.llm = OpenAI(api_key=api_key,temperature=temprature, model="gpt-3.5-turbo")


## multifile upload with streamlit
# get the file list
uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True)
if uploaded_files:
    # save the files to the data folder
    for uploaded_file in uploaded_files:
        with open(os.path.join("data", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.write("Files uploaded successfully")
# load data using SimpleDirectoryReader
# All files in the data folder are loaded into the index

    try:
        documents = SimpleDirectoryReader("data").load_data()

        index = VectorStoreIndex.from_documents(
            documents,

        )
        st.write(f"Number of documents: {len(documents)}")
    except Exception as e:
        st.write(f"Error loading the documents: {e}")
        st.warning("Please make sure you enter the correct API key")
        st.stop()



    # configure retriever
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=similarity_top_k,
    )

    # The response synthesizer is used to turn the response data into a human-readable format
    response_synthesizer = get_response_synthesizer(response_mode=ResponseMode.COMPACT)

    # The query engine is used to query the index and generate a response
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7, # filter nodes with similarity score below the cutoff 
                                                    filter_empty=True,  # filter empty nodes
                                                    filter_duplicates=True,  # filter duplicate nodes
                                                    filter_similar=True,  # filter similar nodes
                                                    )],
        response_synthesizer=response_synthesizer,                                                 
    )

    # Get user input
    query = st.text_area("Enter your query here:")
    if st.button("Submit"):
        response = query_engine.query(query)
        st.markdown(response)




