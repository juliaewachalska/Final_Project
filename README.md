# Final_Project
BCOG200 final project
## Overview
For my final project, I have decided to create a brain hemisphere quiz which, based on user input, determines whether the user is more "left-brained" or "right-brained."

## How it Works
The quiz begins with a simple introudction and instructions. The quiz then asks a series of questions from the CSV file. The user responds with a number between 1 and 5, depending on how much they agree with the presented statement. Each question has a corresponding "brain side" weight, which is then used to calculate the final score. A final positive score presents the user with results saying that they are more "left-brained," and vice versa. There is also an option for someone who might be a balance of both.

## Requirements 
Be sure to also dowload the brain_quiz_questions.csv file!

## Testing
I opted to create a narrative of how someone might be able to test the code and ensure that it runs properly. There are three ways to test different portions of the code.

### Testing Questions
We can ensure that all questions from the CSV file display correctly. We expect them to appear in the terminal one by one, with a reminder of the answer scale appearing with each question. If this occurs, we know that the CSV file is formatted appropriately, and that the load_questions() and ask_questions() functions work correctly.

### Testing Result/Output
We can also test to make sure that the results at the end display and work properly. After answering all questions, the code calculates a score adn returns a results to the user. We can confirm that the calculate_score() and show_result() functions work as they should.

### Testing Input Validation
We can test the user input to ensure that invalid responses aren't accepted. This can be done by inputting anything other than a number between 1 and 5. For example, "6" or "six" should re-prompt the user. This confirms that the ask_question() function works correctly.

