import tensorflow as tf

print("Loading model...")

model = tf.keras.models.load_model("corruption_ann_model.h5")

print("Model loaded successfully")
