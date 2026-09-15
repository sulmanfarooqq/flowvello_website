import os

file_path = 'c:/Users/my/Desktop/strategy/9_The_Solo_Tech_Stack/tools_to_run_it_all.txt'

content = '''THE FREE-TIER AGENCY TECH STACK

First rule: You do NOT send proposals in bulk. You send OUTREACH in bulk. Proposals are custom documents sent only to qualified prospects after a discovery call. 

If you are bootstrapping with zero budget, here are the exact free-tier tools to run your entire agency:

1. BULK OUTREACH & LEADS: Apollo.io
- Use the free tier to search B2B contacts, find emails, and automate your cold email sequences.

2. CRM (Tracking Deals): HubSpot CRM
- 100% free forever. Track who opened your email, who is booked for a call, and your pipeline value.

3. PROPOSALS & CONTRACTS: PandaDoc
- Use the Free eSign plan. Send your scope of work as a PDF and get legally binding signatures.

4. PROJECT MANAGEMENT (Dev Team): ClickUp
- Use the free tier. This is where you paste your Developer Handoff SOP. Track every task and deadline here.

5. MEETINGS: Google Meet
- Free video calls to close deals. 

6. PAYMENTS: Stripe
- No monthly fee (they just take a standard processing percentage). Do not start work until the Stripe invoice is paid.

You now have zero financial excuses. Go execute.'''

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content.strip())
    
print("File updated.")
