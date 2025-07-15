
import streamlit as st

# Page setup
st.set_page_config(page_title="School Help Chatbot")

# Title
st.title("🎓 School Help Chatbot")

# Question input
question = st.text_input("Ask me a question:")

# Q&A dictionary (includes sample + 100 Grade 8 math questions)
answers = {
    "what is photosynthesis": "Photosynthesis is the process by which green plants make their own food using sunlight.",
    "who discovered gravity": "Sir Isaac Newton discovered gravity when he observed a falling apple.",
    "study tips": "Study in short focused sessions (Pomodoro), take breaks, and review regularly.",
    "how to stay focused": "Keep your phone away, study in a quiet space, and set specific goals.",
    "what is 25 percent of 200": "25% of 200 is 50.",
    "what is the square root of 144": "The square root of 144 is 12.",
    "solve for x in 2x + 3 = 11": "x = 4",
    "what is the area of a triangle with base 10 and height 5": "Area = 0.5 × base × height = 0.5 × 10 × 5 = 25",
    "what is the perimeter of a rectangle with length 8 and width 3": "Perimeter = 2(l + w) = 2(8 + 3) = 22",
    "what is 15 squared": "15 squared is 225.",
    "simplify: 3x + 2x": "3x + 2x = 5x",
    "what is the value of pi": "Approximately 3.14",
    "what is 3 to the power of 4": "3⁴ = 81",
    "convert 0.75 to a fraction": "0.75 = 3/4",
    "what is 12 percent of 250": "12% of 250 = 30.",
    "what is 7 squared": "7 squared is 49.",
    "simplify: 4a + 3a - 2a": "4a + 3a - 2a = 5a",
    "solve for x: 3x = 15": "x = 5",
    "find the mean of 5, 10, 15": "Mean = (5+10+15)/3 = 10",
    "what is the median of 4, 6, 7, 8, 10": "The median is 7.",
    "what is the mode of 2, 4, 4, 5, 6": "The mode is 4.",
    "convert 3/4 to decimal": "3/4 = 0.75",
    "convert 0.2 to percentage": "0.2 = 20%",
    "find the volume of a cube with side 4": "Volume = side³ = 64",
    "what is the circumference of a circle with radius 7": "C = 2πr ≈ 2×3.14×7 = 43.96",
    "how many degrees in a triangle": "180 degrees.",
    "how many degrees in a straight angle": "180 degrees.",
    "how many degrees in a right angle": "90 degrees.",
    "solve: 5(x - 2) = 15": "x = 5",
    "factor: x² + 5x + 6": "(x + 2)(x + 3)",
    "expand: (x + 2)(x + 3)": "x² + 5x + 6",
    "simplify: (3x)(2x)": "6x²",
    "what is 10 factorial": "10! = 3628800",
    "what is the lowest common multiple of 4 and 6": "LCM of 4 and 6 is 12",
    "what is the greatest common factor of 18 and 24": "GCF is 6",
    "what is the slope of the line y = 2x + 3": "Slope is 2",
    "what is the y-intercept of y = -4x + 7": "y-intercept is 7",
    "solve: 4x - 1 = 3": "x = 1",
    "simplify: 2(x + 3) - 4": "2x + 6 - 4 = 2x + 2",
    "convert 5/8 to decimal": "5/8 = 0.625",
    "convert 2.5 to a fraction": "2.5 = 5/2",
    "find the area of a circle with radius 3": "Area = πr² ≈ 3.14×3×3 = 28.26",
    "what is 100 divided by 4": "100 ÷ 4 = 25",
    "solve for x: x/5 = 6": "x = 30",
    "what is 6 cubed": "6³ = 216",
    "simplify: 6x - 4x + 2": "2x + 2",
    "what is 20 percent of 90": "20% of 90 = 18",
    "round 7.89 to the nearest whole number": "8",
    "round 4.3 to 1 decimal place": "4.3",
    "convert 1/3 to decimal": "1/3 ≈ 0.333",
    "how many cm in 2 meters": "200 cm",
    "how many mm in 5.5 cm": "55 mm",
    "convert 120 minutes to hours": "2 hours",
    "what is 3/5 as a percentage": "60%",
    "find the area of a square with side 9": "Area = side² = 81",
    "find the perimeter of a square with side 6": "Perimeter = 4 × side = 24",
}

# Display answer
if question:
    answer = answers.get(question.lower(), "❓ Sorry, I don't know that yet. Try asking something else.")
    st.write("📘", answer)
