import os

base_dir = 'c:/Users/my/Desktop/strategy/11_The_Final_Docs'
os.makedirs(base_dir, exist_ok=True)

docs = {
    '1_cold_email_script.txt': '''THE ONLY COLD EMAIL SCRIPT YOU NEED

Stop sending 5-paragraph emails talking about yourself. Nobody cares about Flow Vello. 
They only care about their own problems.

[SUBJECT LINE]: Quick question about your lead routing

Hi [First Name],

I noticed [Company Name] is currently driving traffic to a generic contact form. Most of our [Niche] clients found they were losing 30% of their inbound leads because they couldn't respond within 5 minutes.

We build automated AI routing systems that instantly qualify inbound leads and push them directly to your CRM. 

Are you currently solving this, or would you be open to seeing a 2-minute video on how we did this for another agency?

Best,
Sulman''',

    '2_client_onboarding_form.txt': '''THE CLIENT INTAKE FORM (SOP)

You closed the deal. DO NOT let the developers start coding yet. 
Send this to the client via Typeform or Google Forms. If they don't fill it out, the project does not start.

1. What is the single primary goal of this project? (e.g., Increase sales by 10%, cut manual data entry)
2. Who is the dedicated point of contact for approvals?
3. List every single software/CRM you currently use that needs to be integrated.
4. Do you have API keys and admin access ready for those softwares?
5. What does a "failed project" look like to you? (So we know exactly what to avoid).

If you don't get these answers in writing, the client will change their mind halfway through and blame you.''',

    '3_developer_handoff_sop.txt': '''THE DEVELOPER HANDOFF (SOP)

Do not forward client emails to your developers. 
You are the Solutions Architect. You must translate client wishes into technical scope.

Create a ClickUp/Monday task with this exact structure:

**1. Project Summary:** (What are we building and why?)
**2. Tech Stack:** (React, Node, GoHighLevel API, etc.)
**3. The Deliverables (The Checklist):**
   - [ ] Implement Zapier webhook from Typeform to CRM.
   - [ ] Build custom dashboard UI matching Figma file attached.
   - [ ] Write API script to sync records every 15 minutes.
**4. Definition of Done:** (How do we test it to know it works?)
**5. Deadline:** (Date and Time).

If you give your developers this document, they will build exactly what you want. If you just say "build a dashboard," they will guess, and you will lose the client.'''
}

for filename, content in docs.items():
    file_path = os.path.join(base_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
            
print("Final docs generated.")
