from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Media Research Archive</title>
    <style>
        body { background: #1a1a1a; color: #e0e0e0; font-family: 'Courier New', monospace; display: flex; flex-direction: column; align-items: center; padding: 40px; }
        .box { width: 90%; max-width: 900px; border: 1px solid #444; padding: 20px; background: #222; border-radius: 5px; }
        input { width: 70%; padding: 10px; background: #333; border: 1px solid #555; color: white; }
        button { padding: 10px 20px; background: #444; color: white; border: 1px solid #666; cursor: pointer; }
        button:hover { background: #555; }
        .video-frame { margin-top: 20px; width: 100%; aspect-ratio: 16/9; background: #000; }
        iframe { width: 100%; height: 100%; border: none; }
        .status { color: #888; font-size: 12px; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="box">
        <h3>System Asset Loader</h3>
        <form method="POST">
            <input type="text" name="url" placeholder="Paste Mirror URL here..." required>
            <button type="submit">Fetch Data</button>
        </form>
        <div class="video-frame">
            <iframe src="{{ final_url }}" allowfullscreen></iframe>
        </div>
        <p class="status">Source Tunnel: Active</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    # This is a random sample from a mirror instance
    display_url = "" 
    if request.method == 'POST':
        display_url = request.form.get('url')
    return render_template_string(HTML_TEMPLATE, final_url=display_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
