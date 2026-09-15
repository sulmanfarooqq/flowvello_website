import os

file_path = 'c:/Users/my/Desktop/strategy/12_Master_Agency_Identity.txt'

content = '''FLOW VELLO: MASTER IDENTITY & DELIVERY DOCUMENT

If a client asks you what you do, or if your developers ask you what stack to use, this is the only document you need.

AGENCY NAME: Flow Vello
CORE IDENTITY: We don't sell websites. We build AI systems and workflow automations that eliminate manual labor, cut costs, and scale revenue for B2B companies.

--- THE 4 CORE SERVICES & THE EXACT TOOLS YOU USE TO DELIVER THEM ---

1. WORKFLOW AUTOMATION
What you sell: Connecting disjointed systems so data flows automatically without human data entry.
Tools your team uses to build it:
- Make.com (Cheaper and better than Zapier for complex logic)
- n8n (For enterprise, self-hosted workflows)
- Zapier (For simple, quick client requests)

2. AI AGENTS & CHATBOTS
What you sell: AI customer support and lead qualification agents that talk to customers 24/7.
Tools your team uses to build it:
- Voiceflow or Botpress (For building the chatbot logic and UI)
- OpenAI / Gemini API (The brain powering the responses)
- Twilio (If you are building AI SMS or Voice agents)

3. CRM & DIGITAL OPERATIONS
What you sell: Taking a company off messy Google Sheets and putting them on a centralized operating system.
Tools your team uses to build it:
- GoHighLevel (For local businesses, agencies, and real estate. White-label it as your own software.)
- HubSpot (For B2B SaaS and enterprise clients)
- Monday.com or Airtable (For internal project management dashboards)

4. CUSTOM SOFTWARE (WEB/MOBILE APPS)
What you sell: Bespoke software solutions when out-of-the-box SaaS isn't enough.
Tools your team uses to build it:
- Frontend: React or Next.js (Tailwind for styling)
- Backend: Node.js or Python (FastAPI)
- Database: Supabase or Firebase
- Hosting: Vercel or AWS

--- THE RULE ---
Do not let your developers pick random tools. If a client buys an AI Agent, you tell the developer: "Build this in Voiceflow using the OpenAI API." You are the architect. They are the builders.'''

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content.strip())
    
print("Master identity document created.")
