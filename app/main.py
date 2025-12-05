from flask import Flask, jsonify, redirect, request
from app.utils import is_valid_url, normalize_url
from app import models

app = Flask(__name__) 

@app.route('/') 
def health_check(): 
    return jsonify({ 
        "status": "healthy", 
        "service": "URL Shortener API" 
    }) 

@app.route('/api/health') 
def api_health(): 
    return jsonify({ 
        "status": "ok", 
        "message": "URL Shortener API is running" 
    }) 

# Shorten URL Endpoint
@app.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' in request body"}), 400
    
    raw_url = data["url"]
    if not is_valid_url(raw_url):
            return jsonify({"error": "Invalid URL. Provide a full http/https URL."}), 400

    long_url = normalize_url(raw_url)
    short_code = models.create_mapping(long_url)

    short_url = request.host_url.rstrip("/") + "/" + short_code 

    return jsonify({"short_code": short_code, "short_url": short_url}), 201

# Redirect Endpoint
@app.route("/<short_code>", methods=["GET"])
def redirect_short(short_code):
    mapping = models.get_mapping(short_code)
    if mapping is None:
        return jsonify({"error": "Short code not found"}), 404
    
    # increment click count
    models.increment_clicks(short_code)

    # Redirect to the original URL (temporary redirect)
    return redirect(mapping["url"], code=302)

    # Analytics endpoints
@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    mapping = models.get_mapping(short_code)
    if mapping is None:
        return jsonify({"error": "Short code not found"}), 404
         
    return jsonify({
        "url": mapping["url"],
        "clicks": mapping["clicks"],
        "created_at": mapping["created_at"]
    }), 200
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)

