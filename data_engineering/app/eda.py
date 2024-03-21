import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#function to call app.py
def run():
    st.title('Exploration Data Analysis (EDA)')
    st.write('Further data analysis to gain in-depth insight into the dataset used.')   

    # Load Picture
    st.image("EdaImage.jpg")
    st.markdown('---')

    # Load csv Data 
    data = pd.read_csv('/app/bank-additional-full_clean.csv')

    # Displays the data
    st.header('Displays the data')
    st.dataframe(data)
    st.markdown ('---')
    
    # EDA
    st.header('1. Contact Month')
    image = Image.open('figure_1_last_contact_month.png')
    st.image(image, caption='Figure 1: Contact Month')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            From this visualization, Both graphs above indicate that the majority of respondents have been contacted by the marketing team most frequently in the month of May.
            There is a very prominent trend among those who decide not to take the deposit service. In this group, almost 3 out of 4 people who were contacted and then chose to decline the service were contacted in May.
            ''')
    st.markdown('---')
    
    st.header('2. Subscription Status')
    image = Image.open('figure_2_subscription_status.png')
    st.image(image, caption='Figure 2:Subscription Status')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - Out of approximately 30,000 clean data points to be processed for modeling, it is observed that 87%, of contacted customers prefer not to subscribe to the term deposit service offered by the bank's telemarketers.
            - Only about 13%, or roughly over 3,000 customers, contacted are willing to opt for the term deposit subscription service offered by the bank through telemarketing.
            - These findings highlight a data tendency towards imbalance: the classification of records/customers is uneven, with a ratio of 87.34:12.66 between class 0 and class 1, respectively, in percentage terms.
            - Considering these variables will be the target of modeling, our team will focus on data balancing to provide a more representative modeling approach capable of capturing patterns to predict customers' final decisions after being contacted by telemarketing regarding the offer of the bank's term deposit subscription service.
            ''')
    st.markdown('---')

    st.header('3. Age')
    image = Image.open('figure_3_age.png')
    st.image(image, caption='Figure 3:Age')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - The age distribution displays a positive skew, noticeable as the chart leans towards the left side, with twelve percent of records identified as outliers.
            - Those opting for banking deposit services tend to be older compared to those who decline the offer.
            - This finding is supported by the two-paired independent test, which concludes a significant difference in age characteristics between customers opting for term deposit subscription services and those rejecting the bank's promotional offers.
            ''')
    st.markdown('---')

    st.header('4. Occupation')
    image = Image.open('figure_4_occupation.png')
    st.image(image, caption='Figure 4: Occupation')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - The most commonly cited occupations among respondents are in administration and private employment. This trend persists among respondents who ultimately opt to deposit and those who do not. Both groups also share technicians as the third most frequently mentioned occupation.
            - Out of all customers contacted by telemarketing, only about 2 percent, or approximately 610 individuals, are students.
            - The p-value indicating the relationship between occupation and subscription status is known, marked by a p-value score smaller than the critical value set (p-value < 0.05).
            - Therefore, the occupation variable has a significant association with the final decision status of customers regarding subscribing to term deposit services.
            ''')
    st.markdown('---')

    st.header('5. Last Contact Duration')
    image = Image.open('figure_5_last_contact_duration.png')
    st.image(image, caption='Figure 5: Last Contact Duration')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - The distribution of contact duration shows a positive skew, with over 15%, of all records identified as outliers.
            - Typically, customers who ultimately choose not to subscribe to the bank's term deposit service tend to have shorter contact durations compared to those who do subscribe.
            - This tendency suggests that individuals already disinterested in banking offers are less likely to engage further in telemarketer conversations.
            - Conversely, customers inclined to subscribe exhibit longer contact durations, indicating more substantial, prolonged, and active engagement with telemarketers.
            - Ultimately, respondents with shorter durations tend to decline banking offers, whereas those engaged in longer durations tend to become subscribers.
            - Two-pair independent testing results indicate significant differences in call duration between the subscribing and non-subscribing groups.
            ''')
    st.markdown('---')

    st.header('6. Marriage Status')
    image = Image.open('figure_6_marital_status.png')
    st.image(image, caption='Figure 6: Marriage Status')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - It is known that the majority of respondents are married, comprising 57 percent of the total.
            - About one-third of all respondents contacted by the bank's marketing team are still single.
            - The remainder, approximately 12 percent, are respondents currently going through divorce. It's noteworthy that this status accounts for both legally separated (divorce while both parties are alive) and widowed (the death of their partner).
            - Based on the identification of marital status characteristics among those who opt to deposit and those who don't, there is a relationship between marital status and the decision to subscribe to the term deposit service.
            ''')
    st.markdown('---')

    st.header('7. Number Of Contact')
    image = Image.open('figure_7_campaign_contact.png')
    st.image(image, caption='Figure 7: Number Of Contact')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - The majority of respondents had fewer than 10 interactions with banking campaigns and telemarketers.
            - Those opting to subscribe to banking offers tended to have fewer campaign interactions, possibly due to their inherent interest and quicker decision-making.
            - Conversely, most respondents disinterested in banking offers had more interaction contacts, possibly due to delayed decisions and extended follow-ups.
            - The significant difference in contact numbers between subscribers and non-subscribers may indicate delayed decisions and over-contact by telemarketers.
            - The two-paired independent test results also indicate significant differences between subscribers and non-subscribers.
            ''')
    st.markdown('---')

    st.header('8. Respondents Education Background')
    image = Image.open('figure_8_education_level.png')
    st.image(image, caption='Figure 8: Respondents Education Background')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - There are only 8 individuals, or 0.02 percent of the data, categorized as 'Illiterate'.
            - Those who eventually deposit assets into the bank after the campaign tend to belong to the university-educated demographic category.
            - Conversely, individuals who opt not to deposit come from a more diverse demographic category, with a higher proportion having basic and secondary education backgrounds.
            - This suggests that education level significantly influences their decision to deposit or decline this opportunity.
            - Based on statistical analysis, it's noted that the education status variable has a fairly significant association with the final decision of contacted customers in choosing the term deposit service subscription offered by the bank.
            ''')
    st.markdown('---')

    st.header('9. Personal Loan')
    image = Image.open('figure_9_personal_loan.png')
    st.image(image, caption='Figure 9: Personal Loan')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - Among all bank customers who were respondents to the term deposit service promotion, it's observed that 16 percent of them currently have personal loans in their respective accounts.
            - Approximately four out of five respondents do not have any loans in their accounts.
            - Demographically, the majority of respondents across both groups—those who subscribe to the term deposit service and those who reject it—do not have existing loans in their accounts.
            - This assumption is further supported by a chi-square test, which concludes that the variables of personal loan status and subscription status are not significantly related, as evidenced by a p-value score greater than the critical p-value: 0.3920663794938557 > 0.05.
            ''')
    st.markdown('---')

    st.header('10. Housing Loan')
    image = Image.open('figure_10_housing_loan.png')
    st.image(image, caption='Figure 10: Housing Loan')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - A significant portion of respondents have housing loans, with data indicating that more than half of those who either opt for or decline the bank's term deposit services are involved in mortgage programs.
            - Through statistical testing using the chi-square metric, it's found that the housing loan variable has a relatively weak correlation with the final subscription status variable of customers contacted by the bank's telemarketing team.
            - These findings suggest that this variable may not warrant further attention, as housing loan status does not exhibit significant correlation with the target outcome. Additionally, real-life circumstances influencing housing loan possession may not necessarily align with personal interest in accepting or rejecting term deposit subscription offers.  
            ''')
    st.markdown('---')

    st.header('11. Contact Method')
    image = Image.open('figure_11_contact_method.png')
    st.image(image, caption='Figure 11: Contact Method')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - The predominant communication channel for both subscribers and non-subscribers of the bank's deposit service is mobile phones.
            - An intriguing trend emerges where non-subscribers show a higher proportion of responses via landline phones, suggesting a potential reluctance to engage further through this medium.
            - This is further evidenced by correlation analysis using the chi-square metric; it reveals a significant relationship between the contact medium utilized by telemarketing and the likelihood of customers opting for the term deposit promotion. The resulting p-value score of 5.354605622000064e-139 is below the established threshold of 0.05.
            ''')
    st.markdown('---')

if __name__== '__main__':
    run()