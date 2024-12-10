from flask import Flask, request, jsonify
from behavior_analysis import analyze_behavior
from code_evaluation import evaluate_code
from scoring import calculate_score

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.json
        # Behavioral Analysis
        behavior = analyze_behavior(data["response"])
        # Code Evaluation
        code_result = evaluate_code(data["code"], data["language_id"])
        # Scoring
        final_score = calculate_score(
            technical_score=code_result['status']['id'], 
            behavioral_score=behavior['confidence'], 
            aptitude_score=data['aptitude_score']
        )
        return jsonify({
            "behavior": behavior, 
            "code": code_result, 
            "final_score": final_score
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


