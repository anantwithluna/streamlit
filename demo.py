import streamlit as st
st.title("Luna Vista")
st.sidebar.image('withluna_ai_logo.jpg')
st.sidebar.header("Link to Demo Document")
st.sidebar.link_button("Read the Demo Doc", "https://www.youtube.com/watch?v=TU1gMloI0kc&pp=ygUMb3BlbiBhaSBzb3Jh")
st.sidebar.link_button("Submit Feedback about the output","https://forms.gle/c2zuB8DTgRcKY2QKA")


text = st.text_area('Enter your text here',height = 300)
if st.button('Generate output'):
    st.write(""""Project XYZ:
  - Risks:
    Description: Key dependency on the ABC project, specifically in terms of data integration. Delays in the ABC project have impacted the timelines of the XYZ project.
    Raised by:  John Smith (Product Marketing Manager)
    Raised on: 16/02/2024
    Mitigation plan: Issue already escalated to project ABC's project manager. Escalate the issue further within the organization and seek assistance from Sarah Johnson
    Assigned to: N/A

  - Decision:

    Decision description: N/A
    Decision Rationale: N/A
    Who took the decision: N/A
    Raised on: N/A

  - Updates:

    Update Description: The XYZ project has achieved significant milestones, including the successful launch of the beta version and positive feedback from early users.
    Team: Product Marketing
    Next week's priorities: Address critical user interface issues reported during the beta phase, conduct user research for future improvements
    When: 16/02/2024

  - Link to important resources:

    Important resources: XYZ project documentation
    Link: [XYZ Project Documentation](https://www.example.com/xyz-project-documentation)"""")
else:
    pass
