import time

from pymilvus import MilvusClient

from pymilvus import Function, FunctionType 

from pymilvus import DataType 

# URI | Milvus server uri
uri = 'http://localhost:19530'

## Index params list
# List of dictionaries defining the indices to add to index params
# Here, we're only working with sparse vectors created with BM25
index_params_list = [
    {
        "field_name": "sparse",
        "index_type": "SPARSE_INVERTED_INDEX",
        "metric_type": "BM25",
        "params": {
            "inverted_index_algo": "DAAT_MAXSCORE",
            "bm25_k1": 3,   # Maximize importance of term frequency
            "bm25_b": 1     # Full normalization of docs
        }
    }
]

## BM25 embed function
# The function to get sparse embeddings from text
func_bm25 = Function(
    name="text_bm25_emb",
    input_field_names=["text"],
    output_field_names=["sparse"],
    function_type=FunctionType.BM25,
)

## Field params list
# List of dictionaries defining the fields to add to the schema
# This is how we describe our data:
# just need text and sparse vectors for this demo (full-text search only)
field_params_list = [
    {
        "field_name": "id", 
        "datatype": DataType.INT64, 
        "is_primary": True, 
        "auto_id": True
    },
    {
        "field_name": "text", 
        "datatype": DataType.VARCHAR, 
        "max_length": 1000, 
        "enable_analyzer": True
    },
    {
        "field_name": "sparse", 
        "datatype": DataType.SPARSE_FLOAT_VECTOR
    }
]

## Collection name
collection_name = 'collection_ex'

## Example data
# Default data to use for the insert method
data_ex = [
    {'text': 'information retrieval is a field of study.'},
    {'text': 'information retrieval focuses on finding relevant information in large datasets.'},
    {'text': 'data mining and information retrieval overlap in research.'},
    {'text': 'the rest of the lyrics go,'},
    {'text': 'Last night I dreamed about'}
]

## Query list
# Default list of queries to search the database
query_list = ["What's the focus of information retrieval?"]

## Result limit
# Default maximum number of results to get from search
lim_results = 3

## Initialize MilvusClient
def _init_client(
    self
):
    ## Define MilvusClient with PyMilvus library
    client = MilvusClient(
        uri=self.uri
    )
    return client

## Create field for schema
def _create_field(
    self, 
    schema, 
    params
):
    # Add the field to the schema for the given params
    schema.add_field(**params)

## Create index for index parameters
def _create_index(
    self, 
    index_params, 
    params
):
    # Add the index to the index params for the given params
    index_params.add_index(**params)

## List all client collections
def list_collections(
    self
):
    ## List all client collections
    collections = self.client.list_collections()
    return collections

## Create a collection for the client
def create_collection(
    self, 
    name = collection_name, 
    field_params_list = field_params_list, 
    func_list = [func_bm25], 
    index_params_list = index_params_list,
):
    ## Initialize the collection schema
    # Allow for adding different fields later on with enable_dynamic_field
    schema = self.client.create_schema(
        enable_dynamic_field=True,
    )

    ## Add all fields to the schema
    # This is how to describe the data
    for params in field_params_list:
        self._create_field(schema, params)

    ## Add all functions to the schema (embedding)
    # This is how to represent the data
    for func in func_list:
        schema.add_function(func)

    ## Add all indices to the index params
    # This is how to search the data
    index_params = self.client.prepare_index_params()
    for params in index_params_list:
        self._create_index(index_params, params)

    ## Create collection
    self.client.create_collection(
        collection_name=name,
        schema=schema,
        index_params=index_params
    )

## Drop a collection for the client
def drop_collection(
    self, 
    name = collection_name
):
    # Drop collection
    self.client.drop_collection(collection_name=name)

## Insert data into a collection
def insert(
    self, 
    name = collection_name, 
    data = data_ex
):
    # Insert data into the collection
    results = self.client.insert(
        collection_name=name,
        data=data
    )
    # Wait for the database to update
    time.sleep(0.5)

    ## Return results
    return results

## Delete data from a collection
def delete(
    self, 
    ids,
    name = collection_name, 
):
    # Delete data into the collection
    results = self.client.delete(
        collection_name=name,
        ids=ids
    )
    # Wait for the database to update
    time.sleep(0.5)

## Perform a full text search on a collection
def full_text_search(
    self, 
    name = collection_name, 
    query_list = query_list, 
    limit = lim_results
):
    ## Define search params
    # Only full-text so focus on sparse vectors built from text
    anns_field = 'sparse'
    output_fields = ['text']

    ## Add extra search params
    # Controls trade-off between speed and accuracy in ANN searches
    # Drop some percentage of results before searching
    search_params = {
        'params': {'drop_ratio_search': 0.2},
    }

    ## Get the search results
    results = self.client.search(
        collection_name=name, 
        data=query_list,
        anns_field=anns_field,
        output_fields=output_fields,
        limit=limit,
        search_params=search_params
    )
    return results

class MilvusClientInit:
    def __init__(
        self, 
        uri = uri
    ):
        self.uri = uri
        # Initialize MilvusClient from PyMilvus
        self.client = self._init_client()


    ## Initialize MilvusClient
    def _init_client(
        self
    ):
        ## Define MilvusClient with PyMilvus library
        client = MilvusClient(
            uri=self.uri
        )
        return client