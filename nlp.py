from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from faq_data import FAQ_DATA
from config import MODEL_NAME, CONFIDENCE_THRESHOLD

model = SentenceTransformer(MODEL_NAME)

faq_questions = list(FAQ_DATA.keys())
faq_embeddings = model.encode(faq_questions)

def get_response(user_message):
    try:
        user_embedding = model.encode([user_message])
        similarities = cosine_similarity(user_embedding, faq_embeddings)[0]
        
        best_index = np.argmax(similarities)
        best_score = similarities[best_index]
        
        if best_score >= CONFIDENCE_THRESHOLD:
            return FAQ_DATA[faq_questions[best_index]]
        else:
            return "I'm not confident about that. Please contact support."
    
    except Exception as e:
        return f"Error processing request: {str(e)}"
