import os
from src.rai_crew.crew import RAI_Crew

print("Current working directory:", os.getcwd())
# imaginary product description
with open("product_desc.txt", "r", encoding='utf-8') as product_file:
    product_description = product_file.read()


def run():
    inputs = {
        'company': 'Google'
    }

    crew_output = RAI_Crew().crew().kickoff(inputs=inputs)
    # print('Token usage: ', crew_output.token_usage)   # for token usage control
    tasks_out = crew_output.tasks_output
    result_file = open("final_strategy.txt", "a")   # writing results a txt file
    result_file.write(tasks_out[2].raw)   # only write task 3 output
    result_file.close()


if __name__ == '__main__':
    run()
