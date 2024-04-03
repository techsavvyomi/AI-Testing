import os
import json

# Fetch inputs from environment variables
question = os.getenv('QUESTION')
reference_answer = os.getenv('REFERENCE_ANSWER')
student_answer = os.getenv('STUDENT_ANSWER')

# Evaluation Logic Placeholder
# Implement your evaluation logic here
# For demonstration, let's assume all provided answers get a perfect score
final_total_score = 10
mistakes = []  # List any identified mistakes here

# Output the result
result = {
    "Final Total Score": final_total_score,
    "Mistakes": mistakes
}

print(json.dumps(result))
