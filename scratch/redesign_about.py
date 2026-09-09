# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract Hero
hero_match = re.search(r'(<!-- PAGE HERO .*?</section>)', html, re.DOTALL)
hero_section = hero_match.group(1) if hero_match else ''

# Extract CTA and Footer
cta_match = re.search(r'(<!-- CLOSING CTA.*)', html, re.DOTALL)
cta_footer_section = cta_match.group(1) if cta_match else ''

new_body = f"""
   <!-- MISSION (SPLIT LAYOUT) -->
   <section class="fv-section" style="background:#ffffff; overflow:hidden;">
      <div class="container">
         <div class="row align-items-center">
            <div class="col-lg-6 pr-lg-5 mb-5 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <span class="fv-eyebrow">OUR MISSION</span>
               <h2 class="mb-4" style="color:#111827; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">We don't automate for the sake of automation.</h2>
               <p style="color:#6f7075; font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; margin-bottom:20px;">We first understand how a business actually works.</p>
               <p style="color:#6f7075; font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; margin-bottom:30px;">Then we identify where time, money and productivity are being lost.</p>
               <div style="padding:20px 0; border-top:1px solid #e5e7eb; border-bottom:1px solid #e5e7eb;">
                  <p style="font-family:'Rubik',sans-serif; font-size:20px; font-weight:500; color:#111827; margin:0;">Then we engineer the systems that remove those problems.</p>
               </div>
            </div>
            <div class="col-lg-6 wow fadeInRight" data-wow-delay="0.2s">
               <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop" alt="Business Operations" class="img-fluid" style="box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);">
            </div>
         </div>
      </div>
   </section>

   <!-- THE PROBLEM SECTION (DARK CARDS) -->
   <section class="fv-industries">
      <div class="container">
         <div class="row mb-5">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="fv-eyebrow">THE PROBLEM</span>
               <h2 class="mb-4" style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">Your business shouldn't depend on manual work.</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-industry">
                  <span>01</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Manual Work</h3>
                  <p>Your team repeatedly copies data between systems.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div class="fv-industry">
                  <span>02</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Disconnected Systems</h3>
                  <p>Your software systems don't communicate with each other.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div class="fv-industry">
                  <span>03</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Lost Leads</h3>
                  <p>Leads are lost because follow-ups are entirely manual.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div class="fv-industry">
                  <span>04</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Repetitive Support</h3>
                  <p>Employees answer the exact same customer questions every day.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div class="fv-industry">
                  <span>05</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Spreadsheet Dependency</h3>
                  <p>Your business depends heavily on fragile, manual spreadsheets.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div class="fv-industry">
                  <span>06</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Poor Visibility</h3>
                  <p>Management lacks a clear, real-time operational dashboard.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- SOLUTION SECTION -->
   <section class="fv-section" style="background:#f7f7f5;">
      <div class="container text-center">
         <div class="row">
            <div class="col-lg-10 mx-auto wow fadeInUp" data-wow-delay="0.1s">
               <h2 class="mb-5" style="color:#111827; font-family:'Teko',sans-serif; font-size:56px; letter-spacing:1px; line-height:1.1; text-transform:uppercase;">We turn operational problems into systems that work automatically<span style="color:var(--fv-red);">.</span></h2>
               <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop" alt="Systems that work" class="img-fluid" style="box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
            </div>
         </div>
      </div>
   </section>

   <!-- WHY FLOW VELLO -->
   <section class="fv-section" style="background:#ffffff;">
      <div class="container">
         <div class="row mb-5">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="fv-eyebrow">WHY FLOW VELLO</span>
               <h2 class="mb-4" style="color:#111827; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">Principles that drive results.</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-service-card">
                  <span class="fv-service-number">01</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Start With the Problem</h3>
                  <p>We understand the business before recommending technology.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div class="fv-service-card">
                  <span class="fv-service-number">02</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Build Around Your Business</h3>
                  <p>Your workflows determine the system - not a template.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div class="fv-service-card">
                  <span class="fv-service-number">03</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Connect What You Use</h3>
                  <p>CRM, WhatsApp, email, databases, and tools can work together.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div class="fv-service-card">
                  <span class="fv-service-number">04</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Automate the Work</h3>
                  <p>AI handles repetitive tasks so your team can focus on value.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div class="fv-service-card">
                  <span class="fv-service-number">05</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Engineer for Scale</h3>
                  <p>Systems are designed to evolve as the business grows.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div class="fv-service-card">
                  <span class="fv-service-number">06</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Stay After Launch</h3>
                  <p>We continue improving the system after deployment.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- ENGINEERING SECTION -->
   <section class="fv-section" style="background:var(--fv-dark); color:#fff; position:relative; overflow:hidden;">
      <div style="position:absolute; right:-10%; top:-10%; width:60%; height:120%; background:radial-gradient(circle, rgba(251,56,59,0.1) 0%, transparent 70%); z-index:0;"></div>
      <div class="container" style="position:relative; z-index:1;">
         <div class="row align-items-center">
            <div class="col-lg-6 pr-lg-5 mb-5 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <span class="fv-eyebrow" style="color:rgba(255,255,255,0.6);">ENGINEERING</span>
               <h2 class="mb-4" style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">Business problems deserve engineered solutions.</h2>
               <p class="fv-lead" style="color:#bdbec2;">We design modern SaaS infrastructure and intelligent workflows that connect your operations securely and seamlessly.</p>
            </div>
            <div class="col-lg-5 offset-lg-1 wow fadeInRight" data-wow-delay="0.2s">
               <div style="border-left:2px solid var(--fv-red); padding-left:30px;">
                  <h3 style="color:#fff; font-size:28px; margin-bottom:15px; font-family:'Rubik',sans-serif; font-weight:600;">AI</h3>
                  <h3 style="color:#fff; font-size:28px; margin-bottom:15px; font-family:'Rubik',sans-serif; font-weight:600;">Automation</h3>
                  <h3 style="color:#fff; font-size:28px; margin-bottom:15px; font-family:'Rubik',sans-serif; font-weight:600;">APIs & Databases</h3>
                  <h3 style="color:#fff; font-size:28px; margin-bottom:15px; font-family:'Rubik',sans-serif; font-weight:600;">Custom Software</h3>
                  <h3 style="color:var(--fv-red); font-size:28px; margin-bottom:0; font-family:'Rubik',sans-serif; font-weight:600;">Business Systems</h3>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- WHO WE HELP -->
   <section class="fv-section" style="background:#f9fafb;">
      <div class="container">
         <div class="row mb-5">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="fv-eyebrow">TARGET AUDIENCE</span>
               <h2 class="mb-4" style="color:#111827; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">Who We Help</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div style="position:relative; height:300px; display:flex; align-items:flex-end; padding:30px; background:#111827;">
                  <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=600&auto=format&fit=crop" alt="Agencies" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.4;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:600; margin:0;">Agencies</h3>
               </div>
            </div>
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div style="position:relative; height:300px; display:flex; align-items:flex-end; padding:30px; background:#111827;">
                  <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=600&auto=format&fit=crop" alt="E-commerce" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.4;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:600; margin:0;">E-commerce</h3>
               </div>
            </div>
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="position:relative; height:300px; display:flex; align-items:flex-end; padding:30px; background:#111827;">
                  <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=600&auto=format&fit=crop" alt="Professional Services" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.4;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:600; margin:0;">Professional Services</h3>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="position:relative; height:300px; display:flex; align-items:flex-end; padding:30px; background:var(--fv-dark);">
                  <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=800&auto=format&fit=crop" alt="Growing Businesses" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.3;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">Growing Businesses</h3>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div style="position:relative; height:300px; display:flex; align-items:flex-end; padding:30px; background:var(--fv-red);">
                  <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800&auto=format&fit=crop" alt="Operations-Heavy Companies" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.2;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">Operations-Heavy Companies</h3>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- CORE PHILOSOPHY -->
   <section class="fv-why fv-section">
      <div class="container">
         <div class="row">
            <div class="col-lg-5 mb-5 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <span class="fv-eyebrow">OUR PHILOSOPHY</span>
               <h2 class="mb-4" style="color:#111827; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">Technology should solve problems, not create more of them.</h2>
            </div>
            <div class="col-lg-6 offset-lg-1 wow fadeInRight" data-wow-delay="0.2s">
               <div class="fv-why-card">
                  <strong style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Understand Before We Build</strong>
                  <span>We don't automate a process we haven't completely understood.</span>
               </div>
               <div class="fv-why-card">
                  <strong style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Useful Over Impressive</strong>
                  <span>Technology only matters when it solves a real business problem.</span>
               </div>
               <div class="fv-why-card">
                  <strong style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Simple Beats Complicated</strong>
                  <span>The best system is one the team can actually use without friction.</span>
               </div>
               <div class="fv-why-card">
                  <strong style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Build for the Long Term</strong>
                  <span>Create systems that evolve instead of becoming another technical problem.</span>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- HOW WE WORK -->
   <section class="fv-process fv-section">
      <div class="container">
         <div class="row mb-5">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="fv-eyebrow">HOW WE WORK</span>
               <h2 class="mb-4" style="color:#111827; font-family:'Rubik',sans-serif; font-size:46px; font-weight:600; line-height:1.15; letter-spacing:-1.5px;">From bottleneck to better system.</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-step">
                  <span class="step-no">01</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Discovery</h3>
                  <p>Find the bottleneck.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div class="fv-step">
                  <span class="step-no">02</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Strategy</h3>
                  <p>Design the roadmap.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div class="fv-step">
                  <span class="step-no">03</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Proposal</h3>
                  <p>Make the scope clear.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div class="fv-step">
                  <span class="step-no">04</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Build</h3>
                  <p>Engineer the system.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div class="fv-step">
                  <span class="step-no">05</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">QA & Launch</h3>
                  <p>Test before release.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div class="fv-step">
                  <span class="step-no">06</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Support</h3>
                  <p>Improve after launch.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

"""

# Stitch it all back together
final_html = hero_section + new_body + cta_footer_section

with codecs.open('about.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Redesign complete.")
