# -*- coding: utf-8 -*-
import re
import codecs

with codecs.open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header (everything before PAGE HERO)
header_match = re.search(r'(.*?)(?=<!-- PAGE HERO)', html, re.DOTALL)
header = header_match.group(1) if header_match else ''

# Extract Hero (keep exact hero)
hero_match = re.search(r'(<!-- PAGE HERO .*?</section>)', html, re.DOTALL)
hero = hero_match.group(1) if hero_match else ''

# Extract CTA and Footer
cta_match = re.search(r'(<!-- CLOSING CTA \(SPLIT\).*)', html, re.DOTALL)
cta_footer = cta_match.group(1) if cta_match else ''

new_body = f"""
   <!-- MISSION -->
   <section class="fv-section bg-white text-center">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">OUR MISSION</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#111827; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 30px;">We don't automate for the sake of automation.</h2>
         <div class="wow fadeInUp" data-wow-delay="0.3s" style="max-width:700px; margin:0 auto 60px;">
            <p style="color:#6f7075; font-family:'Rubik',sans-serif; font-size:20px; line-height:1.7; margin-bottom:15px;">We first understand how the business works. We identify bottlenecks, repetitive work and disconnected systems.</p>
            <p style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:500; color:#111827; margin:0;">Then we engineer the systems that remove those problems.</p>
         </div>
         <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop" alt="Business Operations" class="img-fluid wow fadeInUp" data-wow-delay="0.4s" style="border-radius:12px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);">
      </div>
   </section>

   <!-- THE PROBLEM -->
   <section class="fv-industries text-center">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">THE PROBLEM</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 60px;">Your business shouldn't depend on manual work.</h2>
         
         <div class="row text-left justify-content-center">
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-industry">
                  <span>01</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Manual Work</h3>
                  <p>Repeatedly copying data between systems.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div class="fv-industry">
                  <span>02</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Disconnected Systems</h3>
                  <p>Software systems that don't communicate.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div class="fv-industry">
                  <span>03</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Lost Leads</h3>
                  <p>Leads lost due to entirely manual follow-ups.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div class="fv-industry">
                  <span>04</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Repetitive Support</h3>
                  <p>Answering the same customer questions daily.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div class="fv-industry">
                  <span>05</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Spreadsheet Dependency</h3>
                  <p>Relying on fragile, manual spreadsheets.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div class="fv-industry">
                  <span>06</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600;">Poor Visibility</h3>
                  <p>Lacking a real-time operational dashboard.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- TRANSFORMATION -->
   <section class="fv-section text-center" style="background:#f7f7f5;">
      <div class="container">
         <h2 class="wow fadeInUp" data-wow-delay="0.1s" style="color:#111827; font-family:'Teko',sans-serif; font-size:64px; letter-spacing:1px; line-height:1.1; max-width:900px; margin:0 auto 50px; text-transform:uppercase;">We turn operational problems into systems that work automatically<span style="color:var(--fv-red);">.</span></h2>
         
         <div class="wow fadeInUp" data-wow-delay="0.2s" style="background:#ffffff; border-radius:12px; padding:60px 30px; box-shadow:0 15px 35px rgba(0,0,0,0.05); display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:20px;">
            <h3 style="font-size:22px; color:#111827; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Manual Work</h3>
            <i class="fal fa-arrow-right d-none d-md-block" style="color:var(--fv-red); font-size:24px;"></i>
            <i class="fal fa-arrow-down d-md-none" style="color:var(--fv-red); font-size:24px; width:100%;"></i>
            <h3 style="font-size:22px; color:#111827; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Connected Systems</h3>
            <i class="fal fa-arrow-right d-none d-md-block" style="color:var(--fv-red); font-size:24px;"></i>
            <i class="fal fa-arrow-down d-md-none" style="color:var(--fv-red); font-size:24px; width:100%;"></i>
            <h3 style="font-size:22px; color:#111827; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Automation</h3>
            <i class="fal fa-arrow-right d-none d-md-block" style="color:var(--fv-red); font-size:24px;"></i>
            <i class="fal fa-arrow-down d-md-none" style="color:var(--fv-red); font-size:24px; width:100%;"></i>
            <h3 style="font-size:22px; color:var(--fv-red); font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Better Operations</h3>
         </div>
      </div>
   </section>

   <!-- WHY FLOW VELLO -->
   <section class="fv-section bg-white text-center">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">WHY FLOW VELLO</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#111827; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 60px;">Principles that drive results.</h2>
         
         <div class="row text-left justify-content-center">
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-service-card" style="text-align:center;">
                  <span class="fv-service-number d-block mb-3" style="font-size:16px;">01</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; margin-top:0;">Start With the Problem</h3>
                  <p>Understand the business before recommending technology.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div class="fv-service-card" style="text-align:center;">
                  <span class="fv-service-number d-block mb-3" style="font-size:16px;">02</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; margin-top:0;">Build Around Business</h3>
                  <p>Your workflows determine the system - not a template.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div class="fv-service-card" style="text-align:center;">
                  <span class="fv-service-number d-block mb-3" style="font-size:16px;">03</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; margin-top:0;">Connect What You Use</h3>
                  <p>CRM, WhatsApp, email, and tools working together.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div class="fv-service-card" style="text-align:center;">
                  <span class="fv-service-number d-block mb-3" style="font-size:16px;">04</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; margin-top:0;">Automate the Work</h3>
                  <p>AI handles repetition so your team focuses on value.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div class="fv-service-card" style="text-align:center;">
                  <span class="fv-service-number d-block mb-3" style="font-size:16px;">05</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; margin-top:0;">Engineer for Scale</h3>
                  <p>Systems are designed to evolve as the business grows.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div class="fv-service-card" style="text-align:center;">
                  <span class="fv-service-number d-block mb-3" style="font-size:16px;">06</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; margin-top:0;">Stay After Launch</h3>
                  <p>We continue improving the system after deployment.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- CORE VALUES -->
   <section class="fv-section text-center" style="background:#f9fafb;">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">OUR PRINCIPLES</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#111827; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 60px;">Technology should solve problems, not create them.</h2>
         
         <div class="row justify-content-center">
            <div class="col-md-6 col-lg-5 mb-5 wow fadeInUp" data-wow-delay="0.1s">
               <h3 style="font-family:'Rubik',sans-serif; font-size:26px; font-weight:600; color:#111827; margin-bottom:15px;">Understand Before We Build</h3>
            </div>
            <div class="col-md-6 col-lg-5 mb-5 wow fadeInUp" data-wow-delay="0.2s">
               <h3 style="font-family:'Rubik',sans-serif; font-size:26px; font-weight:600; color:#111827; margin-bottom:15px;">Useful Over Impressive</h3>
            </div>
            <div class="col-md-6 col-lg-5 mb-5 wow fadeInUp" data-wow-delay="0.3s">
               <h3 style="font-family:'Rubik',sans-serif; font-size:26px; font-weight:600; color:#111827; margin-bottom:15px;">Simple Beats Complicated</h3>
            </div>
            <div class="col-md-6 col-lg-5 mb-5 wow fadeInUp" data-wow-delay="0.4s">
               <h3 style="font-family:'Rubik',sans-serif; font-size:26px; font-weight:600; color:#111827; margin-bottom:15px;">Build for the Long Term</h3>
            </div>
         </div>
      </div>
   </section>

   <!-- ENGINEERING SECTION -->
   <section class="fv-section text-center" style="background:var(--fv-dark); color:#fff; position:relative; overflow:hidden;">
      <div style="position:absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:100%; height:100%; background:radial-gradient(circle, rgba(251,56,59,0.1) 0%, transparent 70%); z-index:0;"></div>
      <div class="container" style="position:relative; z-index:1;">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s" style="color:rgba(255,255,255,0.6);">ENGINEERING</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 30px;">Business problems deserve engineered solutions.</h2>
         <p class="wow fadeInUp" data-wow-delay="0.3s" style="color:#bdbec2; font-family:'Rubik',sans-serif; font-size:20px; line-height:1.7; max-width:700px; margin:0 auto 60px;">Flow Vello combines AI, automation, software, APIs, databases and business systems to create operational infrastructure built around the way a company actually works.</p>
         
         <div class="wow fadeInUp" data-wow-delay="0.4s" style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:15px 30px;">
            <h3 style="color:#fff; font-size:28px; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">AI</h3>
            <span style="color:var(--fv-red); font-size:24px;">*</span>
            <h3 style="color:#fff; font-size:28px; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Automation</h3>
            <span style="color:var(--fv-red); font-size:24px;">*</span>
            <h3 style="color:#fff; font-size:28px; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">APIs</h3>
            <span style="color:var(--fv-red); font-size:24px;">*</span>
            <h3 style="color:#fff; font-size:28px; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Databases</h3>
            <span style="color:var(--fv-red); font-size:24px;">*</span>
            <h3 style="color:#fff; font-size:28px; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Software</h3>
            <span style="color:var(--fv-red); font-size:24px;">*</span>
            <h3 style="color:var(--fv-red); font-size:28px; font-family:'Rubik',sans-serif; font-weight:600; margin:0;">Business Systems</h3>
         </div>
      </div>
   </section>

   <!-- HOW WE WORK -->
   <section class="fv-process fv-section text-center bg-white">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">OUR PROCESS</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#111827; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 60px;">From bottleneck to better system.</h2>
         
         <div class="row text-left justify-content-center">
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div class="fv-step" style="text-align:center;">
                  <span class="step-no d-block mb-2" style="font-size:16px;">01</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827; font-size:24px; margin-top:0;">Discovery</h3>
                  <p>Find the bottleneck.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div class="fv-step" style="text-align:center;">
                  <span class="step-no d-block mb-2" style="font-size:16px;">02</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827; font-size:24px; margin-top:0;">Strategy</h3>
                  <p>Design the roadmap.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div class="fv-step" style="text-align:center;">
                  <span class="step-no d-block mb-2" style="font-size:16px;">03</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827; font-size:24px; margin-top:0;">Proposal</h3>
                  <p>Make the scope clear.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div class="fv-step" style="text-align:center;">
                  <span class="step-no d-block mb-2" style="font-size:16px;">04</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827; font-size:24px; margin-top:0;">Build</h3>
                  <p>Execute the system.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div class="fv-step" style="text-align:center;">
                  <span class="step-no d-block mb-2" style="font-size:16px;">05</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827; font-size:24px; margin-top:0;">QA & Launch</h3>
                  <p>Test before release.</p>
               </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div class="fv-step" style="text-align:center;">
                  <span class="step-no d-block mb-2" style="font-size:16px;">06</span>
                  <h3 style="font-family:'Rubik',sans-serif; font-weight:600; color:#111827; font-size:24px; margin-top:0;">Support</h3>
                  <p>Improve after launch.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- WHO WE HELP -->
   <section class="fv-section text-center" style="background:#f9fafb;">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">WHO WE HELP</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#111827; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 60px;">Built for businesses where manual work is slowing growth.</h2>
         
         <div class="row text-left justify-content-center">
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div style="position:relative; height:300px; display:flex; align-items:center; justify-content:center; padding:30px; background:#111827; border-radius:12px; overflow:hidden; text-align:center;">
                  <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=600&auto=format&fit=crop" alt="Agencies" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.4;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin:0;">Agencies</h3>
               </div>
            </div>
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div style="position:relative; height:300px; display:flex; align-items:center; justify-content:center; padding:30px; background:#111827; border-radius:12px; overflow:hidden; text-align:center;">
                  <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=600&auto=format&fit=crop" alt="E-commerce" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.4;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin:0;">E-commerce</h3>
               </div>
            </div>
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="position:relative; height:300px; display:flex; align-items:center; justify-content:center; padding:30px; background:#111827; border-radius:12px; overflow:hidden; text-align:center;">
                  <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=600&auto=format&fit=crop" alt="Professional Services" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.4;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin:0;">Professional Services</h3>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="position:relative; height:300px; display:flex; align-items:center; justify-content:center; padding:30px; background:var(--fv-dark); border-radius:12px; overflow:hidden; text-align:center;">
                  <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=800&auto=format&fit=crop" alt="Growing Businesses" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.3;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:36px; font-weight:600; margin:0;">Growing Businesses</h3>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div style="position:relative; height:300px; display:flex; align-items:center; justify-content:center; padding:30px; background:var(--fv-red); border-radius:12px; overflow:hidden; text-align:center;">
                  <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800&auto=format&fit=crop" alt="Operations-Heavy Companies" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.2;">
                  <h3 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:36px; font-weight:600; margin:0;">Operations-Heavy Companies</h3>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- CASE STUDIES BRIDGE -->
   <section class="fv-section bg-white text-center">
      <div class="container">
         <span class="fv-eyebrow wow fadeInUp" data-wow-delay="0.1s">REAL SYSTEMS</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="color:#111827; font-family:'Rubik',sans-serif; font-size:52px; font-weight:600; line-height:1.15; letter-spacing:-1.5px; max-width:850px; margin:0 auto 40px;">We don't just talk about better systems. We build them.</h2>
         <div class="wow fadeInUp" data-wow-delay="0.3s">
            <a href="case-studies.html" class="fv-dual-btn" style="display:inline-flex;">
               <span class="fv-btn-pill">EXPLORE CASE STUDIES</span>
               <div class="fv-btn-circle">
                  <i class="fal fa-arrow-right arrow-main"></i>
                  <i class="fal fa-arrow-right arrow-hover"></i>
               </div>
            </a>
         </div>
      </div>
   </section>

"""

final_html = header + hero + new_body + cta_footer

with codecs.open('about.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Redesign correctly inserted into about.html using strict centered layout.")
