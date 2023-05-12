import json
from typing import List, Dict, Any, Optional

""" This class represents an input and output for a generation """
class Prompt:

	""" Initialize to contain and input, a continuation, and scores """
	def __init__(self, input_text: str, continuation: Optional[str] = None, scores: Optional[Dict[str, float]] = None):
		self.input_text = input_text
		self.continuation = continuation if continuation is not None else ''
		self.scores = scores if scores is not None else dict()

	""" Returns a dictionary representation """
	def dict(self) -> Dict[str, Any]:
		return {'Prompt': self.input_text, 'Continuation': self.continuation, 'Scores': self.scores}

""" This method returns the prompts from a json file """
def load_prompts(file: str) -> List[Prompt]:
	print(f'Loading prompts from "{file}"')
	prompts = []
	with open(file, 'r', encoding='utf8') as load:
		for row in load:
			row_json = json.loads(row)
			prompt = Prompt(input_text=row_json['prompt']['text'])
			prompts.append(prompt)
	print(f'Done loading {len(prompts)} prompts from "{file}"')
	return prompts