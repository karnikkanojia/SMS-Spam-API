import tensorflow as tf
import utils.preprocess
import warnings
import os
warnings.filterwarnings('ignore')


def loadModel():
    model = tf.keras.models.load_model('models/bilstm.h5')
    return model


def get_scores(msg):
    model = loadModel()
    msg = utils.preprocess.preprocess_text(msg)
    scores = model(msg).numpy()
    return scores.tolist()
