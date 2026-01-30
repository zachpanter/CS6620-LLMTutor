# How well does the LLM replace the Expert Model portion of a traditional intelligent tutor? 
It seems to have a good understanding of stoic philosophy and those philosophers who promoted it. 
I did notice that deepseek considered one of my answers as INCORRECT not because I was inherently wrong, 
but because I wasn't verbose enough. 

# Does it get any subject-matter facts wrong?
All of the facts presented seemed correct, 
at least based on my reading of "Meditations" by Marcus Aurelius and "The Daily Stoic" by Ryan Holiday.

# Can you improve this by tweaking the prompting? Report on your experiments.
I altered the prompt after getting my first "false negative" in my [deepseek findings](LLM_Tutor_Findings_deepseek-r1-8b.md#false-negative)

# How well does the LLM replace the Pedagogical Model portion of a traditional intelligent tutoring system? 
I think in this case, my LLM wrapper partially fails to fulfill the "Pedagogical Model" with regards to teaching stoicism. 
Scaffoleded feedback and leading questions are a significant part of the Socratic teaching method, 
whereas my LLM Tutor is framed as a rigid "question --> answer --> new question" process.
Instead, I think there'd be additional value in a method where the inner-loop of a "stoic tenet" outer-loop would be filled with iterative, probing questions.

# Does it use good instructional practices? 
Somewhat. LLM's, especially "mixture-of-experts" models, can be too broad unless carefully prompted. 
Although my LLM Tutor didn't stray from the topics presented (good domain model), it didn't incorporate the Learning Model or Pedagogical models.
I assume it could be manipulated by target responses by the student, 
whereas a true teacher of stoicism would be better adept at gauging the student's understanding, and forming examples targeted for better comprehension.

# What does it do well or not well? 
It knows the authors of the famous works and can cite quotes really well.
My local models were slow, but that encouraged patience and contemplation.
With such a nebulous topic like philosophy, I felt it was accurate, but it's "voice" / prose felt flat and uninspiring.

# Can you improve its use of teaching techniques by tweaking your prompt? Report on your experiments. 
I _did_ improve the teaching technique by adding a third state: "Guidance". By adjusting the "success" conditional statement in the prompt, 
it allowed for a more Socratic, dynamic dialog than the initial, Q/A approach.

# Relate this back to the education research we have learned in class.
VanLehn's outer-loop, inner-loop is represented by my
```commandline
for q in questions:
    ...
    while not is_correct:
        ...
```

The (relatively) immediate feedback is helpful in preventing students from misconstruing a tenet of stoicism.

My sub-prompt _"If the student is wrong, explain the Stoic logic and ask them to try again. "_ 
could be improved to provide hints in a more gradual, scaffolded manner.
