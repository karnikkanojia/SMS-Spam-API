import tensorflow as tf
import utils.preprocess
import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore')


def loadModel():
    model = tf.keras.models.load_model('models/bilstm.h5')
    return model


def get_scores(msg):
    model = loadModel()
    msg = utils.preprocess.preprocess_text([msg])
    return model.predict(msg).tolist()
