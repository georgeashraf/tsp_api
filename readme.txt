Activate the virtual environment:

for window: venv\Scripts\activate
for linux: source venv/bin/activate

to run server:
    hupper -m waitress --port={port} server:app
example : hupper -m waitress --port=8000 server:app

the api support get/post requests:
GET: http://localhost:8000/   "returns the result for a pre defined array of points"

POST: http://localhost:8000/ "returns the result for an array of points sent in request body as follows"

{
    "input":[[0,0],[2,2],[9,9],[5,5]]
  
}