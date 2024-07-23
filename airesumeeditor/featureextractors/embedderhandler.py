import json
from sentence_transformers import SentenceTransformer
from embedder_queue import queue_backend_embedder
from featureextractor import SentenceEmbedder
from collections import OrderedDict

class EmbedCV:
    def __init__(self, queue_list, embedding_model="all-mpnet-base-v2"):
        self.embeddings = {}
        self.queue_list = queue_list
        self.json_data = None
    
    def model_encode(self, text):
        return queue_backend_embedder(text, self.queue_list)

    def embed_segment(self, segment):
        title = segment["segment_title"]
        section_embeddings = {}

        # Special case for "skills" - combines into a single section
        # if title == "skills":
        #     text_to_embed = "\n".join(p["project_description"] for p in segment["section"])
        #     section_embeddings[title] = [self.model.encode(text_to_embed), []]  # No features for projects
            
        # else:
        #     for section in segment["section"]:
        #         features = [str(f) for f in section.values()]
        #         text_to_embed = "\n".join(features)
        #         section_embeddings[section["section_title"]] = [self.model.encode(text_to_embed), self.model.encode(features)]
        if title in ['header', 'education']:
            section_embeddings = None
        elif title in ['skills']:
            section_embeddings =  [" ".join([", ".join([skill_list for skill_list in section['skills']]) for section in segment['items']])]
        else:
            for section in segment['items']:
                features = section['features']
                text_to_embed = section['title']+ section['description'] +"\n".join(features)
                section_embeddings[section["title"]] = [
                    self.model_encode(text_to_embed), 
                    [self.model_encode(text) for text in features]
                    ]
        
        return {title: section_embeddings}

    def embed_all(self, json_data):
        self.json_data = json_data
        for segment in json_data:
            self.embeddings.update(self.embed_segment(segment))
        return True
        

    def add_to_queue(self, text):
        return queue_backend_embedder(text, self.queue_list)


class JDEmbed:

    def __init__(self):
        self.jd_embed = 0

class SegmentsHandler:

        def __init__(self, resume_embedding, jd_embedding, similarity_threshold=0.7):
            self.resume_embedding = resume_embedding
            self.similarity = SentenceEmbedder().similarity
            self.jd_embedding = jd_embedding
            self.similarity_threshold = similarity_threshold 

        def optimize_layout(self):
            layout = OrderedDict()
            
            for segment, section_data in self.resume_embedding.embeddings.items():
                layout[segment] = OrderedDict()
                section_scores = {}

                if segment not in ['education', 'header', 'skills']:
                    for section, (embedding, feature_embeddings) in section_data.items():
                        section_scores[section] = self.similarity(embedding, self.jd_embedding)

                    # Order sections by similarity (highest first)
                    ordered_sections = sorted(section_scores, key=section_scores.get, reverse=True)

                    for section in ordered_sections:
                        if section_scores[section] >= self.similarity_threshold:
                            layout[segment][section] = []
                            feature_scores = [self.similarity(feat_emb, self.jd_embedding) for feat_emb in feature_embeddings]

                            
                            for i, feature_score in enumerate(feature_scores):
                                layout[segment][section].append((i))
                        else:
                            layout[segment][section] = []
                             # Order and include features above the threshold
                            feature_scores = [self.similarity(feat_emb, self.jd_embedding) for feat_emb in feature_embeddings]

                           
                            for i, feature_score in enumerate(feature_scores):
                                if i==2:
                                    break
                                layout[segment][section].append(i) 

            return layout