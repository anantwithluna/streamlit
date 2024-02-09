import streamlit as st
st.image("withluna_ai_logo.jpg")
st.header("Luna's NER demo")

text = st.text_input('Put your texts here')
st.button("Run NER", type="primary")
if st.button('Run NER'):
    st.write("""1. Project names: AI/ML deployment
2. Risks: potential risk that can slow down the launch date, scalability issue in db transfer, latency of API calls causing bottleneck
3. Who raised the risk: Anant
4. Which team is assigned to solve the risk: not mentioned
5. Mitigation plan: not mentioned
6. Key Decisions: meeting at 1:00pm to decide about what can be done with minimum development time
7. Rationale: not mentioned
8. Who raised the decision: Anant
9. Relevant Updates: not mentioned
10. Achievements: tech team achieving their quarterly targets
11. Priorities: not mentioned
12. Important dates and timeframes: not mentioned
13. Links to important resources: https://docs.google.com/document/d/1v4Bxwe_gdkmwPxZ3jaBsp4IpjsC703CFaMODl017stE/edit""")
else:
    pass
