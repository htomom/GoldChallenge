# import module
import pandas as pd
import re
from flask import Flask, jsonify
from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)

# connect data abusive dan kamus alay
df_abusive = pd.read_csv("D:/Binar/Challenge/BinarChallenge1/AssetChallenge/abusive.csv")
df_abusive

df_kbbi = pd.read_csv("D:/Binar/Challenge/BinarChallenge1/AssetChallenge/new_kamusalay.csv", encoding='latin-1', names=['TIDAKBAKU', 'BAKU'])
df_kbbi


# fungsi cleaning
def lowercase(text):
    return text.lower()

def removechars(text):
    text = re.sub('\n',' ',text) 
    text = re.sub('RT',' ',text) 
    text = re.sub('user',' ',text) 
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text)
    text = re.sub('  +', ' ', text)  
    return text

def removenothers(text):
    text = re.sub('[^0-9a-zA-Z~*#?!]+', ' ', text) 
    return text

# fungsi cleaning censor kata kasar dan ubah kalimat alay
def changealay(text):
    alay = dict(zip(df_kbbi['TIDAKBAKU'], df_kbbi['BAKU']))
    text = ' '.join([alay[word] if word in alay else word for word in text.split(' ')])
    return text

def censor(text):
    abusiveword = df_abusive['ABUSIVE'].tolist()
    for word in abusiveword:
        pattern = re.compile(r'\b{}\b'.format(word))
        length = len(word)
        replacement = '*' * length
        text = pattern.sub(replacement, text.lower())
    return text


def cleaning(text):
    text = removechars(text)
    text = lowercase(text)
    text = removenothers(text)
    text = changealay(text)
    text = censor(text)
    return text

# --- start swagger---

# aplikasi swagger 
app.json_encoder = LazyJSONEncoder
swagger_template = dict(
info = {
    'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
    'version': LazyString(lambda: '1.0.0'),
    'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)


# endpoint 1
@swag_from("text_processing.yml", methods=['POST'])
@app.route('/text_processing', methods=['POST'])
def text_clean():

    text = request.form.get('text')

    json_response = {
        'status_code': 200,
        'description': "Hasil teks yang sudah dibersihkan",
        'data': cleaning(text)
    }

    response_data = jsonify(json_response)
    return response_data

# endpoint 2
@swag_from("text_processing_file.yml", methods=['POST'])
@app.route('/text_processing_file', methods=['POST'])
def processing_file():

    # Uploaded file
    file = request.files.getlist('file')[0]

    # Import file csv ke Pandas
    df = pd.read_csv(file, encoding='latin-1')


    # Lakukan cleansing pada teks
    cleaned_text = []
    for text in df['Tweet']:
        cleaned_text.append(cleaning(text))

    json_response = {
        'status_code': 200,
        'description': "Teks yang sudah diproses",
        'data': cleaned_text
    }

    response_data = jsonify(json_response)
    return response_data

if __name__ == '__main__':
   app.run()

# --- end swagger ---