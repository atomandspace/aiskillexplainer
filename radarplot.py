import plotly.graph_objects as go

# skill categories for rating
categories = [
    "Data Pipelines", "Databases", "Data Tools", "Storytelling", 
    "Data Visualization", "Business Insights", "Metrics & Reporting", 
    "Experimentation", "Inference", "Stats & ML Modeling", 
    "Model Deployment", "ML Ops"
]

# Value of each roles as per Hibernian recruiter.
# src: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hibernian-recruitment.com%2Fen%2Fwhats-a-data-scientist-explaining-roles-in-big-data%2F&psig=AOvVaw1HM2k_oXk417A8Ex_do_-K&ust=1731244736621000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCICt-q2rz4kDFQAAAAAdAAAAABAE

data_roles = {
    "Data Engineers": [8, 9, 9, 3, 4, 3, 5, 4, 4, 3, 7, 8],
    "Data Analysts": [3, 4, 5, 9, 9, 8, 8, 6, 4, 3, 2, 1],
    "Data Scientists": [4, 4, 5, 6, 7, 8, 7, 9, 8, 9, 6, 4],
    "ML Engineers": [6, 5, 5, 4, 4, 4, 4, 6, 8, 9, 9, 8]
}

# my skills
my_skills = {
    "Custom Skills": [5, 6, 5, 7, 6, 5, 7, 6, 5, 6, 7, 6]  # Example values
}

# plot all the roles
fig = go.Figure()

for role, values in data_roles.items():
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=role
    ))

# plot my role
for skill_name, values in custom_skills.items():
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=skill_name,
        line=dict(color='black', dash='dash')  # Custom styling for custom skills
    ))

# aesthetics
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )
    ),
    title="",
    template="plotly_dark"
)

# export plot
fig.show()
fig.write_image("my_skills_rating.png")
