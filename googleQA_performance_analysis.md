GoogleQA performance analysis

Using our moviesC-test dataset, Google correctly answered 140 out of 233 questions.
We tested this by matching our results against the gold standard answers in the dataset itself. Whenever we encountered a list of answers 
(e.g. a list a movies),
one match would count as a correct answer. The accuracy is 60.0858369099%.

Out of the 93 incorrectly answered questions, 8 had the wrong date format,
case or missed a substring. For example, "When was Fight Club produced" returned "1999", while the GS expected "1999-09-10", 
"Piano" didn't match against "piano" and "How the Grinch Stole Christmas!" didn't match "Dr. Seuss' How the Grinch Stole Christmas"

After further analysis, we deemed 10 questions in our gold standard to be factually incorrect. Google answered correctly in those cases.

examples:
	
	who plays ken barlow in coronation street?
	gold standard: Tony Warren
	actual answer: William Roache

	who will play mr gray in the film?
	gold standard: Karen Mulder
	actual answer: Dornan

	who did the voice of darth vader in episode 3?
	gold standard: Hayden Christensen
	actual answer: James Earl Jones

	who does alyson stoner play in camp rock?
	gold standard: Caitlyn Gellar
	actual answer: Caitlyn Geller

	who plays caesar flickerman in the hunger games?
	gold standard: Art Conforti
	actual answer: Stanley Tucci

	who plays roxanne in ghost rider?
	gold standard: Daryl Hannah
	actual answer: Raquel Alessi, Eva Mendes

	who played donna on west wing?
	gold standard: Catherine Tate
	actual answer: Janel Moloney

	who does kellan lutz play in prom night?
	gold standard: Mark Rider
	actual answer: Rick Leland

	who played darth vader at the end of return of the jedi?
	gold standard: James Earl Jones
	actual answer: Sebastian Shaw

	what movies did joan crawford play in?
	gold standard: Children’s Hospital Los Angeles
	actual answer: <list of movies>
	
There were other ambiguous questions, but we ignored those as noise.
The mechanical comparison was done using gold_standard_comparison.py

	python gold_standard_comparison.py moviesC-test.json moviesC-test-google.json