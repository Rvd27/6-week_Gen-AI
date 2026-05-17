import streamlit as st

# Title
st.title("Python Quiz App")

# Questions and Answers
questions = {
    "1. What is the capital of India?":
        ("Delhi", ["Mumbai", "Delhi", "Chennai", "Kolkata"]),

    "2. Which language is used for AI?":
        ("Python", ["Java", "Python", "C", "PHP"]),

    "3. What is 5 + 5?":
        ("10", ["5", "10", "15", "20"]),

    "4. Which company developed Python?":
        ("Python Software Foundation",
         ["Google", "Microsoft",
          "Python Software Foundation", "Apple"]),

    "5. Which keyword is used for condition checking?":
        ("if", ["for", "while", "if", "break"]),

    "6. What is the extension of Python file?":
        (".py", [".java", ".py", ".html", ".cpp"]),

    "7. Which function is used to print output?":
        ("print()", ["input()", "display()", "print()", "echo()"]),

    "8. Which operator is used for addition?":
        ("+", ["-", "*", "/", "+"]),

    "9. Streamlit is used for?":
        ("Web Apps", ["Games", "Mobile Apps",
                      "Web Apps", "Operating Systems"]),

    "10. Which loop repeats code?":
        ("for", ["if", "for", "break", "pass"])
}

# Store answers
user_answers = {}

# Display questions
for question, (correct_answer, options) in questions.items():

    user_answers[question] = st.radio(
        question,
        options,
        key=question
    )

# Submit button
if st.button("Submit Quiz"):

    score = 0

    # Check answers
    for question, (correct_answer, options) in questions.items():

        if user_answers[question] == correct_answer:
            score += 1

    # Display score
    st.success(f"Your Final Score is: {score}/10")

    # Result message
    if score >= 8:
        st.balloons()
        st.success("Excellent Performance!")

    elif score >= 5:
        st.info("Good Job!")

    else:
        st.warning("Keep Practicing!")