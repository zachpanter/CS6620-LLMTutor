import ollama
import time

questions = [
    "What is the 'Dichotomy of Control'?",
    "How did Marcus Aurelius view the concept of the 'Obstacle is the Way' in his Meditations?",
    "Explain the difference between 'Preferred Indifferents' and 'Dispreferred Indifferents.'",
    "How does a Stoic distinguish between their own character and external reputation?",
    "If someone insults you, what is the Stoic response according to Epictetus?"
]

def ask_marcus(question):
    is_correct = False
    print(f"\n ### NEW QUESTION\n{question}")

    while not is_correct:
        student_response = input("\n $: ")
        start_time = time.time()

        response = ollama.chat(
            model="deepseek-r1:8b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Stoic philosophy tutor specializing in the Socratic method. "
                        "Evaluate the student's understanding of Stoic principles based on their response. "
                        "If the student is wrong, explain the Stoic logic and ask them to try again. "
                        "Start your response with 'CORRECT' if the student demonstrates clear understanding. "
                        "Start your response with  'GUIDANCE' is the student asks for help or specifically notes they are unfamiliar with a topic, notes they are confused or says they don't know. "
                        "If the response is neither 'CORRECT' nor 'GUIDANCE', start with 'INCORRECT'."
                    )
                },
                {
                    "role": "assistant",
                    "content": question
                },
                {
                    "role": "user",
                    "content": student_response
                }
            ]
        )

        end_time = time.time()

        feedback = response['message']['content']
        print(f"\nSage's Guidance:\n{feedback}")

        duration = end_time - start_time
        print(f"\n(Response took: {duration:.2f} seconds)")

        # Do we move on?
        if feedback.strip().upper().startswith("CORRECT"):
            is_correct = True
            print("\nExcelsior! Let's continue.")
        else:
            print("\nTry again.")


for q in questions:
    ask_marcus(q)