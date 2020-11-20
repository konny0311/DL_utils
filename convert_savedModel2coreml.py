import tensorflow as tf
import tensorflow_hub as tf_hub
import numpy as np
import coremltools as ct

saved_model_dir = "coreml_save_trial"
# model = tf.keras.models.load_model(saved_model_dir)
mlmodel = ct.convert(saved_model_dir)
mlmodel.save("ssd.mlmodel")
