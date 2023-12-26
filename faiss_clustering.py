paragraphs = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial Intelligence has been a subject of intrigue for decades.",
    "The history of Python dates back to the late 1980s.",
    "Machine learning and deep learning drive modern AI.",
    "Natural language processing enables computers to understand human language.",
    "Climate change is impacting ecosystems worldwide.",
    "The exploration of Mars has revealed much about the history of the planet.",
    "Quantum computing holds the potential to revolutionize technology.",
    "Blockchain technology is transforming digital transactions.",
    "Renewable energy sources are becoming increasingly vital.",
    "The study of genetics has advanced our understanding of human health.",
    "Autonomous vehicles could reshape transportation.",
    "Virtual reality offers new possibilities in gaming and education.",
    "The Internet of Things connects everyday devices to the web.",
    "Cybersecurity is crucial in the digital age.",
    "3D printing is changing manufacturing processes.",
    "Augmented reality blends the digital and physical worlds.",
    "Big data analytics helps in understanding complex patterns.",
    "The human brain is an intricate organ still being studied.",
    "Advances in medicine are prolonging life expectancy.",
    "Robotics technology is automating various industries.",
    "Sustainable farming practices are essential for food security.",
    "The psychology of motivation is a complex study.",
    "Urban planning is key to sustainable city development.",
    "The art world continuously evolves with cultural shifts.",
    "Conservation efforts are crucial for endangered species.",
    "Space travel has always captivated human imagination.",
    "Nanotechnology is finding applications in multiple fields.",
    "Philosophy challenges our understanding of existence.",
    "Mathematics is the language of the universe.",
    "Literature reflects the human condition in diverse ways.",
    "The history of cinema offers insight into cultural changes.",
    "Music is a universal language that transcends boundaries.",
    "Photography captures moments and tells stories.",
    "Oceanography is essential for understanding marine ecosystems.",
    "Sports bring people together across the world.",
    "Cooking is both an art and a science.",
    "Fashion reflects both personal style and cultural trends.",
    "Architecture combines functionality with aesthetics.",
    "Linguistics explores the structure and evolution of language.",
    "Anthropology studies human societies and cultural diversity.",
    "The immune system is vital for human health.",
    "Astrophysics seeks to understand the universe's workings.",
    "Psychiatry plays a crucial role in mental health.",
    "Geology helps us understand Earth's history and future.",
    "The digital revolution has transformed how we communicate.",
    "Environmental science is key to addressing ecological issues.",
    "Astronomy has been practiced since ancient times.",
    "Sociology examines the behavior of societies.",
    "Biotechnology is advancing the capabilities of medical treatment."
]

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = np.array(model.encode(paragraphs)).astype('float32')

d = embeddings.shape[1]  # Dimensionality of vectors

# Using a flat index for simplicity; FAISS supports many types of indices
index = faiss.IndexFlatL2(d)
index.add(embeddings)

query_sentence = "Programming languages like Python have revolutionized software development."
query_embedding = np.array(model.encode([query_sentence])).astype('float32')

k = 5  # Number of nearest neighbors to retrieve
D, I = index.search(query_embedding, k)

print("Query:", query_sentence)
for i in range(k):
    print(f"{i + 1}: Paragraph: '{paragraphs[I[0][i]]}', Distance: {D[0][i]}")