import os

base_dir = 'c:/Users/my/Desktop/strategy'
folders = {
    '7_The_God_Schedule': {
        'daily_routine.txt': '''THE 8-FIGURE SOLO SCHEDULE
Stop playing business. Stop spending 3 hours tweaking your website button colors.
Here is your exact daily schedule to hit $1M:

08:00 - 09:00: Deep Work (Review dev team progress, QA the items they built)
09:00 - 11:00: Outbound Sales (Send 100 Cold Emails/LinkedIn DMs. No exceptions.)
11:00 - 12:00: Content Creation (Write 1 case study or LinkedIn post. Schedule it.)
12:00 - 13:00: Break / Walk
13:00 - 16:00: Sales Calls & Client Meetings (Pitching, closing, onboarding)
16:00 - 17:00: The Handoff (Write exact, brutal SOPs and scope documents for your dev team)
17:00 - 17:30: Inbox Zero (Clear all emails, Slack messages. Do not leave clients hanging)

If you aren't doing outbound for 2 hours a day, you don't have a business. You have a hobby.'''
    },
    '8_Marketing_and_Content': {
        'social_media_blueprint.txt': '''SOCIAL MEDIA FOR AGENCIES
Nobody cares about your generic "Top 5 Benefits of AI" Canva posts. That is garbage.
You are selling high-ticket B2B systems. 
Your content strategy is 3 things:

1. THE CASE STUDY: "How we helped [Niche Client] save 40 hours a week using [Specific Tech]." 
2. THE TEARDOWN: "Most [Niche] businesses lose $10k/mo on lead routing. Here is the architecture of how we fix it."
3. THE BELIEF SHIFT: "Why relying on Zapier is killing your enterprise scale (and what to use instead)."

Post these 3 times a week on LinkedIn and Twitter. 
Format: Text + 1 Image of a dashboard, code architecture, or real metric.
No dancing on TikTok. No motivational quotes. Just brutal, undeniable competence.'''
    },
    '9_The_Solo_Tech_Stack': {
        'tools_to_run_it_all.txt': '''THE AGENCY TECH STACK
You want to run it all yourself? You need extreme automation.
- CRM & Sales: HubSpot or GoHighLevel (Track every lead, automate follow-ups)
- Cold Email: Instantly.ai (Send 1,000 cold emails a day on autopilot)
- Project Management: Monday.com or ClickUp (This is where your dev team lives. If it's not in ClickUp, it doesn't exist.)
- Client Communication: Slack (Use Connect channels. Set 24hr response boundaries)
- Proposals & Contracts: PandaDoc or DocuSign
- Payments: Stripe (Require 50% upfront. Automated recurring billing)

Do not buy 50 SaaS tools. Master these 6.'''
    },
    '10_The_Execution_Trap': {
        'read_this_last.txt': '''THE EXECUTION TRAP
You asked me to give you a folder that makes you the "God of the agency."
Here is the hardest truth I will ever give you:
Reading this folder does absolutely nothing.
Watching YouTube videos about SMMA does nothing.
Telling an AI to generate strategies does nothing.

You only become a "God" by getting punched in the mouth by a real client.
You become a God when a client demands a refund because your dev team built the wrong thing, and you have to fix the SOP.
You become a God when you send 1,000 cold emails and get 0 replies, and you have to rewrite your entire offer.

The folders are complete. You have the blueprint. 
Now close the folders, close this chat, and go sell your first $5,000 system.'''
    }
}

for folder, files in folders.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for filename, content in files.items():
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
            
print("Final god-tier folders created.")
