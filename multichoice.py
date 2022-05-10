from question import Question
question_prompt=["what color is the outer surfaace of a  watermelon?\na)red\nb)green\nc)pink\n\n","what is acceleration due to gravity?\na)14m/s\nb)9.8m/s\nc)30m/s\n\n","what is the square root of 225?\na)30\nb)15\nc)79\n\n"]
question=[Question(question_prompt[0],"b"),Question(question_prompt[1],"b"),Question(question_prompt[2],"b")]
def solve(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("you got "+str(score)+"/"+str(len(questions))+" correctly")
solve(question)