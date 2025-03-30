import tensorflow as tf
import numpy as np
from models.model_fit_request import ModelFitRequestPair

tempai_model = None

def __create_model():
    global tempai_model
    layer = tf.keras.layers.Dense(units=3, input_shape=[1])
    hidden = tf.keras.layers.Dense(units=3)
    output_layer = tf.keras.layers.Dense(units=1)
    tempai_model = tf.keras.Sequential([layer,hidden, output_layer])

    tempai_model.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

def model_fit(train_data: list[ModelFitRequestPair]):
    global tempai_model
    celsius = np.array([p.celsius for p in train_data], dtype=float)
    fahrenheit = np.array([p.fahrenheit for p in train_data], dtype=float)

    if tempai_model is None:
        __create_model()
    history = tempai_model.fit(celsius, fahrenheit, epochs=100, verbose=False)


def model_predict(celsius: float) -> float:
    global tempai_model
    if (tempai_model is None):
        raise Exception('It is necessary to train the AI model firts')
    
    return tempai_model.predict(np.array([celsius]))
    