import csv

def load_questions(file_name): #loads questions from csv file and assigns weights to side of brain (1 is left brained, -1 is right btained)
    question_list=[]
    with open(file_name, newline='', encoding= 'utf-8') as file: 
        reader = csv.reader(file)
        for row in reader:
            question = row[0]
            weight = int(row[1])
            question_list.append((question,weight))
        return question_list

def ask_question(question):
    #has user answer questions with a number between 1 and 5, and returns numeric value as an integer
    while True:
            response = input(f"{question}\n(1 = Strongly Disagree, 5 = Strongly Agree): ").strip() #asked ChatGPT how to accept more diverse answers, such as those with spaces; told me to add .strip()
            if response in {"1", "2", "3", "4", "5"}:
                return int(response)
            else:
                print("This input is invalid. Please enter a number from 1 to 5.")

def give_quiz(questions):
    #this will ask all the questions and record the user's responses
    #remember to add error messages if user gives response other than number btwn 1 and 5
    responses = []
    for question, _ in questions:
         response = ask_question(question)
         responses.append(response)
    return responses

def calculate_score(questions, responses):
    #calculates overall score based on the relationship to the neutral score of 3 multiplied by brain-side weight (Had ChatGpt help me with this multiplication concept)
    #Positive score means left brained, negative score means right brained
    score = 0
    for (question, weight), response in zip(questions, responses):
         adjusted = (response -3) * weight
         score += adjusted
    return score

def show_result(score):
    print("\n#### QUIZ RESULTS ####\n")
    if score > 0:
         print("You are more left-brained!")
         print("Being more left-brained means you tend to think more logically, analytically, and methodically. You likely prefer structure, enjoy working with facts and numbers, and excel in tasks involving language, reasoning, or problem-solving.")
    elif score <0:
         print("You are more right-brained!")
         print("Being more right-brained means you tend to think more creatively, intuitively, and emotionally. You likely enjoy artistic expression, big-picture thinking, and are drawn to imagination, visuals, and abstract ideas.")
    else:
         print("You are a balance of both left and right brained!")
         print("Being equal-brained means you have a balanced mix of logical and creative thinking styles. You can switch between analytical tasks and imaginative thinking.")


def save_result(score): 
    with open("quiz_result.txt", "w") as file:
         file.write(f"Score: {score}\n")


def main():
    questions_file = "brain_quiz_questions.csv"
    print ("Welcome to the Brain Hemisphere Quiz! If you're interested in finding out whether you're more left-brained or right-brained, this is the place for you! You will be presented with a series of statements.")
    print ("Answer each statement on a scale from 1, meaning you strongly disagree, to 5, meaning you strongly agree.\n")

    questions = load_questions(questions_file)
    responses = give_quiz(questions)
    score = calculate_score(questions, responses)
    show_result(score)
    save_result(score)

if __name__ == "__main__":
    main()
