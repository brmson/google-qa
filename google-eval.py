#!/usr/bin/python

from __future__ import print_function

import sys
import google_query as q
from time import sleep
import json


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

if __name__ == "__main__":
    argv = sys.argv
    input_filename = argv[1]
    output_filename = argv[2]

    json_data = open(input_filename)
    output = open(output_filename, "w")
    parsed_data = byteify(json.load(json_data))
    number_of_questions = len(parsed_data)

    question_counter = 0
    answered = 0
    result_list = []
    print("question\t\tanswer")
    print('[', file=output)
    while question_counter < number_of_questions:
        questionText = parsed_data[question_counter]["qText"]
        questionAnswers = parsed_data[question_counter]["answers"]
        ID = parsed_data[question_counter]["qId"]
        result = q.query(questionText)
        if len(result) > 0:
            answered = answered + 1
            print(questionText+"\t"+','.join(result))
        else:
            print(questionText+"\t"+"answer not found")
        d = {}
        d['qId'] = ID
        d['query'] = questionText
        d['answer'] = result
        if question_counter < number_of_questions-1:
            print('  %s,' % (json.dumps(d, sort_keys=True),), file=output)
        else:
            print('  %s' % (json.dumps(d, sort_keys=True),), file=output)
        sleep(2)
        question_counter = question_counter+1
    print ("answered " + str(answered) + " questions from " + str(number_of_questions))
    print(']', file=output)
    output.close()
    json_data.close()
