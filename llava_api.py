from flask import Flask, request, jsonify
import base64
import ollama

app = Flask(__name__)

@app.route('/describe', methods=['POST'])
def describe_image():
    data = request.get_json()
    image_base64 = data.get("image", "")

    if not image_base64:
        return jsonify({"error": "No image provided"}), 400

    # Send Image to LLaVA for Analysis
    response = ollama.chat(
        model="llava",
        messages=[{"role": "user", "content": "Describe this image."}],
        images=[image_base64]  # ✅ Use Base64 string, NOT bytes
    )

    print("Response from LLaVA:", response)  # Debugging step

    # Safely extract response message
    description = response.get("message", {}).get("content", "No description available.")

    return jsonify({"description": description})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


