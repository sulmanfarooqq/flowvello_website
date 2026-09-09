# -*- coding: utf-8 -*-
import re
import codecs

# Read index.html for extracting exact components
with codecs.open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    index_html = f.read()

process_match = re.search(r'(<!-- PROCESS \(HOW WE WORK\) -->.*?</section>)', index_html, re.DOTALL)
process_section = process_match.group(1) if process_match else ''

cta_match = re.search(r'(<!-- CLOSING CTA \(SPLIT\) -->.*?</section>)', index_html, re.DOTALL)
cta_section = cta_match.group(1) if cta_match else ''

with codecs.open('about.html', 'r', encoding='utf-8', errors='ignore') as f:
    about_html = f.read()

new_content = f"""
   <!-- PAGE HERO (VISUAL) -->
   <section class="fv-page-hero" style="background:#111827; padding:180px 0 120px; position:relative; overflow:hidden;">
      <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920&auto=format&fit=crop" alt="Abstract Background" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; opacity:0.3; filter: grayscale(100%) contrast(1.2);">
      <div style="position:absolute;inset:0;background:linear-gradient(to bottom, rgba(17,24,39,0.7) 0%, rgba(17,24,39,1) 100%);z-index:1;"></div>
      
      <div class="container" style="position:relative;z-index:2;">
         <div class="row align-items-center">
            <div class="col-lg-9 wow fadeInUp" data-wow-delay="0.1s">
               <span class="d-inline-block mb-3" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:2px; text-transform:uppercase;">ABOUT FLOW VELLO</span>
               <h1 style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:72px; font-weight:600; letter-spacing:-1.5px; line-height:1.05; margin-bottom:30px;">We build the systems that make businesses run better<span style="color:var(--fv-red);">.</span></h1>
               <p style="color:rgba(255,255,255,0.8); font-family:'Rubik',sans-serif; font-size:22px; line-height:1.6; max-width:800px; margin-bottom:0; font-weight:300;">Flow Vello helps businesses eliminate repetitive work, connect disconnected systems and build smarter operations through automation, AI agents and custom software.</p>
            </div>
         </div>
      </div>
   </section>

   <!-- MISSION (SPLIT LAYOUT) -->
   <section style="padding:120px 0; background:#ffffff; overflow:hidden;">
      <div class="container">
         <div class="row align-items-center">
            <div class="col-lg-6 pr-lg-5 mb-5 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <span class="d-inline-block mb-3" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">OUR MISSION</span>
               <h2 style="font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px; color:#111827; margin-bottom:30px; line-height:1.15;">We don't automate for the sake of automation.</h2>
               <p style="font-family:'Rubik',sans-serif; font-size:18px; line-height:1.8; color:#4b5563; margin-bottom:20px;">We first understand how a business actually works.</p>
               <p style="font-family:'Rubik',sans-serif; font-size:18px; line-height:1.8; color:#4b5563; margin-bottom:20px;">Then we identify where time, money and productivity are being lost.</p>
               <div style="padding:20px 0; border-top:1px solid #e5e7eb; border-bottom:1px solid #e5e7eb; margin-top:30px;">
                  <p style="font-family:'Rubik',sans-serif; font-size:20px; font-weight:500; color:#111827; margin:0;">Then we engineer the systems that remove those problems.</p>
               </div>
            </div>
            <div class="col-lg-6 wow fadeInRight" data-wow-delay="0.2s">
               <div style="position:relative; border-radius:12px; overflow:hidden; box-shadow:0 25px 50px -12px rgba(0,0,0,0.15);">
                  <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop" alt="Business Operations Diagram" style="width:100%; display:block; filter: grayscale(20%);">
                  <div style="position:absolute; inset:0; background:linear-gradient(45deg, rgba(251,56,59,0.2) 0%, transparent 100%);"></div>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- THE PROBLEM SECTION -->
   <section style="padding:120px 0; background:#f9fafb;">
      <div class="container">
         <div class="row mb-5 pb-3">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">THE PROBLEM</span>
               <h2 style="font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px; color:#111827;">You might need Flow Vello if...</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div style="background:#ffffff; padding:40px 30px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); height:100%; border-top:3px solid var(--fv-red);">
                  <i class="fal fa-copy mb-4" style="font-size:32px; color:#111827;"></i>
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin-bottom:15px;">Manual Work</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; color:#4b5563; line-height:1.6; margin:0;">Your team repeatedly copies data between systems.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div style="background:#ffffff; padding:40px 30px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); height:100%; border-top:3px solid var(--fv-red);">
                  <i class="fal fa-plug mb-4" style="font-size:32px; color:#111827;"></i>
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin-bottom:15px;">Disconnected Systems</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; color:#4b5563; line-height:1.6; margin:0;">Your software systems don't communicate with each other.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="background:#ffffff; padding:40px 30px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); height:100%; border-top:3px solid var(--fv-red);">
                  <i class="fal fa-user-minus mb-4" style="font-size:32px; color:#111827;"></i>
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin-bottom:15px;">Lost Leads</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; color:#4b5563; line-height:1.6; margin:0;">Leads are lost because follow-ups are entirely manual.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="background:#ffffff; padding:40px 30px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); height:100%; border-top:3px solid var(--fv-red);">
                  <i class="fal fa-headset mb-4" style="font-size:32px; color:#111827;"></i>
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin-bottom:15px;">Repetitive Support</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; color:#4b5563; line-height:1.6; margin:0;">Employees answer the exact same customer questions every day.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div style="background:#ffffff; padding:40px 30px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); height:100%; border-top:3px solid var(--fv-red);">
                  <i class="fal fa-table mb-4" style="font-size:32px; color:#111827;"></i>
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin-bottom:15px;">Spreadsheet Dependency</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; color:#4b5563; line-height:1.6; margin:0;">Your business depends heavily on fragile, manual spreadsheets.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4 wow fadeInUp" data-wow-delay="0.6s">
               <div style="background:#ffffff; padding:40px 30px; border-radius:12px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); height:100%; border-top:3px solid var(--fv-red);">
                  <i class="fal fa-chart-line-down mb-4" style="font-size:32px; color:#111827;"></i>
                  <h4 style="font-family:'Rubik',sans-serif; font-size:22px; font-weight:600; color:#111827; margin-bottom:15px;">Poor Visibility</h4>
                  <p style="font-family:'Rubik',sans-serif; font-size:16px; color:#4b5563; line-height:1.6; margin:0;">Management lacks a clear, real-time operational dashboard.</p>
               </div>
            </div>
         </div>
         
         <div class="row mt-5 pt-3 wow fadeInUp" data-wow-delay="0.7s">
            <div class="col-12 text-center">
               <div style="display:inline-block; width:2px; height:60px; background:var(--fv-red); margin-bottom:30px;"></div>
               <h3 style="color:#111827; font-family:'Rubik',sans-serif; font-size:42px; margin:0; font-weight:600; letter-spacing:-1px;">We turn operational problems into systems that work automatically.</h3>
            </div>
         </div>
      </div>
   </section>

   <!-- WHY FLOW VELLO -->
   <section style="padding:120px 0; background:#ffffff;">
      <div class="container">
         <div class="text-center mb-5 pb-4 wow fadeInUp" data-wow-delay="0.1s">
            <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">WHY FLOW VELLO</span>
            <h2 style="color:#111827; font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px;">Principles that drive results<span style="color:var(--fv-red);">.</span></h2>
         </div>
         <div class="row">
            <div class="col-md-6 col-lg-4 mb-5 wow fadeInUp" data-wow-delay="0.1s">
               <div style="padding-right:20px;">
                  <h4 style="margin:0 0 15px; font-size:24px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Start With the Problem</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">We understand the business before recommending technology.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-5 wow fadeInUp" data-wow-delay="0.2s">
               <div style="padding-right:20px;">
                  <h4 style="margin:0 0 15px; font-size:24px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Build Around Your Business</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">Your workflows determine the system - not a template.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-5 wow fadeInUp" data-wow-delay="0.3s">
               <div style="padding-right:20px;">
                  <h4 style="margin:0 0 15px; font-size:24px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Connect What You Already Use</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">CRM, WhatsApp, email, databases, APIs and internal tools can work together.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-5 wow fadeInUp" data-wow-delay="0.4s">
               <div style="padding-right:20px;">
                  <h4 style="margin:0 0 15px; font-size:24px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Automate the Work</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">AI and software handle repetitive tasks so your team can focus on higher-value work.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-5 wow fadeInUp" data-wow-delay="0.5s">
               <div style="padding-right:20px;">
                  <h4 style="margin:0 0 15px; font-size:24px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Engineer for Scale</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">Systems are designed to evolve as the business grows.</p>
               </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-5 wow fadeInUp" data-wow-delay="0.6s">
               <div style="padding-right:20px;">
                  <h4 style="margin:0 0 15px; font-size:24px; font-family:'Rubik',sans-serif; font-weight:600; color:#111827;">Stay After Launch</h4>
                  <p style="margin:0; color:#4b5563; line-height:1.7; font-size:16px; font-family:'Rubik',sans-serif;">We continue improving the system after deployment.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- ENGINEERING / TECHNOLOGY SECTION -->
   <section style="padding:120px 0; background:#111827; position:relative; overflow:hidden;">
      <div style="position:absolute; right:-10%; top:-10%; width:60%; height:120%; background:radial-gradient(circle, rgba(251,56,59,0.1) 0%, transparent 70%); z-index:0;"></div>
      <div class="container" style="position:relative; z-index:1;">
         <div class="row align-items-center">
            <div class="col-lg-6 pr-lg-5 mb-5 mb-lg-0 wow fadeInLeft" data-wow-delay="0.1s">
               <span class="d-inline-block mb-3" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">ENGINEERING</span>
               <h2 style="font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px; color:#ffffff; margin-bottom:30px; line-height:1.15;">Business problems deserve engineered solutions.</h2>
               <p style="font-family:'Rubik',sans-serif; font-size:18px; line-height:1.8; color:#bdbec2; margin-bottom:0;">
                  We design modern SaaS infrastructure and intelligent workflows that connect your operations securely and seamlessly.
               </p>
            </div>
            <div class="col-lg-5 offset-lg-1 wow fadeInRight" data-wow-delay="0.2s">
               <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:40px;">
                  <ul class="list-unstyled m-0">
                     <li style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:500; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:20px; display:flex; justify-content:space-between;"><span>AI</span> <i class="fal fa-plus text-muted"></i></li>
                     <li style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:500; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:20px; display:flex; justify-content:space-between;"><span>Automation</span> <i class="fal fa-plus text-muted"></i></li>
                     <li style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:500; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:20px; display:flex; justify-content:space-between;"><span>APIs & Databases</span> <i class="fal fa-plus text-muted"></i></li>
                     <li style="color:#ffffff; font-family:'Rubik',sans-serif; font-size:24px; font-weight:500; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:20px; display:flex; justify-content:space-between;"><span>Custom Software</span> <i class="fal fa-plus text-muted"></i></li>
                     <li style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:24px; font-weight:600; margin:0; display:flex; justify-content:space-between;"><span>Business Systems</span> <i class="fal fa-check"></i></li>
                  </ul>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- WHO WE HELP (VISUAL GRID) -->
   <section style="padding:120px 0; background:#f9fafb;">
      <div class="container">
         <div class="row mb-5 pb-3">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">TARGET AUDIENCE</span>
               <h2 style="font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px; color:#111827;">Who We Help</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div style="position:relative; height:300px; border-radius:12px; overflow:hidden; display:flex; align-items:flex-end; padding:30px;">
                  <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=600&auto=format&fit=crop" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; filter:brightness(0.5);">
                  <h4 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">Agencies</h4>
               </div>
            </div>
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div style="position:relative; height:300px; border-radius:12px; overflow:hidden; display:flex; align-items:flex-end; padding:30px;">
                  <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=600&auto=format&fit=crop" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; filter:brightness(0.5);">
                  <h4 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">E-commerce</h4>
               </div>
            </div>
            <div class="col-md-4 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="position:relative; height:300px; border-radius:12px; overflow:hidden; display:flex; align-items:flex-end; padding:30px;">
                  <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=600&auto=format&fit=crop" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; filter:brightness(0.5);">
                  <h4 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">Professional Services</h4>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="position:relative; height:300px; border-radius:12px; overflow:hidden; display:flex; align-items:flex-end; padding:30px;">
                  <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=800&auto=format&fit=crop" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; filter:brightness(0.5);">
                  <h4 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">Growing Businesses</h4>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.5s">
               <div style="position:relative; height:300px; border-radius:12px; overflow:hidden; display:flex; align-items:flex-end; padding:30px;">
                  <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800&auto=format&fit=crop" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0; filter:brightness(0.5);">
                  <h4 style="position:relative; z-index:1; color:#ffffff; font-family:'Rubik',sans-serif; font-size:28px; font-weight:600; margin:0;">Operations-Heavy Companies</h4>
               </div>
            </div>
         </div>
      </div>
   </section>

   <!-- CORE VALUES -->
   <section style="padding:120px 0; background:#ffffff;">
      <div class="container">
         <div class="row mb-5 pb-3">
            <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.1s">
               <span class="d-inline-block mb-2" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">PHILOSOPHY</span>
               <h2 style="font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px; color:#111827;">Core Values</h2>
            </div>
         </div>
         <div class="row">
            <div class="col-lg-6 mb-4 wow fadeInUp" data-wow-delay="0.1s">
               <div style="padding:50px; background:#f9fafb; border-radius:12px; height:100%; display:flex; flex-direction:column; justify-content:center;">
                  <h3 style="color:#111827; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin-bottom:20px; letter-spacing:-0.5px;">Understand Before We Build</h3>
                  <p style="color:#4b5563; font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; margin:0;">We don't automate a process we haven't completely understood.</p>
               </div>
            </div>
            <div class="col-lg-6 mb-4 wow fadeInUp" data-wow-delay="0.2s">
               <div style="padding:50px; background:#f9fafb; border-radius:12px; height:100%; display:flex; flex-direction:column; justify-content:center;">
                  <h3 style="color:#111827; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin-bottom:20px; letter-spacing:-0.5px;">Useful Over Impressive</h3>
                  <p style="color:#4b5563; font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; margin:0;">Technology only matters when it solves a real business problem.</p>
               </div>
            </div>
            <div class="col-lg-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="padding:50px; background:#f9fafb; border-radius:12px; height:100%; display:flex; flex-direction:column; justify-content:center;">
                  <h3 style="color:#111827; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin-bottom:20px; letter-spacing:-0.5px;">Simple Beats Complicated</h3>
                  <p style="color:#4b5563; font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; margin:0;">The best system is one the team can actually use without friction.</p>
               </div>
            </div>
            <div class="col-lg-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="padding:50px; background:#f9fafb; border-radius:12px; height:100%; display:flex; flex-direction:column; justify-content:center;">
                  <h3 style="color:#111827; font-family:'Rubik',sans-serif; font-size:32px; font-weight:600; margin-bottom:20px; letter-spacing:-0.5px;">Build for the Long Term</h3>
                  <p style="color:#4b5563; font-family:'Rubik',sans-serif; font-size:18px; line-height:1.7; margin:0;">Create systems that evolve instead of becoming another technical problem.</p>
               </div>
            </div>
         </div>
      </div>
   </section>

{process_section}

   <!-- PROOF / BRIDGE TO CASE STUDIES -->
   <section style="padding:120px 0; background:#f9fafb; text-align:center;">
      <div class="container">
         <span class="d-inline-block mb-3 wow fadeInUp" data-wow-delay="0.1s" style="color:var(--fv-red); font-family:'Rubik',sans-serif; font-size:14px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">CASE STUDIES</span>
         <h2 class="wow fadeInUp" data-wow-delay="0.2s" style="font-family:'Rubik',sans-serif; font-size:48px; font-weight:600; letter-spacing:-1.5px; color:#111827; margin-bottom:30px;">We don't just talk about systems. We build them<span style="color:var(--fv-red);">.</span></h2>
         
         <div class="row mt-5 mb-5 text-left">
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.3s">
               <div style="background:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 10px 15px -3px rgba(0,0,0,0.1);">
                  <img src="img/case-study-1.webp" alt="Case Study 1" style="width:100%; height:250px; object-fit:cover;">
                  <div style="padding:30px;">
                     <h4 style="font-family:'Rubik',sans-serif; font-size:24px; font-weight:600; margin-bottom:15px; color:#111827;">E-Commerce Automation Ecosystem</h4>
                     <p style="color:#4b5563; font-family:'Rubik',sans-serif; font-size:16px; margin:0;">Reduced manual data entry by 100% and increased fulfillment speed by 3x.</p>
                  </div>
               </div>
            </div>
            <div class="col-md-6 mb-4 wow fadeInUp" data-wow-delay="0.4s">
               <div style="background:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 10px 15px -3px rgba(0,0,0,0.1);">
                  <img src="img/case-study-2.webp" alt="Case Study 2" style="width:100%; height:250px; object-fit:cover;">
                  <div style="padding:30px;">
                     <h4 style="font-family:'Rubik',sans-serif; font-size:24px; font-weight:600; margin-bottom:15px; color:#111827;">AI Customer Support Agent</h4>
                     <p style="color:#4b5563; font-family:'Rubik',sans-serif; font-size:16px; margin:0;">Automated 70% of inbound queries while maintaining a 98% CSAT score.</p>
                  </div>
               </div>
            </div>
         </div>
         
         <a href="case-studies.html" class="fv-dual-btn wow fadeInUp" data-wow-delay="0.5s" style="display:inline-flex;">
            <span class="fv-btn-pill">EXPLORE CASE STUDIES</span>
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
    "Tell us where your team is losing time, dealing with repetitive work or struggling with disconnected systems."
)

# Convert strings using codecs so we don't blow up regex
about_content = re.sub(r'<!-- PAGE HERO -->.*<!-- FOOTER -->', new_content + '\n   <!-- FOOTER -->', about_html, flags=re.DOTALL)

# Explicitly use utf-8 encoding to write
with open('about.html', 'wb') as f:
    f.write(about_content.encode('utf-8'))

print("about.html visual content completely rewritten and injected.")
