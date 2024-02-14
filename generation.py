import pickle
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
import numpy as np

with open('model-files/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

with open("model-files/model_architecture.json", "r") as json_file:
    loaded_model_json = json_file.read()
model = model_from_json(loaded_model_json)

model.load_weights("model-files/model_weights.h5")

with open('model-files/vocabulary_size.txt', 'r') as f:
    total_words = int(f.read())


def generate(seed_text):
    next_words = 100
    generated_text = seed_text
    max_sequence_len = model.layers[0].input_shape[1] + 1
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
        generated_text += " " + output_word
    print(generated_text)
    return(generated_text)