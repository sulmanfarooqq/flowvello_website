import os

base_dir = 'c:/Users/my/Desktop/strategy'
folders = {
    '1_The_Harsh_Reality': {
        'the_solo_delusion.txt': '''THE SOLO DELUSION
You think you just "get orders" and the team "builds items." 
This is how agencies fail. 
Clients do not buy "items." They buy solutions, and they demand communication, revisions, hand-holding, and strategy.
If you are the only one talking to the client, YOU are the bottleneck.
At /month, you are a freelancer with helpers.
At /month (.2M/yr), you will drown if you are the sole project manager.
Your actual job isn't just sales. Your job is SYSTEMS. You must build a machine where the team can operate without you translating every single client request.''',
    },
    '2_Lead_Generation': {
        'outbound_machine.txt': '''OUTBOUND MACHINE
Do not wait for inbound. No one knows who you are.
Pick ONE niche (e.g., B2B SaaS or Healthcare).
Pick ONE channel (e.g., Cold Email or LinkedIn).
Pick ONE offer (e.g., "We automate your lead routing so you stop losing deals").
Send 100 highly personalized, brutal pain-point messages a day. 
No fluff. No "I hope you are doing well." 
Just: "I noticed [Problem]. We fix this by [Solution]. Worth a 10 min chat?"
Do this every single day. Volume negates luck.''',
        'content_trap.txt': '''THE CONTENT TRAP
Do not waste time posting 5 times a day on Instagram. You sell enterprise AI and automation.
Your buyers are on LinkedIn or in their email inbox.
Write case studies. Document EXACTLY how you saved a client 40 hours a week or /month.
Data wins arguments. Proof gets meetings. Fluff gets ignored.'''
    },
    '3_Sales': {
        'ruthless_qualification.txt': '''RUTHLESS QUALIFICATION
You are solo. Your time is your only asset. Do not waste it on broke clients.
If they don't have budget, disqualify them immediately.
Ask hard questions:
- "What is this problem costing you right now?"
- "Do you have the budget to deploy a + solution this month?"
If they flinch, walk away. You need 5 clients paying , not 50 clients paying . Low-ticket clients complain the most and eat your time.''',
        'closing_the_deal.txt': '''CLOSING THE DEAL
Stop sending "proposals" that list features. 
Send a "Plan of Action" that lists OUTCOMES.
They don't care about the tech stack. They care about the ROI.
Tie your price to the money you will save them or make them.
Require 50% upfront. No exceptions. If they won't pay upfront, they aren't a real client.'''
    },
    '4_Operations': {
        'the_handoff.txt': '''THE HANDOFF (YOUR BIGGEST RISK)
You closed the deal. Now you hand it to your team.
If you just forward an email, the project will fail.
You must have a strict intake form.
You must have standard operating procedures (SOPs).
Your team must know exactly what "done" looks like before they write a single line of code.
If the team builds the wrong thing, it is YOUR fault for poor scoping.''',
        'client_management.txt': '''CLIENT MANAGEMENT
Set a communication policy on Day 1.
No WhatsApp. No random phone calls.
All communication goes through a shared Slack channel or project management tool (Monday/ClickUp).
Update them before they ask for an update. An uninformed client is a panicking client.'''
    },
    '5_The_Million_Dollar_Path': {
        'scaling.txt': '''HOW TO HIT 
To hit /year, you need ~/month.
That is 8 clients paying /mo, or 16 clients paying /mo.
You cannot handle 16 active projects by yourself if you are the only Project Manager and Salesperson.
The moment you hit /mo, you must hire an Account/Project Manager to talk to clients. 
You must extract yourself from fulfillment completely.
If you don't, you will cap out at /mo, burn out, and your agency will collapse.'''
    }
}

os.makedirs(base_dir, exist_ok=True)

for folder, files in folders.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for filename, content in files.items():
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
            
print("Strategy structure created on Desktop.")
