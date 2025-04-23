# Final_Project
BCOG200 final project
1. For my final project, I will be creating an interactive quiz that determines whether users are more "left-brained" or "right-brained." Although I know this is not scientifically backed, I think it'd be fun to know whether I'm more of an analytical and logical or creative and intuitive person. I will present the user with about 10 questions that relate to their personal logic and creativity, such as "Do you prefer math and science or literature and art?" or "Do you plan things out or go with the flow?" Each answer will correspond to either left-brain or right-brain score. At the end, the points will be calculated and the user will be presented with a simple explanation of their results.
2a. The first function will present the user with questions, give them answer choices, and record their response.
2b. The next function will consider the response and assign a point value to it based on whether it aligns more with the "left-" or "right-brain." 
2c. Another function in this program will present the user with their final result of whether they are more "left-brained" or "right-brained." A brief explanation will tell the user why they got the results they did, and maybe even give them advice for how to take advantage of their results in real-world situations.

Rough outline:
- Introduction; explain and introduce quiz
- Answer 10-12 questions (questions rated on 1 to 5 scale)
- user receives result and explanation

Functions:
print_instructions(file_name)  displays quiz instructions
ask_question(question_list)  asks questions
Point_question  gives user 1-5 scales answer choices
output_score(left_score, right_score)  displays results with explanation

Example use case: A psychology student wants to run a simple study to collect data for an upcoming presentation. She provides her audience with this quiz and uses the results in a presentation about brain hemispheres. 

Example data:
- instructions.txt  will introduce quiz and provide brief explanation ("Welcome to the Brain Hemisphere Quiz! You will be asked 10 (?) questions. Please answer each question honestly on a scale from 1 (strongly disagree) to 5 (strongly agree). ")
- csv file of questions

Testing:
This program could be used in a variety of different situations. It requires input from the user, which will always be in the form of a number between 1 and 5. I can test this program in a couple different ways. First, I can check the accuracy of the scoring. I can take the quiz and input only low values, which should lean more towards the left-brain result, and vice versa. If I get the appropriate results, I'll know that my code, specifically the function that's in charge of keeping score, works. Next, I can test the code with invalid input from the user, meaning anything other than numbers between 1 and 5. For example, as the user, I could input a letter or phrase. If I get the error statement, then I will know that that portion of the code works the way I want it to. Finally, I can recreate a real-world scenario where this might be used. I could ask a friend to attempt the quiz without any prior knowledge or instructions. By observing them move through the quiz, I'll be able to see if my instructions are clear, if the questions are presented well, and if the results show up in a visually appealing way. I could also ask them for some feedback regarding what I could add to make taking the quiz a better experience for the user. 

Main Structure Code: 

import csv

def load_questions(file_name): #loads questions from csv file and assigns weights to side of brain (1 is left brained, -1 is right btained)
    question_list=[]
    with open(file_name, newline='', encoding= 'utf-8') as file: 
        reader = csv.reader(file)


def ask_question(question):
    #has user answer questions on scale from 1 to 5, (strongly disagree to strongly agree)

def give_quiz(questions):
    #this will ask all the questions and record the user's responses
    #remember to add error messages if user gives response other than number btwn 1 and 5

def calculate_score(questions, responses):
    #calculates overall score

def show_result(score):
    #prints final result with small explanation paragraph, possibly add some sort of graphic here??
    #use if elif else to give options 

def main():
    questions_file = "brain_quiz_questions.csv"
    print ("Welcome to the Brain Hemisphere Quiz!") #add more to this intro
    print ("Answer each of the following questions on a scale from 1, meaning you strongly disagree, to 5, meaning you strongly agree.\n")

    questions = load_questions(questions_file)
    responses = give_quiz(questions)
    score = calculate_score(questions, responses)
    show_result(score)

if __name__ == "__main__":
    main()
ding main_structure.py…]()


Updated Code:

import csv

def load_questions(file_name): #loads questions from csv file and assigns weights to side of brain (1 is left brained, -1 is right btained)
    question_list=[]
    with open(file_name, newline='', encoding= 'utf-8') as file: 
        reader = csv.reader(file)
        for row in reader:
            question = row{0}
            weight = int(row[1])
            question_list.append((question,weight))
        return question_list

def print_instructions(file_name):
    #prints instructions from text file
    with open(file_name, 'r', encoding= 'utf-8') as file:
        instructions = file.read()
        print(instructions)


def ask_question(question):
    #has user answer questions with either 'true' or 'false'; returns as Boolean
    while True:
            response = input(f"{question} (True/False): ").strip().lower() #asked ChatGPT how to accept more diverse answers, such as those with spaces or in non-lowercase letter; told me to add .strip().lower()
            if response == "true":
                    return True
            elif response == "false":
                return False
            else:
            print("This input is invalid. Please type either 'True' or 'False.'")

def give_quiz(questions):
    #this will ask all the questions and record the user's responses
    #remember to add error messages if user gives response other than number btwn 1 and 5
    responses = []
    for question, _ in questions:
         response = ask_question(question)
         responses.append(response)
    return responses

def calculate_score(responses):
    #calculates overall score
    # true means left brain, false means right brain
    score = sum(1 if response else _1 for response in responses) 
    return score

def show_result(score):
    #prints final result with small explanation paragraph, possibly add some sort of graphic here??
    #use if elif else to give options 

def save_result(score): 
# saves score and result as text file
#do i rly want/need this?

def main():
    questions_file = "brain_quiz_questions.csv"
    print ("Welcome to the Brain Hemisphere Quiz!") #add more to this intro
    print ("Answer each of the following questions on a scale from 1, meaning you strongly disagree, to 5, meaning you strongly agree.\n")

    questions = load_questions(questions_file)
    responses = give_quiz(questions)
    score = calculate_score(questions, responses)
    show_result(score)
    save_result(score)

if __name__ == "__main__":
    main()





