import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the presentation
st.title("My Streamlit Presentation")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a section", ["Introduction", "Data Representation", "Visualization Representation", "Conclusion"])

# Introduction section
if option == "Introduction":
    st.header("Introduction to Streamlit")
    st.write("""
        Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
        With Streamlit, you can build and deploy powerful data applications in just a few lines of code.
    """)

    st.subheader("Code Explanation:")
    st.write("""
        In this section, we initialize our Streamlit app with a title and sidebar for navigation.
        The sidebar allows users to select different sections of the presentation.
    """)
    st.code("""
import streamlit as st

# Title of the presentation
st.title("My Streamlit Presentation")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a section", ["Introduction", "Data Representation", "Visualization Representation", "Conclusion"])
    """, language='python')

# Load Iris dataset from a local CSV file
iris_data = pd.read_csv("iris.csv")

# Data section
if option == "Data Representation":
    st.header("Data Section")
    st.write("Here you can present your data.")

    # Explanation of the data section
    st.subheader("Code Explanation:")
    st.write("""
        In this section, we load the Iris dataset from a local CSV file and display it in the Streamlit app.
        The data is stored in a DataFrame and displayed in the app.
    """)
    st.code("""
import pandas as pd

# Load Iris dataset from a local CSV file
iris_data = pd.read_csv("iris.csv")
st.write(iris_data)
    """, language='python')

    # Displaying the data
    st.write(iris_data)

    st.write("""
        This is how a code snippet can be displayed:
    """)

    st.code("""
st.code(\"\"\"
import pandas as pd

# Load Iris dataset from a local CSV file
iris_data = pd.read_csv("iris.csv")
st.write(iris_data)
\"\"\", language='python')
    """, language='python')

# Visualization section
if option == "Visualization Representation":
    st.header("Visualization Section")
    st.write("Here you can present your visualizations.")

    # Explanation of the visualization section
    st.subheader("Code Explanation:")
    st.write("""
        In this section, we create a bar plot to visualize the average sepal length for each Species in the Iris dataset.
        We use Streamlit to display the plot in the app.
    """)
    st.code("""
import matplotlib.pyplot as plt

# Calculate the average sepal length for each Species
avg_SepalLengthCm = iris_data.groupby('Species')['SepalLengthCm'].mean()

# Create a bar plot
fig, ax = plt.subplots()
avg_SepalLengthCm.plot(kind='bar', ax=ax)
ax.set_title('Average Sepal Length by Species')
ax.set_xlabel('Species')
ax.set_ylabel('Average Sepal Length')
st.pyplot(fig)
    """, language='python')

    # Sample visualization
    avg_SepalLengthCm = iris_data.groupby('Species')['SepalLengthCm'].mean()
    fig, ax = plt.subplots()
    avg_SepalLengthCm.plot(kind='bar', ax=ax)
    ax.set_title('Average Sepal Length by Species')
    ax.set_xlabel('Species')
    ax.set_ylabel('Average Sepal Length')
    st.pyplot(fig)

# Conclusion section
if option == "Conclusion":
    st.header("Conclusion: Advantages of Streamlit")
    st.write("""
        Streamlit offers several advantages for building data-driven web applications:
        
        - **Simplicity:** Streamlit's API is straightforward and easy to learn.
        - **Speed:** Quickly build and deploy apps without extensive web development knowledge.
        - **Interactivity:** Add interactive widgets like sliders, buttons, and text inputs with minimal code.
        - **Integration:** Seamlessly integrates with popular Python libraries like Pandas, NumPy, and Matplotlib.
        - **Live Updates:** Streamlit apps update in real-time as you modify your code.
    """)
