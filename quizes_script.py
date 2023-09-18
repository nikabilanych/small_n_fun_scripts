#! python3
import random
#script that creates 5 quiz files together with keys
#questions and answers are unique for each test
european_countries = {
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Netherlands": "Amsterdam",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "United Kingdom": "London"
}
if __name__=='__main__':
    for tests in range(5):
        
        quiz_file=open(f"Quiz_n_{tests+1}",mode='w', encoding="UTF-8")
        key_file=open(f"Quiz_{tests+1}_key",mode='w',encoding="UTF-8")
        quiz_file.write('\nName:\nPeriod:\nDate:\n')
        quiz_file.write(f"Quiz number: {tests+1}\n")
        countries=list(european_countries.keys())
        random.shuffle(countries)
        for questions in range(20):
            correct_answer=european_countries[countries[questions]]
            wrong_answers=list(european_countries.values())
            #deleting the correct answer from the list
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers=random.sample(wrong_answers,4)
            ans_options=[correct_answer]+wrong_answers
            random.shuffle(ans_options)
            #writing the questions
            quiz_file.write(f"{questions+1}. What is the capital of {countries[questions]}?\n")
            for options in range(5):
                quiz_file.write(f"  {'ABCDE'[options]:>4}. {ans_options[options]}\n")
            quiz_file.write("\n")
            key_file.write(f"{questions+1}. {'ABCDE'[ans_options.index(correct_answer)]}\n")
        quiz_file.close()
        key_file.close()