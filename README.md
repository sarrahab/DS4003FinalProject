# HR Analytics Dashboard - Project Overview

My Render URL: https://ds4003finalproject-1.onrender.com/

Introduction:

The HR Analytics Dashboard is a dynamic visualization tool designed to enable deep insights into various aspects of employee engagement, performance, and satisfaction within an organization. This project was created as a part of my ongoing learning and development in data science and aims to highlight my skills in data manipulation, visualization, and interactive dashboard design using Python and Plotly Dash.

Dashboard Description:

The dashboard presents multiple interactive elements, such as dropdown menus, sliders, and radio buttons, allowing users to filter and segment the data according to departments, positions, performance scores, employment status, and other relevant metrics. It features various types of visualizations including scatter plots, bar charts, pie charts, and line graphs to represent different dimensions of the HR data, such as salary ranges, employee satisfaction, absences, and gender distribution across departments.

Building Process and Learning Experiences:

Data Preparation

Step 1: Data Cleaning and Preprocessing

I started by cleaning the data, handling missing values, and correcting anomalies which set a strong foundation for reliable analysis.
During this phase, I learned to use Pandas extensively for data manipulation, which included filtering, sorting, and summarizing data effectively.

Dashboard Design and Development

Step 2: Layout Design

I planned the layout of the dashboard, deciding on the placement of various filters and graphs to ensure a logical flow and ease of use.
Learning to balance aesthetic appeal with functionality was crucial, as it impacts user experience significantly.

Step 3: Implementation of Interactive Elements

I implemented various interactive components like dropdowns for department and position filters, sliders for salary and age, and radio buttons for performance scores.
A challenge was ensuring these elements interacted correctly with the graphs, which was addressed by refining the callback functions in Dash.

Step 4: Graph Creation

Scatter Plot: Showed the relationship between salary and employee engagement. Initially, this graph was squished due to layout constraints, which I adjusted by modifying CSS properties.
Bar Chart: Displayed average employee satisfaction by department. Aligning this next to other visualizations without overcrowding was a challenge, solved by adjusting the flex properties of the containers.
Pie Chart: Represented gender distribution. It was initially misaligned with other charts, which I corrected by tweaking the grid layout.
Line Graph: Added later to show absences vs. salary by department. Making this graph informative involved aggregating data more effectively, by rounding off salaries and grouping by department, which I implemented using Pandas' grouping and rounding capabilities.

Step 5: Integration and Responsiveness

Ensuring the dashboard responded efficiently to user inputs across all filters involved extensive testing and adjustments to the data querying logic in the callbacks.

Debugging and Enhancements

Step 6: Debugging and Testing

One major issue was the dashboard layout breaking when certain filters were applied. This was due to improper handling of empty data slices returned from filtered datasets. I learned to implement checks and balances to handle such scenarios gracefully.
Another issue was related to performance, where initial loads were slow. I optimized the data processing steps and learned about efficient memory usage.

Step 7: Final Touches and Styling

I added final touches by styling the dashboard using custom CSS for colors, font sizes, and padding to make the dashboard visually appealing.
The choice of colors was adjusted several times to enhance readability and aesthetic appeal, sticking mainly to shades of purple and gray for a professional look.

Data Science Concepts Applied

Data Wrangling: The raw dataset underwent a series of processing steps including cleaning, normalization, and transformation to prepare it for analysis and visualization.
Exploratory Data Analysis (EDA): Before developing the dashboard, extensive EDA was conducted to understand the distributions and relationships within the data, which guided the design and functionality of the interactive components.
Statistical Analysis: Basic statistical methods were applied to summarize the data and calculate key metrics such as average salaries and satisfaction levels.
Interactive Visualization: Using Plotly Dash, a framework for building interactive web-based dashboards, I implemented multiple interactive elements that enable real-time data exploration through user inputs.
Learning Experiences
UI/UX Design: Developing a user-friendly interface required thoughtful layout planning and element arrangement to ensure the dashboard is intuitive and accessible.
Debugging and Problem Solving: Throughout the development process, various challenges such as data inconsistencies and coding errors needed to be resolved, enhancing my problem-solving skills.
Performance Optimization: Ensuring the dashboard performs efficiently with large datasets involved optimizing data processing and rendering techniques.
Strengths and Highlights
Adaptability: The dashboard adapts to various data dimensions and user requirements, showcasing flexibility in data representation.
Detail-Oriented: Attention to detail in both data analysis and dashboard aesthetics helped in creating a polished and professional final product.
Technical Proficiency: Utilizing advanced features of Python libraries like Pandas and Plotly Dash to handle data and create dynamic visualizations reflects a high level of technical skill.

Conclusion

The project not only bolstered my technical skills in using Python, Pandas, and Plotly Dash but also improved my understanding of user interface design and the importance of a smooth user experience. Handling real-world data and transforming it into an interactive dashboard provided a holistic learning experience from data preprocessing to user-focused design and optimization.
