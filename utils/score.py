import tensorflow as tf
import utils.preprocess
import warnings
warnings.filterwarnings('ignore')


def loadModel():
    model = tf.keras.models.load_model('models/bilstm.h5')
    return model


def get_scores(msg):
    model = loadModel()
    msg = utils.preprocess.preprocess_text([msg])
    scores = model.predict(msg)
    return scores.tolist()
