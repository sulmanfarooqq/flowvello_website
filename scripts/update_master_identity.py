import os

file_path = 'c:/Users/my/Desktop/strategy/12_Master_Agency_Identity.txt'

content = '''FLOW VELLO: THE MASTER DIRECTORY & FULFILLMENT MATRIX

This is your entire agency mapped out. You are attempting to run a 4-Phase Full-Service Agency. 
As a solo founder, you cannot fulfill all of this yourself. This document dictates exactly what tools/talent you use to fulfill each phase when an order comes in.

--- PHASE 01: CREATIVE (The Visual Layer) ---
What you sell: High-impact branding, UI/UX, and video.
Fulfillment Tools & Talent needed:
- Graphic & Social Media Design: Figma, Adobe Illustrator, Canva Pro. 
- Video Editing: Premiere Pro, After Effects, CapCut.
- 3D & VFX: Blender, Cinema4D. (You must outsource this to specialized 3D artists, you cannot do this yourself).
- UI/UX Design: Figma (Strictly for prototyping before Phase 02 begins).

--- PHASE 02: DEVELOPMENT (The Engineering Layer) ---
What you sell: Custom websites, e-commerce, and software.
Fulfillment Tools & Talent needed:
- Web Apps & Desktop Apps: React, Node.js, Electron, Next.js.
- Web-Based Games: WebGL, Unity (WebGL export), Three.js. (Requires highly specialized game devs).
- WordPress & Wix: Elementor, custom PHP themes. (Low ticket, delegate to junior web designers).
- Shopify Stores: Liquid templates, Shopify CLI.

--- PHASE 03: MARKETING (The Growth Layer) ---
What you sell: Driving traffic and leads.
Fulfillment Tools & Talent needed:
- Email Marketing: Klaviyo, ActiveCampaign, Mailchimp.
- Digital Marketing (PPC/SEO): Google Ads Manager, Ahrefs, SEMrush. 
- Platform Management (Upwork/Fiverr): Custom SOPs for bidding and profile ranking.
- LinkedIn Growth: Expandi, Sales Navigator, Taplio.

--- PHASE 04: AUTOMATION (The High-Ticket Layer) ---
What you sell: Eliminating bottlenecks and manual labor using AI and system architecture.
Fulfillment Tools & Talent needed:
- AI Agents & Calling Agents: Voiceflow, Bland AI, Vapi, OpenAI API.
- Custom Dashboards: Retool, Supabase, Grafana, Tableau.
- API & Integration: Make.com, n8n, custom Python scripts.
- GoHighLevel (GHL): Native GHL workflows, sub-accounts, snapshots.

--- THE BRUTAL WARNING ---
Phases 1, 2, and 3 are highly commoditized. Everyone sells Wix sites and Graphic Design. 
Phase 4 (Automation & AI) is where the $10,000+ retainers are. 
If you try to QA a 3D VFX project while simultaneously debugging a webhook for an AI Calling Agent, your agency will collapse. Delegate Phase 1-3 to trusted contractors immediately, and spend all your time selling Phase 4.'''

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content.strip())
    
print("Master identity document updated with all 4 phases.")
