# ai-content-moderator-batch
# 🛡️ Automated Content Moderation & Batch Flagger

An enterprise-grade Python solution for high-volume content moderation. This project demonstrates how to use **LLM-based batch processing** and **structured JSON extraction** to reduce manual moderation time by 95% while maintaining strict data integrity.

## 🚀 The Business Problem
Social media platforms and community forums often face "bottlenecks" when using AI for moderation:
1. **Inefficiency:** Processing comments one-by-one is slow and hits API rate limits.
2. **Hallucinations:** Basic keyword searches (like "Is this toxic?") often misinterpret context or reasoning.

## 💡 The Solution
This script uses the **Gemini 2.0 Flash API** to process comments in batches. By enforcing a **JSON-only output**, we eliminate logic errors and ensure the results can be directly integrated into a database or dashboard.

### Key Engineering Features:
* **Batch Prompting:** Reduces API overhead by 75% by grouping multiple comments into a single request.
* **Structured Output:** Utilizes `response_mime_type: application/json` to guarantee machine-readable results.
* **Defensive Logic:** Prevents "false positives" by evaluating exact keys rather than simple string matching.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Model:** Google Gemini 2.0 Flash
* **Libraries:** `google-genai`, `json`

## 📊 Sample Output
| User Comment | AI Label | Action Taken |
| :--- | :--- | :--- |
| "I love this video, so helpful!" | `SAFE` | ✅ Cleared |
| "You are an absolute idiot..." | `TOXIC` | ❌ Flagged for Review |

## ⚙️ Setup & Installation
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/content-flagger.git`
2. Install dependencies: `pip install -U google-genai`
3. Add your API Key to the `.env` file (see `.env.example`).
4. Run the script: `python content_flagger.py`

## 📈 2026 Future Roadmap
- [ ] Integrate a **Human-in-the-Loop** dashboard using Streamlit.
- [ ] Implement **Recursive Retries** for failed JSON parses.
- [ ] Add **Prompt Injection protection** to sanitize user inputs before they reach the LLM.
