# LyricGen: Deep Learning Powered Song Lyrics Generation and Exploration Platform

## Project Title: LyricGen

### Description:
LyricGen is an innovative platform designed to explore the vast world of song lyrics using advanced machine learning techniques. With a dataset comprising over 55,000 songs sourced from Spotify, LyricGen offers a unique opportunity to delve into the nuances of lyrical composition and generate new lyrics using cutting-edge neural network models.

The platform begins with an extensive Exploratory Data Analysis (EDA) phase, where users can uncover insightful trends and patterns within the dataset. Visualizations such as histograms, word clouds, and sentiment analysis graphs provide a comprehensive understanding of the lyrical landscape.

Utilizing state-of-the-art neural network architectures, LyricGen's backend employs Natural Language Processing (NLP) techniques to train a model capable of generating coherent and contextually relevant song lyrics. Users can input prompts or themes to inspire the model, resulting in the creation of original lyrical compositions.

In addition to its lyric generation capabilities, LyricGen features a user-friendly web interface built with Flask, HTML, and CSS. The interface includes a sleek homepage welcoming users to the platform and a data report page showcasing the insights derived from the EDA phase. Users can conveniently download the generated graphs and visualizations for further analysis or presentation purposes.

Whether you're a songwriter seeking inspiration, a music enthusiast interested in lyrical analysis, or a data scientist exploring the intersection of music and technology, LyricGen offers a captivating journey through the world of song lyrics. Dive into the depths of musical expression and unlock the potential of AI-driven creativity with LyricGen.

### How to Start:

#### For Mac:

1. Create a virtual environment:
   ```bash
   python3 -m venv env

2. Activate the virtual environment:
   ```bash
   source env/bin/activate #Mac
   .\env\Scripts\activate  #windows

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Start the Flask app:
   ```bash
   python app.py

Once the Flask app is running, you can access it through your web browser by navigating to http://localhost:5000/. The website will provide two options in the taskbar: "Home" and "Data Report." Clicking on "Data Report" will display various graphs generated from the EDA, and you can download the report by clicking on the appropriate buttons.
