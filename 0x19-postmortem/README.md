Incident Report: Mwonyaa Stream App Outage on 30th April, 2024
Summary:
On 30th April, 2024, the Mwonyaa Stream App experienced a significant outage between 9:45 am and 10:15 pm EAT, affecting users' ability to access the service. The root cause of this outage was identified as an invalid configuration change that exposed a bug in a widely used internal library.
Incident Details:
Date: 30th April, 2024
Duration: 9:45 am to 10:15 pm EAT (approximately 12 hours and 30 minutes)
Impact: The outage resulted in a complete loss of service for all users, preventing them from accessing the Mwonyaa Stream App.
Root Cause Analysis:
The investigation revealed that an invalid configuration change was made to the system, which exposed a bug in a widely used internal library. This bug caused a cascading failure of dependent services, leading to the outage.
Resolution:
The issue was resolved by rolling back the invalid configuration change and applying a patch to the affected internal library. Additionally, the team implemented a temporary workaround to ensure service stability while a permanent fix was developed.
Corrective Actions:
Improved Configuration Management: Implement a more robust configuration management process to prevent similar invalid changes in the future.
Enhanced Testing: Increase the scope and frequency of testing to identify potential issues before they affect production.
Library Updates: Prioritize updates to the internal library to ensure any known bugs are addressed.
Incident Response Plan: Review and refine the incident response plan to reduce the time to detect and resolve similar incidents.
Lessons Learned:
This incident highlights the importance of rigorous testing and validation of configuration changes before deployment to production. It also underscores the need for proactive maintenance and updates of internal libraries to prevent bugs from causing outages. Recommendations:
The incident response team recommends that the development team prioritize the implementation of the corrective actions outlined above to prevent similar incidents in the future.
Incident Response Team:
·        Chris Emmanuel Ocero [Team Lead]
·        Emmanuel Oka [IT Head]
·        Johnstone Okello [Senior Software Engineer]
·        Grace Apio [Developer]
·        Nakimera Christine [Developer]
Date of Incident Report: 15th May, 2024
