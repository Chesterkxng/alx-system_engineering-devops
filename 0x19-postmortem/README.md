POST MORTEM FOR ALX PROJECT

Postmortem: Web Stack Outage Incident

Issue Summary:

Duration:
Start Time: March 6, 2024, 15:00 PST
End Time: March 6, 2024, 18:30 PST
Impact:
The outage affected the core authentication service used by our web application.
Users experienced an inability to log in, resulting in a 30% decrease in active sessions during the outage.
Root Cause:
The root cause of the outage was identified as a misconfiguration in the load balancer settings, leading to improper routing of authentication requests.
Timeline:

15:00 PST: Issue Detected
15:15 PST: Monitoring alert triggered due to a significant drop in successful authentication attempts.
15:30 PST: Initial investigation focused on backend database health and network latency assumptions.
16:00 PST: Misleading investigation path pursued, suspecting a database connection issue.
16:30 PST: Incident escalated to the infrastructure and operations team.
17:00 PST: Further investigation revealed load balancer misconfiguration as the probable cause.
18:00 PST: Load balancer settings adjusted to properly route authentication requests.
18:30 PST: Services fully restored, authentication functionality resumed.
Root Cause and Resolution:

Root Cause:
The load balancer was misconfigured to route authentication requests to non-functional backend servers, resulting in failed authentication attempts.
Resolution:
Load balancer settings were reconfigured to direct authentication requests to operational backend servers, restoring proper functionality.
Corrective and Preventative Measures:

Improvements/Fixes:
Strengthen load balancer configuration management processes.
Implement automated testing of load balancer routing configurations.
Tasks to Address the Issue:
Conduct a comprehensive review of load balancer configurations to identify and rectify any additional misconfigurations.
Implement additional monitoring and alerting mechanisms to detect load balancer-related issues promptly.
Develop and execute a playbook for responding to similar incidents in the future, including clear escalation paths and troubleshooting procedures.
This incident highlighted the critical importance of robust configuration management practices and proactive monitoring in maintaining the reliability and availability of our web services. Moving forward, we are committed to implementing the necessary measures to prevent similar incidents and minimize the impact on our users.