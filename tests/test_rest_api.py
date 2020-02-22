"""
This module contains basic REST API tests using requests.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import requests


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_duckduckgo_instant_answer_api():
  r = requests.get('https://api.duckduckgo.com/?q=python+programming&format=json')
  body = r.json()
  assert r.status_code == 200
  assert 'Python' in body['AbstractText']


def test_recipe_puppy_api():
  r = requests.get('http://www.recipepuppy.com/api/?i=onions,garlic')
  body = r.json()
  assert r.status_code == 200
  assert body['title'] == 'Recipe Puppy'
  assert len(body['results']) > 0
