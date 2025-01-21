from llama_index.core import VectorStoreIndex, Document
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss


def create_and_save_index_with_faiss(documents, storage_path="index_storage", faiss_index_path="faiss_index.bin"):
    dimension = 1536
    faiss_index = faiss.IndexFlatL2(dimension)
    vector_store = FaissVectorStore(faiss_index)
    index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)
    faiss.write_index(faiss_index, faiss_index_path)
    index.storage_context.persist(storage_path)


def load_index_and_query_with_faiss(query, storage_path="index_storage", faiss_index_path="faiss_index.bin"):
    faiss_index = faiss.read_index(faiss_index_path)
    vector_store = FaissVectorStore(faiss_index)
    storage_context = StorageContext.from_defaults(persist_dir=storage_path)
    index = load_index_from_storage(storage_context, vector_store=vector_store)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response.response
