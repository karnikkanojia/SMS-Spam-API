import pickle
import tensorflow as tf 

PAD_TYPE = 'post'
TRUNC_TYPE = 'post'
MAX_LEN = 98

def load_tokenizer():
    with open('models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

def text_to_sequence(msg, tokenizer):
    tokenizer = load_tokenizer()
    text_sequence = tokenizer.texts_to_sequences(msg)
    text_padded = tf.keras.preprocessing.sequence.pad_sequences(text_sequence, maxlen=MAX_LEN, padding=PAD_TYPE, truncating=TRUNC_TYPE)
    return text_padded

def preprocess_text(msg):
    tokenizer = load_tokenizer()
    sequence = text_to_sequence(msg, tokenizer)
    return sequence