import json
from sentence_transformers import SentenceTransformer
from embedder_queue import queue_backend_embedder

class EmbedCV:
    def __init__(self, json_file_path, queue_list, embedding_model="all-mpnet-base-v2"):
        with open(json_file_path, 'r') as f:
            self.json_data = json.load(f)
        self.embeddings = {}
        self.queue_list = queue_list

    def embed_segment(self, segment):
        title = segment["segment_title"]
        section_embeddings = {}

        # Special case for "Projects" - combines into a single section
        if title == "projects":
            text_to_embed = "\n".join(p["project_description"] for p in segment["section"])
            section_embeddings[title] = [self.model.encode(text_to_embed), []]  # No features for projects
            
        else:
            for section in segment["section"]:
                features = [str(f) for f in section.values()]
                text_to_embed = "\n".join(features)
                section_embeddings[section["section_title"]] = [self.model.encode(text_to_embed), self.model.encode(features)]

        return {title: section_embeddings}

    def embed_all(self):
        for segment in self.json_data:
            self.embeddings.update(self.embed_segment(segment))
        

    def add_to_queue(self, text):
        return queue_backend_embedder(text, self.queue_list)
