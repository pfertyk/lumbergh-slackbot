from flask import Flask, request, Response, jsonify

app = Flask(__name__)
link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'


@app.route('/lumbergh', methods=['POST'])
def lumbergh():
    text = request.form.get('text', '')
    if 'that would be great' in text.lower() and link not in text:
        return jsonify(text=link)
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
