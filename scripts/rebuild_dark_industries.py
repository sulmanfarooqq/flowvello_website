# -*- coding: utf-8 -*-
import os
import re

with open('c:/Users/my/Desktop/chatgpt/services/web-applications.html', 'r', encoding='utf-8', errors='ignore') as f:
    template = f.read()

nav_match = re.search(r'(?s)(.*?)(<section class="fv-page-hero")', template)
nav = nav_match.group(1) if nav_match else ''

cta_match = re.search(r'(?s)(<section class="fv-cta-split[^>]*>.*)', template)
cta_footer = cta_match.group(1) if cta_match else ''

industries = [
    {
        "id": "real-estate",
        "title": "Real Estate & PropTech",
        "hero_desc": "Automated lead routing, MLS integrations, and high-conversion funnels for top-producing brokerages.",
        "bg_img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Real estate moves fast. Manual data entry doesn't.",
        "problem_desc": "If it takes your agents more than 5 minutes to respond to a Zillow lead, that lead is already talking to your competitor. You are losing millions in GCI because your team is manually copy-pasting data between your CRM, your inbox, and your phone.",
        "pillars": [
            {"title": "Automated Lead Routing", "desc": "Instantly capture leads from Zillow, Realtor.com, and Facebook, and route them to the right agent via SMS in under 2 seconds.", "icon": "fa-funnel-dollar"},
            {"title": "Custom MLS Integrations", "desc": "We build direct API connections to your local MLS so your website and internal databases update properties in real-time.", "icon": "fa-database"},
            {"title": "AI Appointment Setters", "desc": "Custom-trained AI agents that text and qualify buyers 24/7, booking highly qualified tours directly into your agents' Calendly.", "icon": "fa-robot"},
            {"title": "Transaction Automation", "desc": "Automated document generation and compliance routing using Dotloop, DocuSign, and your internal CRM.", "icon": "fa-file-signature"}
        ],
        "deliverables": ["HubSpot / Follow Up Boss Setup", "Zillow API Integration", "Automated SMS Nurture", "AI Buyer Qualification Bot", "Dashboard Analytics", "Automated Review Generation"]
    },
    {
        "id": "b2b-saas",
        "title": "B2B SaaS Companies",
        "hero_desc": "Enterprise API integrations, custom dashboard development, and automated onboarding workflows.",
        "bg_img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Your churn rate is a systems problem.",
        "problem_desc": "When users sign up for your software and get a generic welcome email instead of a personalized, data-driven onboarding sequence, they churn. When your sales team cannot see product usage data inside Salesforce, they lose upsells.",
        "pillars": [
            {"title": "Data Warehouse Syncing", "desc": "We connect your PostgreSQL/MongoDB database directly to HubSpot or Salesforce so sales teams have real-time product usage data.", "icon": "fa-database"},
            {"title": "Automated Onboarding", "desc": "Complex email and in-app messaging sequences triggered by exact user behaviors (e.g., 'User hasn't logged in for 3 days').", "icon": "fa-chart-network"},
            {"title": "Custom Analytics Dashboards", "desc": "Executive-level dashboards built in React that aggregate Stripe revenue, product usage, and marketing spend in one place.", "icon": "fa-browser"},
            {"title": "Churn Prevention AI", "desc": "Predictive models that flag accounts at high risk of churning before they actually cancel, triggering automated outreach.", "icon": "fa-brain"}
        ],
        "deliverables": ["Stripe API Automation", "Salesforce Bi-directional Sync", "Custom React Admin Panels", "Intercom / Zendesk Chatbots", "Automated Drip Campaigns", "API Endpoint Architecture"]
    },
    {
        "id": "ecommerce",
        "title": "High-Volume E-Commerce",
        "hero_desc": "Headless architecture, inventory automation, and retention systems for 7-figure and 8-figure brands.",
        "bg_img": "https://images.unsplash.com/photo-1661956602116-aa6865609028?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Shopify templates are killing your conversion rate.",
        "problem_desc": "When your store takes 4 seconds to load on mobile, you lose 40% of your traffic instantly. When your abandoned cart emails are generic, you leave millions on the table. Standard out-of-the-box setups cannot scale to 8 figures.",
        "pillars": [
            {"title": "Headless Shopify Builds", "desc": "We decouple your frontend using Next.js or React, delivering sub-second load times that drastically increase conversion rates.", "icon": "fa-shopping-cart"},
            {"title": "Advanced Klaviyo Flows", "desc": "Hyper-segmented email and SMS automation sequences based on purchase history, browsing behavior, and LTV.", "icon": "fa-envelope-open-dollar"},
            {"title": "Inventory Syncing", "desc": "Automated API integrations between Shopify, your 3PL warehouse, and your ERP to prevent overselling and manual stock updates.", "icon": "fa-boxes"},
            {"title": "Post-Purchase Automation", "desc": "Automated review requests, upsell offers, and shipping notifications that turn one-time buyers into loyal subscribers.", "icon": "fa-box-heart"}
        ],
        "deliverables": ["Headless Frontend Development", "Klaviyo Advanced Segmentation", "3PL / ERP API Integrations", "Subscription Model Engineering", "Automated Upsell Funnels", "Sub-second Lighthouse Scores"]
    },
    {
        "id": "legal",
        "title": "Law Firms & Legal Practices",
        "hero_desc": "Secure client portals, automated intake forms, and case management integrations for modern practices.",
        "bg_img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "Billable hours are being wasted on administrative chaos.",
        "problem_desc": "Your attorneys are spending hours hunting down client documents, manually entering data into Clio, and chasing signatures. This is non-billable time that destroys your firm's profitability.",
        "pillars": [
            {"title": "Automated Client Intake", "desc": "Secure, dynamic web forms that capture client data and automatically create matters in Clio or PracticePanther.", "icon": "fa-file-signature"},
            {"title": "Secure Document Portals", "desc": "Encrypted environments where clients can securely upload discovery documents and track case progress without emailing your paralegals.", "icon": "fa-lock-alt"},
            {"title": "Consultation Routing", "desc": "Automated qualification bots that screen leads and only book high-value, relevant cases onto an attorney's calendar.", "icon": "fa-calendar-check"},
            {"title": "Automated Document Prep", "desc": "Systems that take intake data and automatically populate standard retainers and pleadings via DocuSign APIs.", "icon": "fa-file-invoice"}
        ],
        "deliverables": ["Clio / PracticePanther Integration", "DocuSign API Automation", "Secure Client Dashboard", "Automated Intake Web Forms", "Case Status SMS Alerts", "HIPAA/Confidentiality Compliance"]
    },
    {
        "id": "healthcare",
        "title": "Healthcare Clinics & Med Spas",
        "hero_desc": "HIPAA-compliant data routing, automated appointment follow-ups, and reputation management.",
        "bg_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "No-shows and manual follow-ups are draining your revenue.",
        "problem_desc": "If your front desk is manually calling patients to confirm appointments or asking them to fill out paper intake forms in the waiting room, you are operating in the past. It ruins the patient experience and increases no-show rates.",
        "pillars": [
            {"title": "HIPAA-Compliant Automation", "desc": "Secure data pipelines that move patient intake forms directly into your EMR/EHR system without violating privacy laws.", "icon": "fa-shield-check"},
            {"title": "No-Show Reduction Systems", "desc": "Automated SMS and WhatsApp sequences that confirm appointments, send prep instructions, and handle automated rescheduling.", "icon": "fa-calendar-plus"},
            {"title": "Reputation Engine", "desc": "Post-appointment automated workflows that intercept negative feedback privately and push 5-star reviews to Google.", "icon": "fa-star"},
            {"title": "Membership Billing", "desc": "Automated recurring billing architectures for Med Spas and concierge clinics using Stripe and secure payment gateways.", "icon": "fa-credit-card"}
        ],
        "deliverables": ["EMR / EHR API Integration", "HIPAA-Compliant Intake Forms", "Automated Appointment Reminders", "Google Review Automation", "Concierge Membership Portals", "WhatsApp Patient Support Bots"]
    },
    {
        "id": "financial",
        "title": "Financial Services & Wealth Management",
        "hero_desc": "Secure document routing, CRM automation, and client reporting dashboards for high-net-worth advisors.",
        "bg_img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1920&q=80",
        "problem_title": "High-net-worth clients expect seamless digital experiences.",
        "problem_desc": "You cannot manage millions in AUM while asking clients to email PDFs or manually scheduling annual reviews. The friction in your onboarding and reporting process makes you look outdated to modern investors.",
        "pillars": [
            {"title": "Client Wealth Dashboards", "desc": "Custom reporting portals that aggregate portfolio data from multiple financial APIs into a single, beautiful client experience.", "icon": "fa-chart-line"},
            {"title": "Frictionless Onboarding", "desc": "Secure digital workflows that capture sensitive financial data, ID verification, and e-signatures seamlessly.", "icon": "fa-user-check"},
            {"title": "CRM Automation", "desc": "Automated triggers for annual review scheduling, compliance document renewals, and high-touch birthday/milestone outreach.", "icon": "fa-users-cog"},
            {"title": "Secure Document Routing", "desc": "Automated pipelines that move tax documents and statements directly to secure storage without sitting in vulnerable email inboxes.", "icon": "fa-file-invoice"}
        ],
        "deliverables": ["Custom Reporting Portals", "Salesforce Financial Services Sync", "Plaid / Finicity Integrations", "Automated KYC/AML Workflows", "Secure File Vault Architecture", "Automated Review Scheduling"]
    }
]

for ind in industries:
    middle = f'''
   <!-- HERO SECTION -->
   <section class="fv-page-hero" style="background: linear-gradient(rgba(17,24,39,0.8), rgba(17,24,39,0.9)), url('{ind["bg_img"]}') no-repeat center center/cover; padding: 180px 0 120px 0; border-bottom: 1px solid #1f2937;">
        <div class="container text-center">
           <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s" style="color:#fb383b; letter-spacing:2px; font-weight: 700; text-transform:uppercase;">INDUSTRY SOLUTIONS</span>
           <h1 class="wow fadeInUp" data-wow-delay="0.2s" style="font-family:'Rubik', sans-serif; font-weight:600; font-size: 64px; letter-spacing:-2px; color: #ffffff; max-width: 900px; margin: 15px auto;">
              {ind["title"]}
           </h1>
           <p class="fv-lead wow fadeInUp" data-wow-delay="0.3s" style="font-family: 'Rubik', sans-serif; font-size: 22px; color: #9ca3af; max-width: 800px; margin: 20px auto 0; line-height:1.6;">
              {ind["hero_desc"]}
           </p>
        </div>
   </section>

   <!-- THE PROBLEM SECTION (DARK) -->
   <section class="fv-process-dark py-5" style="padding-top: 120px !important; padding-bottom: 120px !important; border-bottom: 1px solid rgba(255,255,255,0.05);">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-5 mb-lg-0 wow fadeInLeft">
                    <span class="fv-eyebrow" style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 14px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 20px; display: inline-block;">THE PROBLEM</span>
                    <h2 style="font-family:'Rubik', sans-serif; font-size: 48px; font-weight: 600; color: #ffffff; letter-spacing: -1.5px; margin-bottom: 24px; line-height: 1.15;">
                        {ind["problem_title"]}
                    </h2>
                    <p style="color: #9ca3af; font-size: 20px; font-family:'Rubik', sans-serif; line-height: 1.6; margin-bottom: 0;">
                        {ind["problem_desc"]}
                    </p>
                </div>
                <div class="col-lg-5 offset-lg-1 wow fadeInRight">
                    <div style="background: rgba(255,255,255,0.02); padding: 50px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05); box-shadow: 0 20px 40px rgba(0,0,0,0.4);">
                        <h4 style="font-family:'Rubik', sans-serif; font-size: 22px; font-weight: 600; color: #ffffff; margin-bottom: 24px;">The Cost of Inaction:</h4>
                        <ul style="list-style: none; padding: 0; margin: 0;">
                            <li style="margin-bottom: 16px; color: #fb383b; font-weight: 500; font-size: 18px; display: flex; align-items: flex-start; gap: 12px;"><i class="fal fa-times-circle" style="margin-top: 4px;"></i> <span>Lost revenue to faster competitors</span></li>
                            <li style="margin-bottom: 16px; color: #fb383b; font-weight: 500; font-size: 18px; display: flex; align-items: flex-start; gap: 12px;"><i class="fal fa-times-circle" style="margin-top: 4px;"></i> <span>Burned out staff doing manual entry</span></li>
                            <li style="color: #fb383b; font-weight: 500; font-size: 18px; display: flex; align-items: flex-start; gap: 12px;"><i class="fal fa-times-circle" style="margin-top: 4px;"></i> <span>Unscalable, fragile infrastructure</span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
   </section>

   <!-- THE SOLUTION GRID (DARK) -->
   <section class="fv-process-dark py-5" style="padding-top: 120px !important; padding-bottom: 120px !important;">
        <div class="container">
            <div class="text-left mb-5 pb-3">
                <span style="color: #fb383b; font-family: 'Rubik', sans-serif; font-size: 14px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; display: inline-block;">ARCHITECTURE</span>
                <h2 style="font-family:'Rubik', sans-serif; font-size: 52px; font-weight: 600; color: #ffffff; letter-spacing: -1.5px; margin: 0; line-height: 1.15; max-width: 800px;">
                    How we engineer scale.
                </h2>
            </div>
            
            <div class="row">
                <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
                    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); height: 100%; transition: all 0.3s ease;">
                        <i class="fal {ind["pillars"][0]["icon"]}" style="font-size: 40px; color: #fb383b; margin-bottom: 30px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 26px; font-weight: 600; color: #ffffff; margin-bottom: 16px; letter-spacing: -0.5px;">{ind["pillars"][0]["title"]}</h3>
                        <p style="color: #9ca3af; font-size: 18px; line-height: 1.7; margin: 0;">{ind["pillars"][0]["desc"]}</p>
                    </div>
                </div>
                <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
                    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); height: 100%; transition: all 0.3s ease;">
                        <i class="fal {ind["pillars"][1]["icon"]}" style="font-size: 40px; color: #fb383b; margin-bottom: 30px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 26px; font-weight: 600; color: #ffffff; margin-bottom: 16px; letter-spacing: -0.5px;">{ind["pillars"][1]["title"]}</h3>
                        <p style="color: #9ca3af; font-size: 18px; line-height: 1.7; margin: 0;">{ind["pillars"][1]["desc"]}</p>
                    </div>
                </div>
                <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
                    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); height: 100%; transition: all 0.3s ease;">
                        <i class="fal {ind["pillars"][2]["icon"]}" style="font-size: 40px; color: #fb383b; margin-bottom: 30px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 26px; font-weight: 600; color: #ffffff; margin-bottom: 16px; letter-spacing: -0.5px;">{ind["pillars"][2]["title"]}</h3>
                        <p style="color: #9ca3af; font-size: 18px; line-height: 1.7; margin: 0;">{ind["pillars"][2]["desc"]}</p>
                    </div>
                </div>
                <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
                    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); height: 100%; transition: all 0.3s ease;">
                        <i class="fal {ind["pillars"][3]["icon"]}" style="font-size: 40px; color: #fb383b; margin-bottom: 30px;"></i>
                        <h3 style="font-family: 'Rubik', sans-serif; font-size: 26px; font-weight: 600; color: #ffffff; margin-bottom: 16px; letter-spacing: -0.5px;">{ind["pillars"][3]["title"]}</h3>
                        <p style="color: #9ca3af; font-size: 18px; line-height: 1.7; margin: 0;">{ind["pillars"][3]["desc"]}</p>
                    </div>
                </div>
            </div>
        </div>
   </section>

   <!-- DELIVERABLES LIST (DARK) -->
   <section class="fv-process-dark py-5" style="padding-top: 80px !important; padding-bottom: 120px !important; border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container text-center">
            <h3 style="font-family:'Rubik', sans-serif; font-size: 36px; font-weight: 600; color: #ffffff; letter-spacing: -1.5px; margin-bottom: 50px;">Technical Deliverables</h3>
            <div class="row justify-content-center">
                <div class="col-lg-9">
                    <div class="d-flex flex-wrap justify-content-center" style="gap: 16px;">
                        <span style="background: rgba(251,56,59,0.1); color: #fb383b; padding: 14px 28px; border-radius: 9999px; font-weight: 600; font-size: 16px; border: 1px solid rgba(251,56,59,0.2);">{ind["deliverables"][0]}</span>
                        <span style="background: rgba(251,56,59,0.1); color: #fb383b; padding: 14px 28px; border-radius: 9999px; font-weight: 600; font-size: 16px; border: 1px solid rgba(251,56,59,0.2);">{ind["deliverables"][1]}</span>
                        <span style="background: rgba(251,56,59,0.1); color: #fb383b; padding: 14px 28px; border-radius: 9999px; font-weight: 600; font-size: 16px; border: 1px solid rgba(251,56,59,0.2);">{ind["deliverables"][2]}</span>
                        <span style="background: rgba(251,56,59,0.1); color: #fb383b; padding: 14px 28px; border-radius: 9999px; font-weight: 600; font-size: 16px; border: 1px solid rgba(251,56,59,0.2);">{ind["deliverables"][3]}</span>
                        <span style="background: rgba(251,56,59,0.1); color: #fb383b; padding: 14px 28px; border-radius: 9999px; font-weight: 600; font-size: 16px; border: 1px solid rgba(251,56,59,0.2);">{ind["deliverables"][4]}</span>
                        <span style="background: rgba(251,56,59,0.1); color: #fb383b; padding: 14px 28px; border-radius: 9999px; font-weight: 600; font-size: 16px; border: 1px solid rgba(251,56,59,0.2);">{ind["deliverables"][5]}</span>
                    </div>
                </div>
            </div>
        </div>
   </section>
'''
    page_html = nav + middle + cta_footer
    page_html = re.sub(r'<title>.*?</title>', f'<title>{ind["title"]} Solutions | Flow Vello</title>', page_html)
    
    with open(f'c:/Users/my/Desktop/chatgpt/industries/{ind["id"]}.html', 'w', encoding='utf-8') as fw:
        fw.write(page_html)

print("Industries rebuilt in pure dark mode.")
