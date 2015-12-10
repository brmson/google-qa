#!/usr/bin/python -u

import json
import os
import re
import sys

def intersect(a, b):
     return list(set(a) & set(b))

def date_reformat(date):
     return os.popen('date +%F -d "'+date.encode('utf8')+'" 2>/dev/null').read().rstrip()

argv = sys.argv
gs_filename = argv[1]
answers_filename = argv[2]
gs_data = open(gs_filename)
answers_data = open(answers_filename)

gs_json = json.load(gs_data)
answers_json = json.load(answers_data)
number_of_questions = len(gs_json)
correctly_answered = 0
for x in range(0, number_of_questions):
    if len(answers_json[x]['answer']) == 0:
        i = 1
    elif len(answers_json[x]['answer']) == 1:
        for gs_answer in gs_json[x]['answers']:
            ans = answers_json[x]['answer'][0]
            if re.search(gs_answer, ans, re.IGNORECASE) or \
               re.search(gs_answer, date_reformat(ans), re.IGNORECASE):
                correctly_answered = correctly_answered + 1
                break
        else:
            print
            print "question " + answers_json[x]['qId'] + " " + answers_json[x]['query']
            print "incorrect answer, expected " + gs_json[x]['answers'][0]
            print "                       got " + answers_json[x]['answer'][0] 
    else:
        number_of_answers = min(len(answers_json[x]['answer']), len(gs_json[x]['answers']))
        m_answers = [val for val in answers_json[x]['answer'] if val in gs_json[x]['answers']]
        matched_answers = len(m_answers)
        if matched_answers > 0:	
            correctly_answered = correctly_answered + 1
        else:
            print
            print "question " + answers_json[x]['qId'] + " " + answers_json[x]['query']
            print "no match, expected " + ' '.join(gs_json[x]['answers'])
            print "               got " + ' '.join(answers_json[x]['answer'])
        #print "matched " + str(matched_answers) + " out of " + str(number_of_answers)
print "estimating " + str(correctly_answered) + " correct answers out of " + str(number_of_questions)
answer_ratio = float(correctly_answered)/number_of_questions * 100
print str (number_of_questions - correctly_answered) + " incorrect"
print str(answer_ratio) + "%"
