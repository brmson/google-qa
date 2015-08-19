This script sends questions to google and retrieves results 
only from the QA module. You might get captchas if you overdo it.
It prints the results to the console and creates a JSON file
for later reviewing.

To run this script, you should have one of our json datasets.
For example, moviesC from dataset-factoid-movies 

Then start it with:
	
	./google-eval.py input.json output.json

