import joblib
import os
import re  # <--- WE NEED THIS

# 1. Setup Paths
current_dir = os.getcwd()
model_path = os.path.join(current_dir, "models", "ticket_pipeline.joblib")

print(f"🔎 Loading model from: {model_path}")

# 2. Define the SAME cleaning function used in training
def clean_text(text):
    text = str(text).lower()                 # Lowercase
    text = re.sub(r'[^a-z\s]', '', text)     # Remove punctuation/numbers
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra spaces
    return text

# 3. Load & Test
try:
    pipeline = joblib.load(model_path)
    
    # RAW input
    raw_text = "work experience user work experience user hi work experience student coming next his name much appreciate him duration thank."
    
    # CLEAN it first!
    cleaned_input = clean_text(raw_text)
    
    # Predict
    prediction = pipeline.predict([cleaned_input])[0]
    
    print(f"\n📝 Raw Input:   '{raw_text}'")
    print(f"🧹 Cleaned Input: '{cleaned_input}'")
    print(f"🔮 Prediction:    {prediction}")
    
    if prediction == "HR Support":
        print("\n✅ IT WORKS! The model just needed clean text.")
    else:
        print("\n❌ STILL FAILING. The model might need retraining.")

except Exception as e:
    print(f"❌ Error: {e}")