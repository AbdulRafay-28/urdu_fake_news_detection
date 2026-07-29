from pathlib import Path
from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

# ==========================
# Paths
# ==========================


MODEL_PATH = BASE_DIR / "models" / "distilbert_model"

print("=" * 50)
print("Loading Model...")
print("Model Path:", MODEL_PATH)
print("=" * 50)

# ==========================
# Check Model Folder
# ==========================

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model folder not found:\n{MODEL_PATH}")

# ==========================
# Load Tokenizer
# ==========================

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

# ==========================
# Load Model
# ==========================

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model.to(device)
model.eval()

print("✅ Model Loaded Successfully!")

# ==========================
# Prediction Function
# ==========================

def predict_news(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = F.softmax(outputs.logits, dim=1)

    prediction = torch.argmax(outputs.logits, dim=1).item()

    confidence = probabilities[0][prediction].item() * 100

    if prediction == 1:
        label = "REAL NEWS ✅"
        color = "success"
    else:
        label = "FAKE NEWS ❌"
        color = "danger"

    return label, confidence, color

# ==========================
# Home Page
# ==========================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    color = None
    news = ""

    if request.method == "POST":

        news = request.form.get("news", "").strip()

        if news:

            prediction, confidence, color = predict_news(news)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        color=color,
        news=news
    )

# ==========================
# Run
# ==========================

if __name__ == "__main__":
    app.run(debug=True)