from flask import Flask, render_template, send_from_directory, request
import generation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data-report')
def data_report():
    images = [
        'distribution-of-song-length.png',
        'word-cloud.png',
        'distribution-song-name-length.png',
        'most-comman-words.png',
        'frequency-of-words.png',
        'distribution-of-unique-words-lyrics.png',
        'song-length-vs-unique-words.png',
        'training-loss-over-epochs.png',
        'training-accurcay-over-epochs.png'
    ]
    return render_template('data_report.html', images=images)

@app.route('/generate-lyrics', methods=['POST'])
def generate_lyrics():

    text = request.form['lyrics-input']

    generated_lyrics = generation.generate(text)

    return render_template('index.html', generated_lyrics=generated_lyrics)

@app.route('/download/<path:filename>', methods=['GET'])
def download_image(filename):
    return send_from_directory('static/images', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True , port = 5000)
