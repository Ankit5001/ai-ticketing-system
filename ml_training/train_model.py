import pandas as pd
import joblib
import os
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# ==========================================
# 1. CONFIGURATION
# ==========================================
CSV_FILENAME = 'large_ticket_dataset.csv'
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, CSV_FILENAME)
models_dir = os.path.join(os.path.dirname(current_dir), 'models')
os.makedirs(models_dir, exist_ok=True)

# ==========================================
# 2. LOAD & CLEAN DATA
# ==========================================
print(f"⏳ Loading {CSV_FILENAME}...")
if not os.path.exists(csv_path):
    print("❌ Error: CSV not found. Run generate_data.py first!")
    exit()

df = pd.read_csv(csv_path)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['clean_text'] = df['Document'].apply(clean_text)
df = df.dropna(subset=['clean_text', 'Topic_group', 'Priority'])
print(f"✅ Loaded {len(df)} rows.")

# ==========================================
# 3. DEFINE THE 3 MODELS
# ==========================================
# 1. Random Forest (The Decision Maker)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# 2. SVM (The Line Drawer - fast and accurate for text)
svm = SVC(kernel='linear', probability=True, random_state=42)

# 3. Neural Network (The Brain - Multi-Layer Perceptron)
#    - 64 neurons in hidden layer
#    - 'relu' activation (standard for AI)
#    - max_iter=500 to give it time to learn
nn = MLPClassifier(hidden_layer_sizes=(64,), activation='relu', max_iter=500, random_state=42)

# ==========================================
# 4. BUILD & TRAIN DEPARTMENT ENSEMBLE
# ==========================================
print("\n⚙️  Training Department Ensemble (RF + SVM + Neural Net)...")

# We create a "Voting System"
dept_voting = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('svm', svm),
        ('nn', nn)
    ],
    voting='hard' # 'hard' means Majority Vote (2 vs 1 wins)
)

dept_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('ensemble', dept_voting)
])

X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['Topic_group'], test_size=0.2)
dept_pipeline.fit(X_train, y_train)

print("📊 Department Accuracy:")
print(classification_report(y_test, dept_pipeline.predict(X_test)))

# Save
joblib.dump(dept_pipeline, os.path.join(models_dir, 'ticket_pipeline.joblib'))

# ==========================================
# 5. BUILD & TRAIN PRIORITY ENSEMBLE
# ==========================================
print("\n⚙️  Training Priority Ensemble (RF + SVM + Neural Net)...")

prio_voting = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('svm', svm),
        ('nn', nn)
    ],
    voting='hard'
)

prio_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('ensemble', prio_voting)
])

X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(df['clean_text'], df['Priority'], test_size=0.2)
prio_pipeline.fit(X_train_p, y_train_p)

print("📊 Priority Accuracy:")
print(classification_report(y_test_p, prio_pipeline.predict(X_test_p)))

# Save
joblib.dump(prio_pipeline, os.path.join(models_dir, 'priority_pipeline.joblib'))

print("\n✅ SUCCESS: Ensemble Models Saved! (You don't need to change main.py)")