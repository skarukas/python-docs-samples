# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from typing import Optional

from vertexai.preview.rag import RagCorpus

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


def create_corpus_pinecone(
    pinecone_index_name: str,
    pinecone_api_key_secret_manager_version: str,
    display_name: Optional[str] = None,
    description: Optional[str] = None,
) -> RagCorpus:
    # [START generativeaionvertexai_rag_create_corpus_pinecone]

    from vertexai import rag
    import vertexai

    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # pinecone_index_name = "pinecone-index-name"
    # pinecone_api_key_secret_manager_version = "projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/latest"
    # display_name = "test_corpus"
    # description = "Corpus Description"

    # Initialize Vertex AI API once per session
    vertexai.init(project=PROJECT_ID, location="us-central1")

    # Configure embedding model (Optional)
    embedding_model_config = rag.RagEmbeddingModelConfig(
        vertex_prediction_endpoint=rag.VertexPredictionEndpoint(
            publisher_model="publishers/google/models/text-embedding-005"
        )
    )

    # Configure Vector DB
    vector_db = rag.Pinecone(
        index_name=pinecone_index_name,
        api_key=pinecone_api_key_secret_manager_version,
    )

    corpus = rag.create_corpus(
        display_name=display_name,
        description=description,
        backend_config=rag.RagVectorDbConfig(
            rag_embedding_model_config=embedding_model_config,
            vector_db=vector_db,
        ),
    )
    print(corpus)
    # Example response:
    # RagCorpus(name='projects/1234567890/locations/us-central1/ragCorpora/1234567890',
    # display_name='test_corpus', description='Corpus Description', embedding_model_config=...
    # ...

    # [END generativeaionvertexai_rag_create_corpus_pinecone]
    return corpus


if __name__ == "__main__":
    create_corpus_pinecone(
        pinecone_index_name="pinecone-index-name",
        pinecone_api_key_secret_manager_version="projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/latest",
        display_name="test_corpus",
        description="Corpus Description",
    )
