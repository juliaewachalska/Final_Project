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
