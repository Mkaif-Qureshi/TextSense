from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import io
import base64
import boto3

app = Flask(__name__)
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id='ACCESS_KEY', aws_secret_access_key='ACCESS_KEY')
def extract_text_from_image(image_bytes):
    aws_mag_con = boto3.session.Session(profile_name='IAM_USER_NAME')
    textract_client = aws_mag_con.client(service_name='textract', region_name='us-east-1')

    response = textract_client.detect_document_text(Document={'Bytes': image_bytes})
    extracted_text = " ".join(item['Text'] for item in response['Blocks'] if item['BlockType'] == 'WORD')

    return extracted_text

def analyze_sentiment(text_to_analyze):
    aws_mag_con = boto3.session.Session(profile_name="IAM_USER_NAME")
    client = aws_mag_con.client(service_name="comprehend", region_name="us-east-1")

    if text_to_analyze:
        response = client.detect_sentiment(Text=text_to_analyze, LanguageCode='en')

        sentiment = response['Sentiment']
        sentiment_score = response['SentimentScore']

        formatted_score = f"Positive: {sentiment_score['Positive']}\n" \
                          f"Negative: {sentiment_score['Negative']}\n" \
                          f"Neutral: {sentiment_score['Neutral']}\n" \
                          f"Mixed: {sentiment_score['Mixed']}"

        result_str = (
            f'The prominent sentiment is: {sentiment}\n'
            f'The SentimentScore is:\n{formatted_score}'
        )

        return result_str
    else:
        return "Please enter some text for sentiment analysis."


# Function to translate text
def translate_text(text_to_translate, target_language):
    aws_mag_con = boto3.session.Session(profile_name="IAM_USER_NAME")
    client = aws_mag_con.client(service_name="translate", region_name="us-east-1")

    try:
        response = client.translate_text(
            Text=text_to_translate,
            SourceLanguageCode='en',
            TargetLanguageCode=target_language
        )

        translated_text = response.get('TranslatedText')
        return translated_text

    except Exception as e:
        return str(e)


@app.route('/')
def index():
    extracted_text = request.args.get('extracted_text', '')
    # image_data = request.args.get('image', '')

    # return render_template('index.html', extracted_text=extracted_text, image_data=image_data)
    return render_template('index.html', extracted_text=extracted_text)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part', 400

    image_file = request.files['image']

    if image_file.filename == '':
        return 'No selected file', 400

    if image_file:
        # Read the image file
        image_bytes = image_file.read()
        s3.upload_fileobj(image_file, 'BUCKET_NAME', image_file.name)
        # Convert image bytes to base64
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')

        # Extract text from the image
        extracted_text = extract_text_from_image(image_bytes)

        # Redirect to index.html with extracted text and image data as form data
        return redirect(url_for('index', _anchor='result', extracted_text=extracted_text))

    return 'Error processing file', 500

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_endpoint():
    text_to_analyze = request.form.get('extracted_text', '')

    result_str = analyze_sentiment(text_to_analyze)

    return result_str

@app.route('/translate_text', methods=['POST'])
def translate_text_endpoint():
    text_to_translate = request.form.get('extracted_text', '')
    target_language = request.form.get('target_language', '')

    translated_text = translate_text(text_to_translate, target_language)
    return translated_text

if __name__ == '__main__':
    app.run(debug=True)
