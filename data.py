import requests
import html

question_req = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_req.raise_for_status()
question_data = question_req.json()['results']
q_and_a = [ {"text":html.unescape(question['question']),"answer":question['correct_answer']} for question in question_data]
