This script sends questions to google and retrieves results 
only from the QA module. You might get captchas if you overdo it.
It prints the results to the console and creates a JSON file
for later reviewing. When there is a wikipedia passage, we only consider the bold text as the answer.

To run this script, you should have one of our json datasets.
For example, moviesC from dataset-factoid-movies 

Then start it with:
	
	./google-eval.py input.json output.json

google_query can by used by itself, by calling query or queryAndDump (which also saves the website to a file) with the question as parameter.

	import google_query as q
	q.query("Who directed fight club?")

It is also extensible, you can add html attributes to the lists and increase the amount of found answers.

The moviesC-test-google.json dataset was created by using moviesC-test
from brmson/dataset-factoid-movies/moviesC on 2015-08-27.
See PERFORMANCE.md for the numbers as well as detailed evaluation.
