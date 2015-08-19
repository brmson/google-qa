#!/usr/bin/python

import sys
import subprocess
from time import sleep
import random
import json

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def main():
    argv = sys.argv
    input_filename = argv[1]
    output_filename = argv[2]
    json_data = open(input_filename)
    output = open(output_filename,"w")
    parsed_data = byteify(json.load(json_data))
    number_of_questions = len(parsed_data)
    question_counter = 0
    result_list = []
    json_result_list = []
    print("question\tanswer")
    while question_counter < number_of_questions:
        questionText = parsed_data[question_counter]["qText"]
        questionAnswers = parsed_data[question_counter]["answers"]
        ID = parsed_data[question_counter]["qId"]
        result = subprocess.check_output(["./google-query.sh", questionText]).rstrip()
        print(questionText+"\t"+result)
        d = {}
        d['qText'] = questionText
        d['answer'] = result
        result_list.append(d)
        sleep(1)
        question_counter = question_counter+1

    json_result_list = json.dumps(result_list)
    output.write(json_result_list)
    output.close()
    json_data.close()
    return

if __name__ == "__main__":
    main()