# -*- coding: utf-8 -*-
import re

# Read index.html for extracting exact components
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract Process Section
process_match = re.search(r'(<!-- PROCESS \(HOW WE WORK\) -->.*?</section>)', index_html, re.DOTALL)
process_section = process_match.group(1) if process_match else ''

# Extract CTA
cta_match = re.search(r'(<!-- CLOSING CTA \(SPLIT\) -->.*?</section>)', index_html, re.DOTALL)
cta_section = cta_match.group(1) if cta_match else ''

# Read about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# Construct New Content
new_content = f"""
   <!-- PAGE HERO -->
   <section class="fv-page-hero" style="background:#111827; padding:160px 0 100px; position:relative; overflow:hidden;">
      <div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,0.08) 1px,transparent 1px);background-size:30px 30px;z-index:0;opacity:0.6;"></div>
      <div class="container" style="position:relative;z-index:1;">
         <div class="row">
            <div class="col-lg-10 wow fadeInUp" data-wow-delay="0.1s">
               <span class="d-inline-block mb-3" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:2px; text-transform:uppercase;">ABOUT FLOW VELLO</span>
               <h1 style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:64px; font-weight:600; letter-spacing:-1.5px; line-height:1.1; margin-bottom:24px;">We build the systems that make your business run better<span style="color:var(--fv-red);">.</span></h1>
               <p style="color:rgba(255,255,255,0.8); font-family:'Rubik',sans-serif; font-size:20px; line-height:1.7; max-width:750px; margin-bottom:0; font-weight:400;">Flow Vello helps businesses replace repetitive work, disconnected tools and inefficient processes with custom automation, AI agents and software built around how their teams actually work.</p>
            </div>
         </div>
      </div>
   </section>

   <!-- MISSION -->
   <section style="padding:100px 0; background:#ffffff;">
      <div class="container">
         <div class="row">
            <div class="col-lg-10 wow fadeInUp" data-wow-delay="0.1s">
               <h2 style="font-family:'Rubik',sans-serif; font-size:42px; font-weight:600; letter-spacing:-1px; color:#111827; margin-bottom:30px; line-height:1.2;">We don't automate for the sake of automation. We find where your business is losing time, money and productivity -- then engineer a better system.</h2>
               <p style="font-family:'Rubik',sans-serif; font-size:18px; line-height:1.8; color:#4b5563; max-width:850px; margin-bottom:0;">
                  By understanding the existing business and finding bottlenecks, we remove repetitive work and connect disconnected systems. We focus on improving operational efficiency and building long-term systems that scale with you, rather than just selling technology.
               </p>
            </div>
         </div>
      </div>
   </section>

   <!-- PROBLEM SECTION -->
   <section style="padding:100px 0; background:#f9fafb;">
      <div class="container">
         <div class="row mb-5">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">THE PROBLEM</span>
               <h2 style="font-family:'Rubik',sans-serif; font-size:42px; font-weight:600; letter-spacing:-1px; color:#111827;">You might need Flow Vello if...</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-lg-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <ul class="list-unstyled m-0" style="font-family:'Rubik',sans-serif; font-size:18px; color:#4b5563;">
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Your team repeatedly copies data between systems.</span></li>
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Employees answer the same customer questions every day.</span></li>
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Leads are lost because follow-ups are manual.</span></li>
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Your business depends heavily on spreadsheets.</span></li>
               </ul>
            </div>
            <div class="col-lg-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <ul class="list-unstyled m-0" style="font-family:'Rubik',sans-serif; font-size:18px; color:#4b5563;">
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Your software systems don't communicate with each other.</span></li>
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Management lacks a clear operational dashboard.</span></li>
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>Your team is growing but your processes aren't.</span></li>
                  <li class="mb-4 d-flex align-items-start"><i class="fal fa-check-circle mt-1 mr-3" style="color:var(--fv-red); font-size:20px;"></i> <span>You know AI could help but don't know where to start.</span></li>
               </ul>
            </div>
         </div>
         <div class="row mt-4 wow fadeInUp" data-wow-delay="0.4s">
            <div class="col-12">
               <div style="background:#111827; padding:40px 50px; border-radius:12px; border-left:4px solid var(--fv-red); display:flex; align-items:center;">
                  <h3 style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; margin:0; font-weight:500; letter-spacing:-0.5px;">We turn operational problems into systems that work automatically.</h3>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- WHY FLOW VELLO -->
   <section style="padding:100px 0; background:#ffffff;">
      <div class="container">
         <div class="text-center mb-5 pb-3 wow fadeInUp" data-wow-delay="0.1s">
            <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">WHY FLOW VELLO</span>
            <h2 style="color:#111827; font-family:'Rubik',sans-serif; font-size:42px; font-weight:600; letter-spacing:-1px;">Principles that drive results<span style="color:var(--fv-red);">.</span></h2>
         </div>
         <div class="row">
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div style="padding:40px; background:#f9fafb; border-radius:8px; height:100%; transition:0.3s; border: 1px solid rgba(0,0,0,0.05);" class="hover-shadow">
                  <h4 style="margin:0 0 15px; font-size:22px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">We Start With the Problem</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">Understand the business before recommending technology.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div style="padding:40px; background:#f9fafb; border-radius:8px; height:100%; transition:0.3s; border: 1px solid rgba(0,0,0,0.05);" class="hover-shadow">
                  <h4 style="margin:0 0 15px; font-size:22px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">We Build Around Your Business</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">No unnecessary templates or forced processes.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="padding:40px; background:#f9fafb; border-radius:8px; height:100%; transition:0.3s; border: 1px solid rgba(0,0,0,0.05);" class="hover-shadow">
                  <h4 style="margin:0 0 15px; font-size:22px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">We Connect Your Systems</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">CRM, email, WhatsApp, databases, APIs and internal tools can work together.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="padding:40px; background:#f9fafb; border-radius:8px; height:100%; transition:0.3s; border: 1px solid rgba(0,0,0,0.05);" class="hover-shadow">
                  <h4 style="margin:0 0 15px; font-size:22px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">We Automate the Work</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">Let software and AI handle repetitive operational tasks while people remain in control of important decisions.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div style="padding:40px; background:#f9fafb; border-radius:8px; height:100%; transition:0.3s; border: 1px solid rgba(0,0,0,0.05);" class="hover-shadow">
                  <h4 style="margin:0 0 15px; font-size:22px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">We Engineer for Scale</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">Build systems that remain maintainable as the company grows.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div style="padding:40px; background:#f9fafb; border-radius:8px; height:100%; transition:0.3s; border: 1px solid rgba(0,0,0,0.05);" class="hover-shadow">
                  <h4 style="margin:0 0 15px; font-size:22px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">We Stay After Launch</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">Monitor, improve and evolve the system after deployment.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- WHO WE HELP -->
   <section style="padding:100px 0; background:#111827;">
      <div class="container text-center">
         <h2 class="wow fadeInUp" data-wow-delay="0.1s" style="font-family:'Rubik',sans-serif; font-size:42px; font-weight:600; letter-spacing:-1px; color:#ffffff; margin-bottom:20px;">Who We Help</h2>
         <p class="wow fadeInUp" data-wow-delay="0.2s" style="font-family:'Rubik',sans-serif; font-size:18px; color:rgba(255,255,255,0.8); max-width:750px; margin:0 auto 50px; line-height:1.7;">
            Flow Vello is built for businesses where manual work, disconnected systems and inefficient processes are slowing growth.
         </p>
         <div class="d-flex flex-wrap justify-content-center wow fadeInUp" data-wow-delay="0.3s" style="gap:15px; max-width:900px; margin:0 auto;">
            <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#ffffff; padding:12px 28px; border-radius:40px; font-family:'Rubik',sans-serif; font-size:16px; font-weight:500;">Agencies</span>
            <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#ffffff; padding:12px 28px; border-radius:40px; font-family:'Rubik',sans-serif; font-size:16px; font-weight:500;">E-commerce businesses</span>
            <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#ffffff; padding:12px 28px; border-radius:40px; font-family:'Rubik',sans-serif; font-size:16px; font-weight:500;">Professional services</span>
            <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#ffffff; padding:12px 28px; border-radius:40px; font-family:'Rubik',sans-serif; font-size:16px; font-weight:500;">Growing companies</span>
            <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#ffffff; padding:12px 28px; border-radius:40px; font-family:'Rubik',sans-serif; font-size:16px; font-weight:500;">Operations-heavy businesses</span>
         </div>
      </div>
   </section>

   <!-- CORE VALUES -->
   <section style="padding:100px 0; background:#f9fafb;">
      <div class="container">
         <div class="row align-items-center">
            <div class="col-lg-5 mb-5 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">CORE VALUES</span>
               <h2 class="mb-4" style="font-family:'Rubik',sans-serif; font-size:42px; font-weight:600; letter-spacing:-1px; color:#111827; line-height:1.1;">What drives every system we build<span style="color:var(--fv-red);">.</span></h2>
               <p style="font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; color:#4b5563; margin:0;">
                  We design solutions based on practical principles rather than generic claims, ensuring every system delivers real business value.
               </p>
            </div>
            <div class="col-lg-6 offset-lg-1">
               <div class="wow fadeInRight" data-wow-delay="0.2s" style="padding:30px 0; border-top:1px solid rgba(0,0,0,0.1);">
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin:0 0 10px;">Understand Before We Build</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; line-height:1.7; color:#4b5563; margin:0;">We don't automate a process we haven't understood.</p>
               </div>
               <div class="wow fadeInRight" data-wow-delay="0.3s" style="padding:30px 0; border-top:1px solid rgba(0,0,0,0.1);">
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin:0 0 10px;">Useful Over Impressive</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; line-height:1.7; color:#4b5563; margin:0;">Technology only matters when it solves a real business problem.</p>
               </div>
               <div class="wow fadeInRight" data-wow-delay="0.4s" style="padding:30px 0; border-top:1px solid rgba(0,0,0,0.1);">
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin:0 0 10px;">Simple Beats Complicated</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; line-height:1.7; color:#4b5563; margin:0;">The best system is one the team can actually use.</p>
               </div>
               <div class="wow fadeInRight" data-wow-delay="0.5s" style="padding:30px 0; border-top:1px solid rgba(0,0,0,0.1); border-bottom:1px solid rgba(0,0,0,0.1);">
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin:0 0 10px;">Build for the Long Term</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; line-height:1.7; color:#4b5563; margin:0;">Create systems that evolve instead of becoming another technical problem.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

{process_section}

   <!-- PROOF / BRIDGE TO CASE STUDIES -->
   <section style="padding:100px 0; background:#ffffff; text-align:center;">
      <div class="container">
         <h2 class="wow fadeInUp" data-wow-delay="0.1s" style="font-family:'Rubik',sans-serif; font-size:42px; font-weight:600; letter-spacing:-1px; color:#111827; margin-bottom:20px;">Don't take our word for it<span style="color:var(--fv-red);">.</span></h2>
         <p class="wow fadeInUp" data-wow-delay="0.2s" style="font-family:'Rubik',sans-serif; font-size:18px; line-height:1.8; color:#4b5563; max-width:700px; margin:0 auto 40px;">
            See real examples of systems Flow Vello has built and the operational problems they solved.
         </p>
         <a href="case-studies.html" class="fv-dual-btn wow fadeInUp" data-wow-delay="0.3s" style="display:inline-flex;">
            <span class="fv-btn-pill">VIEW CASE STUDIES</span>
            <div class="fv-btn-circle">
               <i class="fal fa-arrow-right arrow-main"></i>
               <i class="fal fa-arrow-right arrow-hover"></i>
            </div>
         </a>
      </div>
   </section>

{cta_section}
"""

new_content = new_content.replace('Ready to automate and scale?', "What's slowing your business down?")
new_content = new_content.replace(
    'Tell us what is slowing your team down. We will help you identify where automation, AI or custom software can create the biggest operational improvement.', 
    "Tell us where your team is losing time, dealing with repetitive work or struggling with disconnected systems. We'll identify where automation, AI or custom software can create the biggest operational improvement."
)

about_content = re.sub(r'<!-- PAGE HERO -->.*<!-- FOOTER -->', new_content + '\n   <!-- FOOTER -->', about_html, flags=re.DOTALL)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)

print("about.html content completely rewritten to match premium UI specifications.")
