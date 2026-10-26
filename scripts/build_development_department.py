import re
import os

dev_html = '''    <div id="development" class="dev-department-wrapper" style="scroll-margin-top: 70px; background-color: #ffffff; border-bottom: 1px solid #f3f4f6;">
      
      <!-- =================================================================
           DEVELOPMENT DEPARTMENT STYLES (SORA TYPOGRAPHY & TECHTOX DESIGN)
      ================================================================== -->
      <style>
        .dev-dept-hero {
          background: linear-gradient(180deg, #f9fafb 0%, #ffffff 100%);
          border-bottom: 1px solid #e5e7eb;
          padding: 80px 0 70px;
        }
        .dev-eyebrow {
          color: #FF2E3E;
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          font-weight: 700;
          letter-spacing: 2px;
          text-transform: uppercase;
          margin-bottom: 14px;
          display: inline-block;
        }
        .dev-badge-pill {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          border-radius: 9999px;
          background-color: #000000;
          color: #ffffff;
          padding: 6px 16px;
          font-size: 12px;
          font-weight: 600;
          font-family: 'Sora', sans-serif !important;
          letter-spacing: 1px;
          text-transform: uppercase;
          margin-bottom: 16px;
        }
        .dev-heading {
          font-family: 'Sora', sans-serif !important;
          font-size: 46px;
          font-weight: 700;
          color: #000000;
          letter-spacing: -1.5px;
          line-height: 1.15;
          margin-bottom: 18px;
        }
        .dev-lead {
          font-family: 'Sora', sans-serif !important;
          color: #4b5563;
          font-size: 18px;
          line-height: 1.65;
          margin: 0;
          letter-spacing: -0.2px;
        }
        .dev-trust-list {
          display: flex;
          flex-wrap: wrap;
          gap: 24px;
          margin-top: 28px;
          padding: 0;
          list-style: none;
        }
        .dev-trust-item {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          font-weight: 600;
          color: #1f2937;
        }
        .dev-trust-item i {
          color: #FF2E3E;
          font-size: 15px;
        }
        
        /* Modern App Mockup Preview */
        .dev-hero-mockup {
          background: #0b0f17;
          border-radius: 14px;
          border: 1px solid rgba(255, 255, 255, 0.12);
          box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
          overflow: hidden;
          transition: transform 0.3s ease;
        }
        .dev-hero-mockup:hover {
          transform: translateY(-4px);
        }
        .dev-mockup-bar {
          background: #111827;
          padding: 12px 18px;
          display: flex;
          align-items: center;
          gap: 8px;
          border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .dev-mockup-dot {
          width: 10px;
          height: 10px;
          border-radius: 50%;
          display: inline-block;
        }
        .dev-mockup-body {
          padding: 24px;
          color: #e5e7eb;
          font-family: 'Sora', sans-serif !important;
        }

        /* 02 - Problem Grid */
        .dev-problem-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 24px;
        }
        @media (min-width: 768px) {
          .dev-problem-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-problem-grid { grid-template-columns: repeat(4, 1fr); }
        }
        .dev-problem-card {
          background: #ffffff;
          border: 1px solid #fee2e2;
          border-radius: 12px;
          padding: 30px 24px;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
          transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
          display: flex;
          flex-direction: column;
        }
        .dev-problem-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 14px 28px -4px rgba(239, 68, 68, 0.12);
        }
        .dev-problem-badge {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          background: #fef2f2;
          color: #ef4444;
          font-family: 'Sora', sans-serif !important;
          font-size: 11px;
          font-weight: 700;
          padding: 4px 10px;
          border-radius: 6px;
          margin-bottom: 16px;
          letter-spacing: 0.5px;
          text-transform: uppercase;
          width: fit-content;
        }
        .dev-problem-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 19px;
          font-weight: 700;
          color: #111827;
          margin-bottom: 12px;
          letter-spacing: -0.4px;
          line-height: 1.3;
        }
        .dev-problem-desc {
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          font-weight: 400;
          color: #6b7280;
          line-height: 1.6;
          margin: 0;
          letter-spacing: -0.2px;
        }

        /* 03 - Solution Box */
        .dev-solution-box {
          background: #000000;
          color: #ffffff;
          border-radius: 16px;
          padding: 56px 48px;
          border: 1px solid rgba(255, 255, 255, 0.1);
          position: relative;
          overflow: hidden;
        }
        .dev-solution-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 36px;
          font-weight: 700;
          color: #ffffff;
          letter-spacing: -1px;
          margin-bottom: 16px;
          line-height: 1.2;
        }
        .dev-solution-desc {
          font-family: 'Sora', sans-serif !important;
          font-size: 17px;
          font-weight: 300;
          color: #d1d5db;
          line-height: 1.7;
          max-width: 820px;
          margin: 0 0 36px 0;
          letter-spacing: -0.2px;
        }
        .dev-capability-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 20px;
        }
        @media (min-width: 768px) {
          .dev-capability-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-capability-grid { grid-template-columns: repeat(4, 1fr); }
        }
        .dev-capability-item {
          background: rgba(255, 255, 255, 0.05);
          border: 1px solid rgba(255, 255, 255, 0.1);
          border-radius: 10px;
          padding: 22px 20px;
          transition: background 0.25s ease, border-color 0.25s ease;
        }
        .dev-capability-item:hover {
          background: rgba(255, 255, 255, 0.09);
          border-color: rgba(255, 46, 62, 0.4);
        }
        .dev-capability-item i {
          color: #FF2E3E;
          font-size: 20px;
          margin-bottom: 12px;
          display: block;
        }
        .dev-capability-item p {
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          font-weight: 500;
          color: #f3f4f6;
          line-height: 1.55;
          margin: 0;
          letter-spacing: -0.2px;
        }

        /* 04 - Services Cards Grid */
        .dev-services-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 32px;
        }
        @media (min-width: 768px) {
          .dev-services-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-services-grid { grid-template-columns: repeat(3, 1fr); gap: 40px 30px; }
        }
        .dev-service-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 14px;
          overflow: hidden;
          display: flex;
          flex-direction: column;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
          transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.25s ease;
          text-decoration: none !important;
        }
        .dev-service-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 16px 32px -4px rgba(0, 0, 0, 0.1);
          border-color: #cbd5e1;
        }
        .dev-service-img-wrap {
          aspect-ratio: 16/10;
          background-color: #f8fafc;
          overflow: hidden;
          position: relative;
        }
        .dev-service-img-wrap img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          display: block;
          transition: transform 0.4s ease;
        }
        .dev-service-card:hover .dev-service-img-wrap img {
          transform: scale(1.05);
        }
        .dev-service-body {
          padding: 28px 24px;
          display: flex;
          flex-direction: column;
          flex: 1;
        }
        .dev-service-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 21px;
          font-weight: 700;
          color: #000000;
          margin: 0 0 10px 0;
          letter-spacing: -0.5px;
          transition: color 0.2s ease;
        }
        .dev-service-card:hover .dev-service-title {
          color: #FF2E3E;
        }
        .dev-service-desc {
          font-family: 'Sora', sans-serif !important;
          color: #6b7280;
          font-size: 14px;
          line-height: 1.6;
          margin: 0 0 16px 0;
          letter-spacing: -0.2px;
        }
        .dev-deliverables-list {
          list-style: none;
          padding: 0;
          margin: 0 0 20px 0;
          display: flex;
          flex-direction: column;
          gap: 8px;
        }
        .dev-deliverables-list li {
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          color: #4b5563;
          display: flex;
          align-items: flex-start;
          gap: 8px;
          line-height: 1.45;
          letter-spacing: -0.2px;
        }
        .dev-deliverables-list li i {
          color: #FF2E3E;
          font-size: 11px;
          margin-top: 3px;
          flex-shrink: 0;
        }
        .dev-service-link {
          margin-top: auto;
          padding-top: 14px;
          border-top: 1px solid #f3f4f6;
          display: inline-flex;
          align-items: center;
          gap: 8px;
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          font-weight: 700;
          color: #FF2E3E;
          transition: gap 0.2s ease;
        }
        .dev-service-card:hover .dev-service-link {
          gap: 12px;
        }

        /* 05 - Project Showcase Grid */
        .dev-showcase-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 28px;
        }
        @media (min-width: 768px) {
          .dev-showcase-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-showcase-grid { grid-template-columns: repeat(3, 1fr); }
        }
        .dev-showcase-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 12px;
          overflow: hidden;
          display: flex;
          flex-direction: column;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
          transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
        }
        .dev-showcase-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 14px 28px -4px rgba(0, 0, 0, 0.09);
        }
        .dev-showcase-img-wrap {
          aspect-ratio: 16/10;
          background: #f3f4f6;
          overflow: hidden;
          position: relative;
        }
        .dev-showcase-img-wrap img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.4s ease;
        }
        .dev-showcase-card:hover .dev-showcase-img-wrap img {
          transform: scale(1.05);
        }
        .dev-showcase-badge {
          position: absolute;
          top: 14px;
          left: 14px;
          background: rgba(0, 0, 0, 0.82);
          color: #ffffff;
          backdrop-filter: blur(4px);
          padding: 4px 10px;
          border-radius: 6px;
          font-family: 'Sora', sans-serif !important;
          font-size: 11px;
          font-weight: 600;
          letter-spacing: 0.5px;
          text-transform: uppercase;
        }
        .dev-showcase-body {
          padding: 24px;
          display: flex;
          flex-direction: column;
          gap: 12px;
          flex: 1;
        }
        .dev-showcase-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 18px;
          font-weight: 700;
          color: #111827;
          margin: 0;
          letter-spacing: -0.4px;
        }
        .dev-showcase-meta {
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          line-height: 1.55;
          color: #4b5563;
          letter-spacing: -0.2px;
        }
        .dev-showcase-label {
          font-weight: 700;
          color: #111827;
          display: inline-block;
          margin-right: 4px;
        }

        /* 06 - Video Demonstration Area */
        .dev-video-card {
          border-radius: 16px;
          overflow: hidden;
          background: #000000;
          border: 1px solid rgba(255, 255, 255, 0.12);
          box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
          position: relative;
        }
        .dev-video-inner {
          aspect-ratio: 16/9;
          min-height: 420px;
          background-size: cover;
          background-position: center;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 40px 20px;
          position: relative;
        }
        .dev-video-pulse {
          width: 84px;
          height: 84px;
          border-radius: 50%;
          background: #FF2E3E;
          display: flex;
          align-items: center;
          justify-content: center;
          box-shadow: 0 0 0 14px rgba(255, 46, 62, 0.25), 0 12px 30px rgba(255, 46, 62, 0.45);
          transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
          cursor: pointer;
          margin: 0 auto 20px auto;
        }
        .dev-video-card:hover .dev-video-pulse {
          transform: scale(1.1);
          box-shadow: 0 0 0 22px rgba(255, 46, 62, 0.35), 0 16px 36px rgba(255, 46, 62, 0.55);
        }
        .dev-video-admin-bar {
          background: #0b0f17;
          border-top: 1px solid rgba(255, 255, 255, 0.08);
          padding: 14px 24px;
          display: flex;
          align-items: center;
          justify-content: space-between;
          flex-wrap: wrap;
          gap: 12px;
        }

        /* 07 - Workflow Grid (8 Steps) */
        .dev-workflow-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 20px;
        }
        @media (min-width: 768px) {
          .dev-workflow-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-workflow-grid { grid-template-columns: repeat(4, 1fr); }
        }
        .dev-workflow-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 12px;
          padding: 28px 22px;
          display: flex;
          flex-direction: column;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
          transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
          position: relative;
        }
        .dev-workflow-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 12px 24px -2px rgba(0, 0, 0, 0.08);
          border-color: #cbd5e1;
        }
        .dev-workflow-num {
          font-family: 'Sora', sans-serif !important;
          font-size: 32px;
          font-weight: 800;
          color: #FF2E3E;
          line-height: 1;
          margin-bottom: 12px;
          letter-spacing: -1px;
        }
        .dev-workflow-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 17px;
          font-weight: 700;
          color: #111827;
          margin-bottom: 8px;
          letter-spacing: -0.4px;
        }
        .dev-workflow-desc {
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          font-weight: 400;
          color: #6b7280;
          line-height: 1.5;
          margin-bottom: 14px;
          letter-spacing: -0.2px;
        }
        .dev-workflow-activities {
          list-style: none;
          padding: 0;
          margin: 0 0 16px 0;
          display: flex;
          flex-direction: column;
          gap: 6px;
        }
        .dev-workflow-activities li {
          font-family: 'Sora', sans-serif !important;
          font-size: 12px;
          color: #4b5563;
          display: flex;
          align-items: center;
          gap: 6px;
          letter-spacing: -0.2px;
        }
        .dev-workflow-deliverable {
          margin-top: auto;
          background: #f9fafb;
          border: 1px solid #e5e7eb;
          border-radius: 8px;
          padding: 10px 12px;
          font-family: 'Sora', sans-serif !important;
          font-size: 12px;
          font-weight: 600;
          color: #1f2937;
          letter-spacing: -0.2px;
        }

        /* 08 - Tech Stack Groups */
        .dev-tech-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 24px;
        }
        @media (min-width: 768px) {
          .dev-tech-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-tech-grid { grid-template-columns: repeat(3, 1fr); }
        }
        .dev-tech-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 12px;
          padding: 30px 26px;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
          transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .dev-tech-card:hover {
          transform: translateY(-3px);
          box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.06);
        }
        .dev-tech-header {
          display: flex;
          align-items: center;
          gap: 12px;
          margin-bottom: 14px;
        }
        .dev-tech-icon {
          width: 42px;
          height: 42px;
          border-radius: 8px;
          background: #fef2f2;
          color: #FF2E3E;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 18px;
        }
        .dev-tech-group-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 18px;
          font-weight: 700;
          color: #111827;
          margin: 0;
          letter-spacing: -0.4px;
        }
        .dev-pills-wrap {
          display: flex;
          flex-wrap: wrap;
          gap: 8px;
          margin-top: 14px;
        }
        .dev-tech-pill {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          padding: 6px 14px;
          border-radius: 9999px;
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          font-weight: 600;
          background: #f3f4f6;
          color: #374151;
          border: 1px solid #e5e7eb;
          letter-spacing: -0.2px;
          transition: background 0.2s ease, border-color 0.2s ease;
        }
        .dev-tech-pill:hover {
          background: #fef2f2;
          color: #991b1b;
          border-color: #fecaca;
        }

        /* 09 - Included in Scope Grid */
        .dev-scope-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 20px;
        }
        @media (min-width: 768px) {
          .dev-scope-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-scope-grid { grid-template-columns: repeat(4, 1fr); }
        }
        .dev-scope-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 12px;
          padding: 26px 20px;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
          transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .dev-scope-card:hover {
          transform: translateY(-3px);
          box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.07);
        }
        .dev-scope-icon {
          font-size: 22px;
          color: #FF2E3E;
          margin-bottom: 12px;
        }
        .dev-scope-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 16px;
          font-weight: 700;
          color: #111827;
          margin-bottom: 8px;
          letter-spacing: -0.3px;
        }
        .dev-scope-desc {
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          color: #6b7280;
          line-height: 1.55;
          margin: 0;
          letter-spacing: -0.2px;
        }

        /* 10 - Packages Cards */
        .dev-packages-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 28px;
        }
        @media (min-width: 992px) {
          .dev-packages-grid { grid-template-columns: repeat(3, 1fr); }
        }
        .dev-package-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 16px;
          padding: 40px 32px;
          display: flex;
          flex-direction: column;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
          transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.25s ease;
          position: relative;
        }
        .dev-package-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 16px 32px -4px rgba(0, 0, 0, 0.1);
        }
        .dev-package-card.popular {
          border: 2px solid #FF2E3E;
          background: linear-gradient(180deg, #ffffff 0%, #fffcfc 100%);
        }
        .dev-package-badge {
          position: absolute;
          top: -14px;
          left: 50%;
          transform: translateX(-50%);
          background: #FF2E3E;
          color: #ffffff;
          padding: 4px 14px;
          border-radius: 9999px;
          font-family: 'Sora', sans-serif !important;
          font-size: 12px;
          font-weight: 700;
          letter-spacing: 1px;
          text-transform: uppercase;
        }
        .dev-package-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 24px;
          font-weight: 700;
          color: #111827;
          margin-bottom: 8px;
          letter-spacing: -0.5px;
        }
        .dev-package-desc {
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          color: #6b7280;
          line-height: 1.6;
          margin-bottom: 24px;
        }
        .dev-package-features {
          list-style: none;
          padding: 0;
          margin: 0 0 32px 0;
          display: flex;
          flex-direction: column;
          gap: 12px;
          flex: 1;
        }
        .dev-package-features li {
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          color: #4b5563;
          display: flex;
          align-items: flex-start;
          gap: 10px;
          line-height: 1.5;
        }
        .dev-package-features li i {
          color: #FF2E3E;
          font-size: 13px;
          margin-top: 3px;
        }

        /* 11 - Client Journey */
        .dev-journey-grid {
          display: grid;
          grid-template-columns: 1fr;
          gap: 18px;
        }
        @media (min-width: 768px) {
          .dev-journey-grid { grid-template-columns: repeat(3, 1fr); }
        }
        @media (min-width: 1024px) {
          .dev-journey-grid { grid-template-columns: repeat(5, 1fr); }
        }
        .dev-journey-card {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 12px;
          padding: 24px 18px;
          transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .dev-journey-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 10px 20px -2px rgba(0, 0, 0, 0.07);
        }
        .dev-journey-step {
          font-family: 'Sora', sans-serif !important;
          font-size: 26px;
          font-weight: 800;
          color: #FF2E3E;
          margin-bottom: 8px;
          letter-spacing: -1px;
        }
        .dev-journey-title {
          font-family: 'Sora', sans-serif !important;
          font-size: 15px;
          font-weight: 700;
          color: #111827;
          margin-bottom: 8px;
          letter-spacing: -0.3px;
        }
        .dev-journey-desc {
          font-family: 'Sora', sans-serif !important;
          font-size: 13px;
          color: #6b7280;
          line-height: 1.5;
          margin: 0;
          letter-spacing: -0.2px;
        }

        /* 12 - Development FAQ Accordion */
        .dev-faq-container {
          max-width: 860px;
          margin: 0 auto;
        }
        .dev-faq-item {
          background: #ffffff;
          border: 1px solid #e5e7eb;
          border-radius: 10px;
          margin-bottom: 12px;
          transition: border-color 0.25s ease, box-shadow 0.25s ease;
          overflow: hidden;
        }
        .dev-faq-item.active {
          border-color: #FF2E3E;
          box-shadow: 0 4px 12px -2px rgba(255, 46, 62, 0.08);
        }
        .dev-faq-header {
          padding: 20px 24px;
          display: flex;
          align-items: center;
          justify-content: space-between;
          cursor: pointer;
          user-select: none;
        }
        .dev-faq-header h3 {
          font-family: 'Sora', sans-serif !important;
          font-size: 17px;
          font-weight: 600;
          color: #111827;
          margin: 0;
          letter-spacing: -0.3px;
          transition: color 0.25s ease;
        }
        .dev-faq-item.active .dev-faq-header h3 {
          color: #FF2E3E;
        }
        .dev-faq-icon {
          font-size: 15px;
          color: #9ca3af;
          transition: transform 0.3s ease, color 0.3s ease;
        }
        .dev-faq-item.active .dev-faq-icon {
          transform: rotate(180deg);
          color: #FF2E3E;
        }
        .dev-faq-body {
          max-height: 0;
          overflow: hidden;
          transition: max-height 0.35s ease-out, padding 0.35s ease-out;
          padding: 0 24px;
        }
        .dev-faq-item.active .dev-faq-body {
          max-height: 500px;
          padding: 0 24px 22px 24px;
        }
        .dev-faq-body p {
          font-family: 'Sora', sans-serif !important;
          font-size: 14px;
          color: #4b5563;
          line-height: 1.65;
          margin: 0;
          letter-spacing: -0.2px;
        }

        /* 13 - Final CTA Split */
        .dev-final-cta-box {
          background: #000000;
          border-radius: 20px;
          overflow: hidden;
          position: relative;
          border: 1px solid rgba(255, 255, 255, 0.12);
        }
      </style>

      <!-- =================================================================
           01 — DEVELOPMENT DEPARTMENT HERO SECTION
      ================================================================== -->
      <section class="dev-dept-hero">
        <div class="container">
          <div class="row align-items-center">
            
            <div class="col-lg-7 mb-5 mb-lg-0 pr-lg-5 wow fadeInLeft" data-wow-delay="0.1s">
              <div class="dev-badge-pill">
                <i class="fa fa-code" style="color: #FF2E3E;"></i> Phase 02 &mdash; Department
              </div>
              <span class="dev-eyebrow d-block">SOFTWARE DEVELOPMENT &amp; DIGITAL SOLUTIONS</span>
              <h2 class="dev-heading">We Design, Build &amp; Deliver Digital Products That Work.</h2>
              <p class="dev-lead">
                Techtox transforms business ideas into reliable digital solutions, from custom web applications and business websites to e-commerce platforms, desktop software, and integrated systems. We focus on practical functionality, clean user experiences, maintainable code, and solutions designed around real business requirements.
              </p>
              
              <div class="d-flex align-items-center flex-wrap gap-3 mt-4 pt-2" style="gap: 16px;">
                <a href="contact.html" class="fv-dual-btn">
                  <span class="fv-btn-pill">DISCUSS YOUR PROJECT</span>
                  <div class="fv-btn-circle">
                    <i class="fa fa-arrow-right arrow-main"></i>
                    <i class="fa fa-arrow-right arrow-hover"></i>
                  </div>
                </a>
                
                <a href="#dev-video-demo" class="popup-youtube vibe-btn-demo" id="dev-hero-video-link" style="text-decoration: none;">
                  <span class="vibe-play-circle"><i class="fa fa-play"></i></span>
                  <span style="font-family: 'Sora', sans-serif !important; font-weight: 600;">Watch Development Walkthrough</span>
                </a>
              </div>

              <!-- Trust Indicators -->
              <ul class="dev-trust-list">
                <li class="dev-trust-item"><i class="fa fa-check-circle"></i> Custom-Built Solutions</li>
                <li class="dev-trust-item"><i class="fa fa-check-circle"></i> Responsive User Experiences</li>
                <li class="dev-trust-item"><i class="fa fa-check-circle"></i> Structured Development Process</li>
                <li class="dev-trust-item"><i class="fa fa-check-circle"></i> Ongoing Technical Support</li>
              </ul>
            </div>

            <!-- Hero Mockup Visual -->
            <div class="col-lg-5 wow fadeInRight" data-wow-delay="0.2s">
              <div class="dev-hero-mockup">
                <div class="dev-mockup-bar">
                  <span class="dev-mockup-dot" style="background: #ef4444;"></span>
                  <span class="dev-mockup-dot" style="background: #f59e0b;"></span>
                  <span class="dev-mockup-dot" style="background: #10b981;"></span>
                  <span style="color: #9ca3af; font-size: 11px; margin-left: 12px; font-family: monospace;">techtox-platform.app/dashboard</span>
                </div>
                <div class="dev-mockup-body">
                  <div class="d-flex justify-content-between align-items-center mb-3">
                    <div>
                      <span style="font-size: 11px; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;">Core Engine</span>
                      <h4 style="color: #ffffff; font-size: 18px; margin: 2px 0 0 0; font-weight: 700;">Operational Portal</h4>
                    </div>
                    <span style="background: rgba(16, 185, 129, 0.2); color: #34d399; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 9999px;">
                      <i class="fa fa-circle" style="font-size: 7px; margin-right: 4px;"></i> Production Live
                    </span>
                  </div>
                  
                  <div style="background: #161f2e; border-radius: 8px; padding: 14px; margin-bottom: 14px; border: 1px solid rgba(255, 255, 255, 0.06); font-family: 'Fira Code', monospace; font-size: 12px; color: #93c5fd;">
                    <span style="color: #f472b6;">const</span> app = <span style="color: #60a5fa;">createEnterpriseApp</span>({<br/>
                    &nbsp;&nbsp;architecture: <span style="color: #34d399;">"Clean &amp; Modular"</span>,<br/>
                    &nbsp;&nbsp;security: <span style="color: #34d399;">"RoleBasedAuth"</span>,<br/>
                    &nbsp;&nbsp;performance: <span style="color: #fbbf24;">"SubSecondSSR"</span><br/>
                    });
                  </div>

                  <div class="row" style="margin: 0 -6px;">
                    <div class="col-6" style="padding: 0 6px;">
                      <div style="background: #111827; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 12px;">
                        <span style="font-size: 11px; color: #9ca3af;">API Health</span>
                        <div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-top: 2px;">99.98%</div>
                      </div>
                    </div>
                    <div class="col-6" style="padding: 0 6px;">
                      <div style="background: #111827; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 12px;">
                        <span style="font-size: 11px; color: #9ca3af;">Response Time</span>
                        <div style="font-size: 18px; font-weight: 700; color: #FF2E3E; margin-top: 2px;">&lt;180ms</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           02 — THE DEVELOPMENT CHALLENGE (OPERATIONAL FRICTION)
      ================================================================== -->
      <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">THE DEVELOPMENT CHALLENGE</span>
            <h2 class="vibe-heading" style="font-size: 40px;">What Is Holding Your Business Back?</h2>
            <p class="vibe-lead">Common operational bottlenecks and technical hurdles businesses experience before investing in purpose-built software.</p>
          </div>
          
          <div class="dev-problem-grid">
            
            <!-- Problem Card 1 -->
            <div class="dev-problem-card wow fadeInUp" data-wow-delay="0.1s">
              <span class="dev-problem-badge"><i class="fal fa-layer-group"></i> Operational Friction</span>
              <h3 class="dev-problem-title">Fragmented Business Processes</h3>
              <p class="dev-problem-desc">Teams rely on spreadsheets, disconnected applications, and manual work because their systems do not communicate effectively.</p>
            </div>

            <!-- Problem Card 2 -->
            <div class="dev-problem-card wow fadeInUp" data-wow-delay="0.2s">
              <span class="dev-problem-badge"><i class="fal fa-browser"></i> User Experience Gap</span>
              <h3 class="dev-problem-title">Outdated Websites &amp; Digital Experiences</h3>
              <p class="dev-problem-desc">Slow, difficult-to-use, or outdated websites can damage credibility, frustrate customers, and reduce conversions.</p>
            </div>

            <!-- Problem Card 3 -->
            <div class="dev-problem-card wow fadeInUp" data-wow-delay="0.3s">
              <span class="dev-problem-badge"><i class="fal fa-puzzle-piece"></i> Architectural Mismatch</span>
              <h3 class="dev-problem-title">Software That Does Not Fit the Business</h3>
              <p class="dev-problem-desc">Off-the-shelf tools may not support specific workflows, business rules, reporting needs, or operational requirements.</p>
            </div>

            <!-- Problem Card 4 -->
            <div class="dev-problem-card wow fadeInUp" data-wow-delay="0.4s">
              <span class="dev-problem-badge"><i class="fal fa-database"></i> Data Isolation</span>
              <h3 class="dev-problem-title">Disconnected Platforms and Data</h3>
              <p class="dev-problem-desc">Customer information, orders, records, and internal processes become difficult to manage when applications operate in isolation.</p>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           03 — THE ENGINEERED SOLUTION SECTION
      ================================================================== -->
      <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
        <div class="container">
          <div class="dev-solution-box wow fadeInUp" data-wow-delay="0.1s">
            <span class="dev-eyebrow">THE ENGINEERED SOLUTION</span>
            <h2 class="dev-solution-title">Software Designed Around Your Business</h2>
            <p class="dev-solution-desc">
              We build digital products around your requirements, users, and operational goals. From planning and interface design to implementation, testing, deployment, and ongoing improvement, Techtox follows a structured approach to deliver software that is practical, reliable, and maintainable.
            </p>

            <div class="dev-capability-grid">
              <div class="dev-capability-item">
                <i class="fal fa-bullseye-arrow"></i>
                <p>Purpose-built functionality aligned with business requirements.</p>
              </div>
              <div class="dev-capability-item">
                <i class="fal fa-sparkles"></i>
                <p>Responsive and intuitive user interfaces.</p>
              </div>
              <div class="dev-capability-item">
                <i class="fal fa-shield-check"></i>
                <p>Secure, maintainable application architecture appropriate to the project.</p>
              </div>
              <div class="dev-capability-item">
                <i class="fal fa-plug"></i>
                <p>Integration with relevant databases, APIs, and third-party services.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- =================================================================
           04 — MAIN DEVELOPMENT SERVICES SECTION (6 SERVICES)
      ================================================================== -->
      <section class="py-5" id="dev-services" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">WHAT WE BUILD</span>
            <h2 class="vibe-heading" style="font-size: 40px;">Development Services Built for Real-World Needs</h2>
            <p class="vibe-lead">Explore the digital solutions Techtox can design, develop, integrate, and maintain for your business.</p>
          </div>

          <div class="dev-services-grid">

            <!-- Service 1 — Custom Web Applications -->
            <a href="services/web-applications.html" class="dev-service-card wow fadeInUp" data-wow-delay="0.1s">
              <div class="dev-service-img-wrap">
                <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80" alt="Custom Web Applications" loading="lazy">
              </div>
              <div class="dev-service-body">
                <h3 class="dev-service-title">Custom Web Applications</h3>
                <p class="dev-service-desc">We develop custom web applications that help businesses manage operations, organize information, serve customers, and streamline complex workflows through purpose-built digital tools.</p>
                <ul class="dev-deliverables-list">
                  <li><i class="fa fa-check"></i> Business management systems &amp; admin dashboards</li>
                  <li><i class="fa fa-check"></i> Customer &amp; employee portals with role-based access</li>
                  <li><i class="fa fa-check"></i> Booking, inventory &amp; operational record tools</li>
                  <li><i class="fa fa-check"></i> Database-backed architectures (React, ASP.NET Core)</li>
                </ul>
                <div class="dev-service-link">
                  <span>Explore Web Applications</span> <i class="fa fa-arrow-right"></i>
                </div>
              </div>
            </a>

            <!-- Service 2 — WordPress Development -->
            <a href="services/wordpress-solutions.html" class="dev-service-card wow fadeInUp" data-wow-delay="0.2s">
              <div class="dev-service-img-wrap">
                <img src="https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=800&q=80" alt="WordPress Development" loading="lazy">
              </div>
              <div class="dev-service-body">
                <h3 class="dev-service-title">WordPress Development</h3>
                <p class="dev-service-desc">We build and customize WordPress websites that help businesses establish their online presence and manage content without unnecessary complexity.</p>
                <ul class="dev-deliverables-list">
                  <li><i class="fa fa-check"></i> Corporate websites, landing pages &amp; portfolios</li>
                  <li><i class="fa fa-check"></i> Custom theme development &amp; modular block styling</li>
                  <li><i class="fa fa-check"></i> Plugin configuration &amp; bespoke functionality</li>
                  <li><i class="fa fa-check"></i> Performance optimization, migrations &amp; maintenance</li>
                </ul>
                <div class="dev-service-link">
                  <span>Explore WordPress Solutions</span> <i class="fa fa-arrow-right"></i>
                </div>
              </div>
            </a>

            <!-- Service 3 — Shopify & E-commerce Development -->
            <a href="services/shopify-stores.html" class="dev-service-card wow fadeInUp" data-wow-delay="0.3s">
              <div class="dev-service-img-wrap">
                <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80" alt="Shopify & E-commerce Development" loading="lazy">
              </div>
              <div class="dev-service-body">
                <h3 class="dev-service-title">Shopify &amp; E-commerce Development</h3>
                <p class="dev-service-desc">We create and improve e-commerce experiences that help businesses showcase products, manage online stores, and provide customers with a smooth purchasing journey.</p>
                <ul class="dev-deliverables-list">
                  <li><i class="fa fa-check"></i> Shopify &amp; WooCommerce storefront setup &amp; theme design</li>
                  <li><i class="fa fa-check"></i> Product catalog, collection &amp; inventory structuring</li>
                  <li><i class="fa fa-check"></i> Cart, checkout &amp; secure payment gateway integrations</li>
                  <li><i class="fa fa-check"></i> Storefront optimization, speed audits &amp; enhancements</li>
                </ul>
                <div class="dev-service-link">
                  <span>Explore E-commerce Solutions</span> <i class="fa fa-arrow-right"></i>
                </div>
              </div>
            </a>

            <!-- Service 4 — Desktop Application Development -->
            <a href="services/desktop-applications.html" class="dev-service-card wow fadeInUp" data-wow-delay="0.4s">
              <div class="dev-service-img-wrap">
                <img src="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80" alt="Desktop Application Development" loading="lazy">
              </div>
              <div class="dev-service-body">
                <h3 class="dev-service-title">Desktop Application Development</h3>
                <p class="dev-service-desc">We develop desktop software for business workflows that require a dedicated application experience, structured data handling, or functionality tailored to specific operational needs.</p>
                <ul class="dev-deliverables-list">
                  <li><i class="fa fa-check"></i> Internal business utilities &amp; operational desktop tools</li>
                  <li><i class="fa fa-check"></i> High-volume data entry &amp; record processing tools</li>
                  <li><i class="fa fa-check"></i> Custom reporting &amp; analytics applications</li>
                  <li><i class="fa fa-check"></i> Desktop interfaces connected to secure APIs &amp; databases</li>
                </ul>
                <div class="dev-service-link">
                  <span>Discuss a Desktop Application</span> <i class="fa fa-arrow-right"></i>
                </div>
              </div>
            </a>

            <!-- Service 5 — API Development & System Integration -->
            <a href="services/api-software-integration.html" class="dev-service-card wow fadeInUp" data-wow-delay="0.5s">
              <div class="dev-service-img-wrap">
                <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="API Development & System Integration" loading="lazy">
              </div>
              <div class="dev-service-body">
                <h3 class="dev-service-title">API Development &amp; System Integration</h3>
                <p class="dev-service-desc">We connect applications, services, and databases so information can move between systems reliably and business processes can operate more efficiently.</p>
                <ul class="dev-deliverables-list">
                  <li><i class="fa fa-check"></i> REST API architecture, development &amp; documentation</li>
                  <li><i class="fa fa-check"></i> Third-party SaaS, CRM &amp; helpdesk service connections</li>
                  <li><i class="fa fa-check"></i> Database synchronization &amp; resilient webhook pipelines</li>
                  <li><i class="fa fa-check"></i> Payment gateways &amp; secure tokenized authentication</li>
                </ul>
                <div class="dev-service-link">
                  <span>Discuss an Integration Project</span> <i class="fa fa-arrow-right"></i>
                </div>
              </div>
            </a>

            <!-- Service 6 — Website Maintenance & Software Improvements -->
            <a href="contact.html" class="dev-service-card wow fadeInUp" data-wow-delay="0.6s">
              <div class="dev-service-img-wrap">
                <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80" alt="Website Maintenance & Software Improvements" loading="lazy">
              </div>
              <div class="dev-service-body">
                <h3 class="dev-service-title">Website Maintenance &amp; Improvements</h3>
                <p class="dev-service-desc">We help businesses maintain, improve, and extend existing digital products after launch with structured technical care and iterative improvements.</p>
                <ul class="dev-deliverables-list">
                  <li><i class="fa fa-check"></i> Bug fixing, troubleshooting &amp; technical health checks</li>
                  <li><i class="fa fa-check"></i> Performance tuning, caching &amp; database optimization</li>
                  <li><i class="fa fa-check"></i> Feature enhancements &amp; responsive UI updates</li>
                  <li><i class="fa fa-check"></i> Dependency updates, security audits &amp; ongoing support</li>
                </ul>
                <div class="dev-service-link">
                  <span>Request Technical Support</span> <i class="fa fa-arrow-right"></i>
                </div>
              </div>
            </a>

          </div>
        </div>
      </section>

      <!-- =================================================================
           05 — DEVELOPMENT PROJECT SHOWCASE SECTION
      ================================================================== -->
      <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">OUR DEVELOPMENT WORK</span>
            <h2 class="vibe-heading" style="font-size: 40px;">From Requirements to Working Software</h2>
            <p class="vibe-lead">Explore examples of the interfaces, workflows, and digital products we build to solve real business challenges.</p>
          </div>

          <div class="dev-showcase-grid">
            
            <!-- Showcase Item 1 -->
            <div class="dev-showcase-card wow fadeInUp" data-wow-delay="0.1s">
              <div class="dev-showcase-img-wrap">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80" alt="Custom Web Application Operations Dashboard" loading="lazy">
                <span class="dev-showcase-badge">Prototype Demonstration</span>
              </div>
              <div class="dev-showcase-body">
                <h3 class="dev-showcase-title">Operations &amp; Task Management Portal</h3>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Problem:</span>
                  <span>Operations teams struggled with scattered spreadsheets, missing client status records, and uncoordinated task delegation.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Built:</span>
                  <span>Role-based web portal featuring live Kanban boards, centralized activity tracking, and automated email notifications.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Technology:</span>
                  <span style="color: #FF2E3E; font-weight: 600;">React, TypeScript, ASP.NET Core, PostgreSQL</span>
                </div>
              </div>
            </div>

            <!-- Showcase Item 2 -->
            <div class="dev-showcase-card wow fadeInUp" data-wow-delay="0.2s">
              <div class="dev-showcase-img-wrap">
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80" alt="Corporate WordPress Website" loading="lazy">
                <span class="dev-showcase-badge">Client Build Showcase</span>
              </div>
              <div class="dev-showcase-body">
                <h3 class="dev-showcase-title">Corporate Services Website &amp; CMS</h3>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Problem:</span>
                  <span>Previous website was slow, non-responsive on mobile devices, and difficult for non-technical marketing staff to update.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Built:</span>
                  <span>Custom WordPress theme engineered with modular Gutenberg components, sub-second load times, and structured SEO schema.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Technology:</span>
                  <span style="color: #FF2E3E; font-weight: 600;">WordPress, Custom PHP/CSS, MySQL, Cloudflare</span>
                </div>
              </div>
            </div>

            <!-- Showcase Item 3 -->
            <div class="dev-showcase-card wow fadeInUp" data-wow-delay="0.3s">
              <div class="dev-showcase-img-wrap">
                <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80" alt="E-Commerce Storefront" loading="lazy">
                <span class="dev-showcase-badge">Client Store Showcase</span>
              </div>
              <div class="dev-showcase-body">
                <h3 class="dev-showcase-title">Specialized E-Commerce Storefront</h3>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Problem:</span>
                  <span>High cart abandonment on mobile due to cluttered navigation and a disjointed multi-step checkout journey.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Built:</span>
                  <span>Streamlined Shopify storefront with rapid variant selection, one-click cart drawer, and integrated payment gateways.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Technology:</span>
                  <span style="color: #FF2E3E; font-weight: 600;">Shopify Liquid, JavaScript, Stripe API</span>
                </div>
              </div>
            </div>

            <!-- Showcase Item 4 -->
            <div class="dev-showcase-card wow fadeInUp" data-wow-delay="0.4s">
              <div class="dev-showcase-img-wrap">
                <img src="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80" alt="Desktop Application Interface" loading="lazy">
                <span class="dev-showcase-badge">Prototype Demonstration</span>
              </div>
              <div class="dev-showcase-body">
                <h3 class="dev-showcase-title">High-Throughput Inventory Utility</h3>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Problem:</span>
                  <span>Warehouse operators needed dedicated, high-speed data processing capable of barcode scanning without browser latency.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Built:</span>
                  <span>Focused desktop utility with direct hardware scanner input, batch label creation, and real-time database sync.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Technology:</span>
                  <span style="color: #FF2E3E; font-weight: 600;">C#, .NET Desktop, SQL Server</span>
                </div>
              </div>
            </div>

            <!-- Showcase Item 5 -->
            <div class="dev-showcase-card wow fadeInUp" data-wow-delay="0.5s">
              <div class="dev-showcase-img-wrap">
                <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80" alt="API and Data Pipelines" loading="lazy">
                <span class="dev-showcase-badge">Integration Showcase</span>
              </div>
              <div class="dev-showcase-body">
                <h3 class="dev-showcase-title">Multi-Platform API Gateway</h3>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Problem:</span>
                  <span>Incoming sales orders required manual re-entry into internal billing software and third-party logistics systems daily.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Built:</span>
                  <span>Resilient REST API middleware engine that listens for order webhooks, transforms payloads, and logs confirmed deliveries.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Technology:</span>
                  <span style="color: #FF2E3E; font-weight: 600;">ASP.NET Core REST API, Webhooks, JSON</span>
                </div>
              </div>
            </div>

            <!-- Showcase Item 6 -->
            <div class="dev-showcase-card wow fadeInUp" data-wow-delay="0.6s">
              <div class="dev-showcase-img-wrap">
                <img src="https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=800&q=80" alt="Client Document Hub" loading="lazy">
                <span class="dev-showcase-badge">Client Solution Showcase</span>
              </div>
              <div class="dev-showcase-body">
                <h3 class="dev-showcase-title">Secure Customer Documentation Hub</h3>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Problem:</span>
                  <span>Corporate clients needed self-service access to historical invoices, project contracts, and deliverable archives.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Built:</span>
                  <span>Protected client portal featuring tokenized authentication, download logging, and integrated support ticket creation.</span>
                </div>
                <div class="dev-showcase-meta">
                  <span class="dev-showcase-label">Technology:</span>
                  <span style="color: #FF2E3E; font-weight: 600;">React, REST APIs, SQL Database, JWT Auth</span>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           06 — VIDEO DEMONSTRATION SECTION WITH UPLOADABLE / CONFIGURABLE VIDEO
      ================================================================== -->
      <section class="py-5" id="dev-video-demo" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">INSIDE THE BUILD</span>
            <h2 class="vibe-heading" style="font-size: 40px;">Watch the System in Action</h2>
            <p class="vibe-lead">See how a Techtox development solution works in practice. Our walkthroughs explain the system's purpose, user experience, key features, internal workflow, and how its components work together.</p>
          </div>

          <!-- Video Demo Card Component -->
          <div class="dev-video-card wow fadeInUp" data-wow-delay="0.15s">
            <div class="dev-video-inner" id="dev-video-inner-container" style="background-image: linear-gradient(rgba(11, 15, 23, 0.72), rgba(11, 15, 23, 0.88)), url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1920&q=80');">
              
              <!-- Video Play Link / Lightbox Trigger -->
              <a href="https://www.youtube.com/watch?v=LXb3EKWsInQ" class="popup-youtube text-center" id="dev-main-video-trigger" style="text-decoration: none; cursor: pointer; display: block; max-width: 650px;" target="_blank" rel="noopener noreferrer">
                <div class="dev-video-pulse">
                  <i class="fa fa-play" style="color: #ffffff; font-size: 26px; margin-left: 4px;"></i>
                </div>
                <div>
                  <span id="dev-video-title-display" style="display: block; color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 24px; font-weight: 700; letter-spacing: -0.5px; line-height: 1.3;">
                    How Our Software Development Process Works
                  </span>
                  <span id="dev-video-desc-display" style="display: block; color: #d1d5db; font-family: 'Sora', sans-serif !important; font-size: 15px; font-weight: 400; margin-top: 10px; line-height: 1.6;">
                    Watch a practical walkthrough of how a software project moves from business requirements and interface planning to development, testing, deployment, and ongoing support.
                  </span>
                  <span style="display: inline-flex; align-items: center; gap: 8px; color: #ffffff; background: rgba(255, 46, 62, 0.25); border: 1px solid rgba(255, 46, 62, 0.5); padding: 6px 16px; border-radius: 9999px; font-family: 'Sora', sans-serif !important; font-size: 13px; font-weight: 600; margin-top: 16px;">
                    <i class="fa fa-play-circle" style="color: #FF2E3E;"></i> Click to Play Video Walkthrough &bull; ~4 Mins
                  </span>
                </div>
              </a>

            </div>

            <!-- Admin Video Management Bar -->
            <div class="dev-video-admin-bar">
              <div class="d-flex align-items-center gap-3">
                <span style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #9ca3af;">
                  <i class="fal fa-film" style="color: #FF2E3E; margin-right: 6px;"></i> Source: <strong id="dev-video-source-label" style="color: #e5e7eb;">YouTube Walkthrough</strong>
                </span>
                <span style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #9ca3af;">
                  &bull; Stack: <strong style="color: #e5e7eb;">React, ASP.NET Core &amp; APIs</strong>
                </span>
              </div>
              <div class="d-flex align-items-center gap-2">
                <a href="contact.html" class="btn btn-sm" style="background: #FF2E3E; color: #ffffff; font-family: 'Sora', sans-serif !important; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 6px;">
                  Discuss a Similar Project
                </a>
                <button type="button" class="btn btn-sm btn-outline-secondary" id="dev-toggle-video-admin" style="font-family: 'Sora', sans-serif !important; font-size: 12px; color: #9ca3af; border-color: rgba(255,255,255,0.15);">
                  <i class="fal fa-cog"></i> Configure Video
                </button>
              </div>
            </div>

            <!-- Admin Video Drawer / Modal Form -->
            <div id="dev-video-config-drawer" style="display: none; background: #0f172a; padding: 24px; border-top: 1px solid rgba(255,255,255,0.12); color: #ffffff; font-family: 'Sora', sans-serif !important;">
              <div class="d-flex justify-content-between align-items-center mb-3">
                <h5 style="color: #ffffff; font-size: 16px; margin: 0; font-weight: 700;">
                  <i class="fal fa-sliders-h" style="color: #FF2E3E; margin-right: 8px;"></i> Administrator: Configure Video Source
                </h5>
                <button type="button" class="btn btn-sm btn-link text-white" id="dev-close-video-admin" style="padding: 0; text-decoration: none;">&times; Close</button>
              </div>
              <p style="font-size: 13px; color: #94a3b8; margin-bottom: 16px;">
                Authorized Techtox staff can replace the video walkthrough by pasting a direct MP4 URL or YouTube / Vimeo link below. Settings are applied dynamically and persisted in your browser.
              </p>
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label style="font-size: 12px; color: #cbd5e1; font-weight: 600; display: block; margin-bottom: 4px;">Video Walkthrough URL (MP4, YouTube, or Vimeo):</label>
                  <input type="text" id="dev-cfg-url" class="form-control form-control-sm" style="background: #1e293b; border-color: #334155; color: #ffffff;" placeholder="e.g. https://www.youtube.com/watch?v=LXb3EKWsInQ">
                </div>
                <div class="col-md-6 mb-3">
                  <label style="font-size: 12px; color: #cbd5e1; font-weight: 600; display: block; margin-bottom: 4px;">Custom Thumbnail / Poster URL (Optional):</label>
                  <input type="text" id="dev-cfg-poster" class="form-control form-control-sm" style="background: #1e293b; border-color: #334155; color: #ffffff;" placeholder="e.g. https://images.unsplash.com/photo-1498050108023-c5249f4df085">
                </div>
                <div class="col-md-6 mb-3">
                  <label style="font-size: 12px; color: #cbd5e1; font-weight: 600; display: block; margin-bottom: 4px;">Video Title:</label>
                  <input type="text" id="dev-cfg-title" class="form-control form-control-sm" style="background: #1e293b; border-color: #334155; color: #ffffff;" placeholder="How Our Software Development Process Works">
                </div>
                <div class="col-md-6 mb-3">
                  <label style="font-size: 12px; color: #cbd5e1; font-weight: 600; display: block; margin-bottom: 4px;">Video Description:</label>
                  <input type="text" id="dev-cfg-desc" class="form-control form-control-sm" style="background: #1e293b; border-color: #334155; color: #ffffff;" placeholder="Watch a practical walkthrough of our software development process.">
                </div>
              </div>
              <div class="d-flex gap-2 justify-content-end" style="gap: 10px;">
                <button type="button" class="btn btn-sm btn-outline-light" id="dev-cfg-reset-btn" style="font-size: 12px;">Reset to Default</button>
                <button type="button" class="btn btn-sm btn-danger" id="dev-cfg-save-btn" style="background: #FF2E3E; border-color: #FF2E3E; font-size: 12px; font-weight: 600;">Save &amp; Apply Video</button>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           07 — COMPLETE SOFTWARE DEVELOPMENT WORKFLOW (8 STEPS)
      ================================================================== -->
      <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">OPERATIONAL BLUEPRINT</span>
            <h2 class="vibe-heading" style="font-size: 40px;">Our End-to-End Software Development Workflow</h2>
            <p class="vibe-lead">Every successful software project begins with a clear understanding of the problem and follows a structured process through planning, development, testing, release, and continuous improvement.</p>
          </div>

          <div class="dev-workflow-grid">

            <!-- Step 01 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.05s">
              <div class="dev-workflow-num">01</div>
              <h3 class="dev-workflow-title">Discovery &amp; Requirements</h3>
              <p class="dev-workflow-desc">We learn about the business, its users, its current challenges, and the desired outcome.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Initial consultation &amp; goals</li>
                <li><i class="fa fa-angle-right text-danger"></i> Stakeholder &amp; user needs</li>
                <li><i class="fa fa-angle-right text-danger"></i> Feature priority identification</li>
                <li><i class="fa fa-angle-right text-danger"></i> Constraints &amp; risk criteria</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-file-alt text-danger mr-1"></i> Deliverable: Documented Project Brief
              </div>
            </div>

            <!-- Step 02 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.10s">
              <div class="dev-workflow-num">02</div>
              <h3 class="dev-workflow-title">Scope &amp; Estimation</h3>
              <p class="dev-workflow-desc">We turn the requirements into an actionable plan with clear boundaries and realistic expectations.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Included vs. excluded scope</li>
                <li><i class="fa fa-angle-right text-danger"></i> Milestones &amp; task breakdown</li>
                <li><i class="fa fa-angle-right text-danger"></i> Third-party dependencies</li>
                <li><i class="fa fa-angle-right text-danger"></i> Delivery timeline agreement</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-file-contract text-danger mr-1"></i> Deliverable: Scoped Proposal &amp; Plan
              </div>
            </div>

            <!-- Step 03 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.15s">
              <div class="dev-workflow-num">03</div>
              <h3 class="dev-workflow-title">UI/UX &amp; Architecture</h3>
              <p class="dev-workflow-desc">We plan the user experience and technical structure before implementing the solution.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> User flows &amp; wireframes</li>
                <li><i class="fa fa-angle-right text-danger"></i> Responsive layout planning</li>
                <li><i class="fa fa-angle-right text-danger"></i> Database &amp; API schema design</li>
                <li><i class="fa fa-angle-right text-danger"></i> Security &amp; auth planning</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-drafting-compass text-danger mr-1"></i> Deliverable: Approved Design &amp; Specs
              </div>
            </div>

            <!-- Step 04 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.20s">
              <div class="dev-workflow-num">04</div>
              <h3 class="dev-workflow-title">Development</h3>
              <p class="dev-workflow-desc">We implement the agreed functionality in manageable, milestone-based stages.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Frontend component builds</li>
                <li><i class="fa fa-angle-right text-danger"></i> Backend API &amp; business logic</li>
                <li><i class="fa fa-angle-right text-danger"></i> Database modeling &amp; setup</li>
                <li><i class="fa fa-angle-right text-danger"></i> Third-party API integrations</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-code-branch text-danger mr-1"></i> Deliverable: Working Product Build
              </div>
            </div>

            <!-- Step 05 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.25s">
              <div class="dev-workflow-num">05</div>
              <h3 class="dev-workflow-title">Testing &amp; QA</h3>
              <p class="dev-workflow-desc">We verify that the product behaves as expected before launch across browsers and devices.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Feature &amp; acceptance testing</li>
                <li><i class="fa fa-angle-right text-danger"></i> Responsive &amp; browser checks</li>
                <li><i class="fa fa-angle-right text-danger"></i> API validation &amp; edge cases</li>
                <li><i class="fa fa-angle-right text-danger"></i> Bug fixing &amp; regression runs</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-shield-check text-danger mr-1"></i> Deliverable: Tested Release Candidate
              </div>
            </div>

            <!-- Step 06 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.30s">
              <div class="dev-workflow-num">06</div>
              <h3 class="dev-workflow-title">Review &amp; Refinement</h3>
              <p class="dev-workflow-desc">We present the working solution and collect client feedback against agreed requirements.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Live walkthrough demonstration</li>
                <li><i class="fa fa-angle-right text-danger"></i> Requirements verification</li>
                <li><i class="fa fa-angle-right text-danger"></i> Structured client feedback</li>
                <li><i class="fa fa-angle-right text-danger"></i> Final polish &amp; sign-off</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-check-double text-danger mr-1"></i> Deliverable: Approved Final Release
              </div>
            </div>

            <!-- Step 07 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.35s">
              <div class="dev-workflow-num">07</div>
              <h3 class="dev-workflow-title">Deployment &amp; Handover</h3>
              <p class="dev-workflow-desc">We prepare the application for production use and transfer agreed code and documentation.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Production hosting setup</li>
                <li><i class="fa fa-angle-right text-danger"></i> Domain &amp; SSL configuration</li>
                <li><i class="fa fa-angle-right text-danger"></i> Database migration &amp; test</li>
                <li><i class="fa fa-angle-right text-danger"></i> Source code &amp; credentials handover</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-rocket text-danger mr-1"></i> Deliverable: Live System &amp; Handover Pack
              </div>
            </div>

            <!-- Step 08 -->
            <div class="dev-workflow-card wow fadeInUp" data-wow-delay="0.40s">
              <div class="dev-workflow-num">08</div>
              <h3 class="dev-workflow-title">Maintenance &amp; Care</h3>
              <p class="dev-workflow-desc">After launch, we help keep the software reliable and improve it as requirements evolve.</p>
              <ul class="dev-workflow-activities">
                <li><i class="fa fa-angle-right text-danger"></i> Bug fixes under support terms</li>
                <li><i class="fa fa-angle-right text-danger"></i> Security &amp; dependency patches</li>
                <li><i class="fa fa-angle-right text-danger"></i> Performance &amp; speed monitoring</li>
                <li><i class="fa fa-angle-right text-danger"></i> Iterative feature enhancements</li>
              </ul>
              <div class="dev-workflow-deliverable">
                <i class="fa fa-tools text-danger mr-1"></i> Deliverable: Ongoing Maintenance Plan
              </div>
            </div>

          </div>

          <!-- Bottom Workflow Banner CTA -->
          <div class="mt-5 p-4 rounded-3 d-flex flex-column flex-md-row justify-content-between align-items-center" style="background: #ffffff; border: 1px solid #e5e7eb; gap: 20px;">
            <div>
              <h4 style="font-family: 'Sora', sans-serif !important; font-size: 20px; font-weight: 700; color: #111827; margin: 0 0 4px 0;">Have a Project in Mind? Let's Plan It Together.</h4>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #6b7280; margin: 0;">We will review your requirements, recommend the best architecture, and prepare a clear project scope.</p>
            </div>
            <a href="contact.html" class="fv-dual-btn flex-shrink-0">
              <span class="fv-btn-pill">DISCUSS YOUR PROJECT</span>
              <div class="fv-btn-circle">
                <i class="fa fa-arrow-right arrow-main"></i>
                <i class="fa fa-arrow-right arrow-hover"></i>
              </div>
            </a>
          </div>

        </div>
      </section>

      <!-- =================================================================
           08 — TECHNOLOGY STACK SECTION
      ================================================================== -->
      <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">BUILT WITH THE RIGHT TOOLS</span>
            <h2 class="vibe-heading" style="font-size: 40px;">Technology Chosen for the Problem</h2>
            <p class="vibe-lead">We select technologies based on project requirements, maintainability, integration needs, performance expectations, and the capabilities needed to support the product over time.</p>
          </div>

          <div class="dev-tech-grid">

            <!-- Group 1: Frontend -->
            <div class="dev-tech-card wow fadeInUp" data-wow-delay="0.1s">
              <div class="dev-tech-header">
                <div class="dev-tech-icon"><i class="fal fa-browser"></i></div>
                <h3 class="dev-tech-group-title">Frontend Technologies</h3>
              </div>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">Modern, reactive client experiences built with clean architecture, responsive components, and accessible patterns.</p>
              <div class="dev-pills-wrap">
                <span class="dev-tech-pill"><i class="fab fa-react" style="color: #61dafb;"></i> React</span>
                <span class="dev-tech-pill"><i class="fab fa-js" style="color: #3178c6;"></i> TypeScript</span>
                <span class="dev-tech-pill"><i class="fab fa-html5" style="color: #e34f26;"></i> HTML5 &amp; CSS3</span>
                <span class="dev-tech-pill"><i class="fab fa-js" style="color: #f7df1e;"></i> JavaScript (ES6+)</span>
                <span class="dev-tech-pill"><i class="fal fa-mobile-android" style="color: #FF2E3E;"></i> Responsive UI</span>
              </div>
            </div>

            <!-- Group 2: Backend -->
            <div class="dev-tech-card wow fadeInUp" data-wow-delay="0.2s">
              <div class="dev-tech-header">
                <div class="dev-tech-icon"><i class="fal fa-server"></i></div>
                <h3 class="dev-tech-group-title">Backend Architecture</h3>
              </div>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">Robust, type-safe application backends engineered for business logic execution, data integrity, and throughput.</p>
              <div class="dev-pills-wrap">
                <span class="dev-tech-pill"><i class="fab fa-microsoft" style="color: #512bd4;"></i> ASP.NET Core</span>
                <span class="dev-tech-pill"><i class="fal fa-code" style="color: #239120;"></i> C#</span>
                <span class="dev-tech-pill"><i class="fal fa-network-wired" style="color: #FF2E3E;"></i> RESTful APIs</span>
                <span class="dev-tech-pill"><i class="fab fa-node-js" style="color: #339933;"></i> Node.js</span>
                <span class="dev-tech-pill"><i class="fal fa-cubes" style="color: #6b7280;"></i> Microservices</span>
              </div>
            </div>

            <!-- Group 3: Data -->
            <div class="dev-tech-card wow fadeInUp" data-wow-delay="0.3s">
              <div class="dev-tech-header">
                <div class="dev-tech-icon"><i class="fal fa-database"></i></div>
                <h3 class="dev-tech-group-title">Databases &amp; Storage</h3>
              </div>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">Scalable, relational and caching data stores modeled for ACID transactions, search performance, and security.</p>
              <div class="dev-pills-wrap">
                <span class="dev-tech-pill"><i class="fal fa-database" style="color: #cc292b;"></i> SQL Server</span>
                <span class="dev-tech-pill"><i class="fal fa-database" style="color: #336791;"></i> PostgreSQL</span>
                <span class="dev-tech-pill"><i class="fal fa-bolt" style="color: #d82c20;"></i> Redis Caching</span>
                <span class="dev-tech-pill"><i class="fal fa-table" style="color: #512bd4;"></i> Entity Framework</span>
              </div>
            </div>

            <!-- Group 4: CMS & E-commerce -->
            <div class="dev-tech-card wow fadeInUp" data-wow-delay="0.4s">
              <div class="dev-tech-header">
                <div class="dev-tech-icon"><i class="fal fa-shopping-cart"></i></div>
                <h3 class="dev-tech-group-title">CMS &amp; E-commerce</h3>
              </div>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">Proven content management and online store platforms customized to eliminate administrative friction.</p>
              <div class="dev-pills-wrap">
                <span class="dev-tech-pill"><i class="fab fa-wordpress" style="color: #21759b;"></i> WordPress</span>
                <span class="dev-tech-pill"><i class="fal fa-store" style="color: #96588a;"></i> WooCommerce</span>
                <span class="dev-tech-pill"><i class="fab fa-shopify" style="color: #96bf48;"></i> Shopify Liquid</span>
                <span class="dev-tech-pill"><i class="fal fa-tags" style="color: #FF2E3E;"></i> Storefront API</span>
              </div>
            </div>

            <!-- Group 5: Desktop -->
            <div class="dev-tech-card wow fadeInUp" data-wow-delay="0.5s">
              <div class="dev-tech-header">
                <div class="dev-tech-icon"><i class="fal fa-desktop"></i></div>
                <h3 class="dev-tech-group-title">Desktop Software</h3>
              </div>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">Dedicated operational utilities engineered for high-throughput processing, hardware integration, and offline stability.</p>
              <div class="dev-pills-wrap">
                <span class="dev-tech-pill"><i class="fab fa-windows" style="color: #0078d7;"></i> .NET Desktop</span>
                <span class="dev-tech-pill"><i class="fal fa-window" style="color: #512bd4;"></i> WPF</span>
                <span class="dev-tech-pill"><i class="fal fa-laptop-code" style="color: #239120;"></i> Windows Forms</span>
                <span class="dev-tech-pill"><i class="fal fa-microchip" style="color: #FF2E3E;"></i> Local DB Sync</span>
              </div>
            </div>

            <!-- Group 6: Integrations -->
            <div class="dev-tech-card wow fadeInUp" data-wow-delay="0.6s">
              <div class="dev-tech-header">
                <div class="dev-tech-icon"><i class="fal fa-plug"></i></div>
                <h3 class="dev-tech-group-title">APIs &amp; Integrations</h3>
              </div>
              <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">Secure connections linking your software to third-party services, payment providers, and enterprise systems.</p>
              <div class="dev-pills-wrap">
                <span class="dev-tech-pill"><i class="fab fa-stripe" style="color: #635bff;"></i> Stripe API</span>
                <span class="dev-tech-pill"><i class="fab fa-paypal" style="color: #003087;"></i> Payment Gateways</span>
                <span class="dev-tech-pill"><i class="fal fa-key" style="color: #f59e0b;"></i> OAuth 2.0 &amp; JWT</span>
                <span class="dev-tech-pill"><i class="fal fa-bolt" style="color: #FF2E3E;"></i> Webhook Pipelines</span>
                <span class="dev-tech-pill"><i class="fal fa-sync" style="color: #10b981;"></i> Two-Way Sync</span>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           09 — INCLUDED IN SCOPE SECTION
      ================================================================== -->
      <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
        <div class="container">
          <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="dev-eyebrow">INCLUDED IN SCOPE</span>
            <h2 class="vibe-heading" style="font-size: 40px;">What You Can Expect From Our Development Work</h2>
            <p class="vibe-lead">Every software project we undertake is delivered with rigorous standards, transparent milestones, and complete client ownership.</p>
          </div>

          <div class="dev-scope-grid">
            
            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.05s">
              <div class="dev-scope-icon"><i class="fal fa-clipboard-list-check"></i></div>
              <h3 class="dev-scope-title">Requirements &amp; Scope</h3>
              <p class="dev-scope-desc">Clear boundaries, agreed feature lists, and defined success criteria before writing a line of code.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.10s">
              <div class="dev-scope-icon"><i class="fal fa-mobile-alt"></i></div>
              <h3 class="dev-scope-title">Responsive Interfaces</h3>
              <p class="dev-scope-desc">Pixel-perfect user interfaces tested on desktop, tablet, and mobile breakpoints for seamless interaction.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.15s">
              <div class="dev-scope-icon"><i class="fal fa-code"></i></div>
              <h3 class="dev-scope-title">Agreed Feature Builds</h3>
              <p class="dev-scope-desc">Purpose-built business logic, database relationships, and admin features built strictly to agreed specifications.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.20s">
              <div class="dev-scope-icon"><i class="fal fa-plug"></i></div>
              <h3 class="dev-scope-title">Reliable Integrations</h3>
              <p class="dev-scope-desc">Secure webhooks and API connections with automated retry handling and schema validation.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.25s">
              <div class="dev-scope-icon"><i class="fal fa-vial"></i></div>
              <h3 class="dev-scope-title">Testing &amp; Bug Fixing</h3>
              <p class="dev-scope-desc">Cross-browser validation, workflow simulation, and prioritized fixes before launch sign-off.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.30s">
              <div class="dev-scope-icon"><i class="fal fa-cloud-upload"></i></div>
              <h3 class="dev-scope-title">Deployment Assistance</h3>
              <p class="dev-scope-desc">Production server setup, domain routing, SSL certificate installation, and launch smoke tests.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.35s">
              <div class="dev-scope-icon"><i class="fal fa-book-open"></i></div>
              <h3 class="dev-scope-title">Handover &amp; IP Ownership</h3>
              <p class="dev-scope-desc">100% intellectual property ownership, full Git repository access, and technical handover documentation.</p>
            </div>

            <div class="dev-scope-card wow fadeInUp" data-wow-delay="0.40s">
              <div class="dev-scope-icon"><i class="fal fa-heart-rate"></i></div>
              <h3 class="dev-scope-title">Optional Ongoing Care</h3>
              <p class="dev-scope-desc">Dedicated post-launch support agreements covering bug fixing, upgrades, and continuous improvements.</p>
            </div>

          </div>

          <!-- Scope Disclaimer Note -->
          <div class="mt-4 p-3 rounded-2 text-center mx-auto" style="max-width: 860px; background: #ffffff; border: 1px solid #e5e7eb;">
            <p style="font-family: 'Sora', sans-serif !important; font-size: 13px; color: #6b7280; margin: 0; line-height: 1.5;">
              <i class="fa fa-info-circle text-danger mr-1"></i> <strong>Note:</strong> Project deliverables depend on the agreed proposal, platform, complexity, and service package. Hosting, subscriptions, paid plugins, third-party licenses, and ongoing support should be specified separately where applicable.
            </p>
          </div>

        </div>
      </section>

      <!-- =================================================================
           10 — DEVELOPMENT PACKAGES SECTION
      ================================================================== -->
      <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
        <div class="container">
          <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="dev-eyebrow">ENGAGEMENT OPTIONS</span>
            <h2 class="vibe-heading" style="font-size: 40px;">Choose the Right Starting Point</h2>
            <p class="vibe-lead">We structure development engagements around your specific project size, technical needs, and timeline.</p>
          </div>

          <div class="dev-packages-grid">

            <!-- Package 1 -->
            <div class="dev-package-card wow fadeInUp" data-wow-delay="0.1s">
              <h3 class="dev-package-title">Website &amp; Store Launch</h3>
              <p class="dev-package-desc">For businesses launching a high-performance marketing website, portfolio, landing page, or online store.</p>
              <ul class="dev-package-features">
                <li><i class="fa fa-check"></i> Initial requirements discussion &amp; structure</li>
                <li><i class="fa fa-check"></i> Agreed page or storefront layout design</li>
                <li><i class="fa fa-check"></i> Responsive mobile &amp; tablet optimization</li>
                <li><i class="fa fa-check"></i> Contact form &amp; lead capture integration</li>
                <li><i class="fa fa-check"></i> Basic quality &amp; speed checks</li>
                <li><i class="fa fa-check"></i> Deployment &amp; domain launch assistance</li>
              </ul>
              <a href="contact.html" class="btn btn-outline-dark w-100" style="padding: 12px; font-family: 'Sora', sans-serif !important; font-weight: 600; font-size: 14px; border-radius: 8px;">
                Request a Proposal
              </a>
            </div>

            <!-- Package 2 (Popular) -->
            <div class="dev-package-card popular wow fadeInUp" data-wow-delay="0.2s">
              <span class="dev-package-badge">RECOMMENDED</span>
              <h3 class="dev-package-title">Custom Software Project</h3>
              <p class="dev-package-desc">For businesses needing a tailored web application, desktop tool, operational dashboard, or bespoke integration.</p>
              <ul class="dev-package-features">
                <li><i class="fa fa-check"></i> Comprehensive technical scoping &amp; requirements</li>
                <li><i class="fa fa-check"></i> UI/UX wireframing &amp; interface planning</li>
                <li><i class="fa fa-check"></i> Database architecture &amp; secure API endpoints</li>
                <li><i class="fa fa-check"></i> Role-based authentication &amp; permissions</li>
                <li><i class="fa fa-check"></i> Rigorous acceptance testing &amp; staging demo</li>
                <li><i class="fa fa-check"></i> Production deployment &amp; code handover</li>
              </ul>
              <a href="contact.html" class="btn w-100" style="background: #FF2E3E; color: #ffffff; padding: 12px; font-family: 'Sora', sans-serif !important; font-weight: 700; font-size: 14px; border-radius: 8px; border: none;">
                Request a Proposal
              </a>
            </div>

            <!-- Package 3 -->
            <div class="dev-package-card wow fadeInUp" data-wow-delay="0.3s">
              <h3 class="dev-package-title">Ongoing Development &amp; Care</h3>
              <p class="dev-package-desc">For businesses that need regular improvements, technical updates, and dedicated engineering support.</p>
              <ul class="dev-package-features">
                <li><i class="fa fa-check"></i> Agreed monthly maintenance hours</li>
                <li><i class="fa fa-check"></i> Priority bug fixing &amp; issue troubleshooting</li>
                <li><i class="fa fa-check"></i> Iterative feature additions &amp; UI upgrades</li>
                <li><i class="fa fa-check"></i> Security audits &amp; framework updates</li>
                <li><i class="fa fa-check"></i> Performance tuning &amp; database checks</li>
                <li><i class="fa fa-check"></i> Periodic improvement planning meetings</li>
              </ul>
              <a href="contact.html" class="btn btn-outline-dark w-100" style="padding: 12px; font-family: 'Sora', sans-serif !important; font-weight: 600; font-size: 14px; border-radius: 8px;">
                Request a Proposal
              </a>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           11 — CLEAR CLIENT JOURNEY (5 STEPS)
      ================================================================== -->
      <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #e5e7eb;">
        <div class="container">
          <div class="mb-5 d-flex flex-column align-items-start wow fadeInUp" style="gap: 10px;">
            <span class="dev-eyebrow">THE COLLABORATION PROCESS</span>
            <h2 class="vibe-heading" style="font-size: 40px;">The Client Journey: From Concept to Launch</h2>
            <p class="vibe-lead">A transparent, structured engineering partnership every step of the way.</p>
          </div>

          <div class="dev-journey-grid">
            
            <div class="dev-journey-card wow fadeInUp" data-wow-delay="0.05s">
              <div class="dev-journey-step">01</div>
              <h3 class="dev-journey-title">Tell Us About Your Project</h3>
              <p class="dev-journey-desc">Share your business problem, desired outcome, timeline, and any existing requirements or tools.</p>
            </div>

            <div class="dev-journey-card wow fadeInUp" data-wow-delay="0.10s">
              <div class="dev-journey-step">02</div>
              <h3 class="dev-journey-title">We Review Requirements</h3>
              <p class="dev-journey-desc">Techtox evaluates feasibility, likely architecture, technical considerations, and initial dependencies.</p>
            </div>

            <div class="dev-journey-card wow fadeInUp" data-wow-delay="0.15s">
              <div class="dev-journey-step">03</div>
              <h3 class="dev-journey-title">Scope &amp; Proposal</h3>
              <p class="dev-journey-desc">We deliver a detailed proposal with deliverables, milestones, assumptions, effort estimates, and commercial terms.</p>
            </div>

            <div class="dev-journey-card wow fadeInUp" data-wow-delay="0.20s">
              <div class="dev-journey-step">04</div>
              <h3 class="dev-journey-title">Build &amp; Review</h3>
              <p class="dev-journey-desc">Development proceeds in agreed stages with regular demos, feedback checkpoints, and milestone sign-offs.</p>
            </div>

            <div class="dev-journey-card wow fadeInUp" data-wow-delay="0.25s">
              <div class="dev-journey-step">05</div>
              <h3 class="dev-journey-title">Launch &amp; Support</h3>
              <p class="dev-journey-desc">We deploy the solution live, hand over code and documentation, and initiate ongoing maintenance if selected.</p>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           12 — DEVELOPMENT FAQ SECTION (10 QUESTIONS ACCORDION)
      ================================================================== -->
      <section class="py-5" style="background-color: #ffffff; padding-top: 80px !important; padding-bottom: 80px !important; border-bottom: 1px solid #f3f4f6;">
        <div class="container dev-faq-container">
          <div class="text-center mb-5 pb-2 mx-auto wow fadeInUp" style="max-width: 700px;">
            <span class="dev-eyebrow">DEVELOPMENT FAQS</span>
            <h2 class="vibe-heading" style="font-size: 40px;">Frequently Asked Questions About Development</h2>
            <p class="vibe-lead">Straightforward answers about our software engineering, web development, technologies, process, and delivery.</p>
          </div>

          <div class="dev-faq-list">

            <!-- Question 1 -->
            <div class="dev-faq-item active wow fadeInUp" data-wow-delay="0.05s">
              <div class="dev-faq-header">
                <h3>What types of software does Techtox develop?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>We develop custom web applications, business management tools, admin dashboards, employee and customer portals, corporate WordPress websites, Shopify and WooCommerce e-commerce storefronts, desktop business utilities, and secure API system integrations.</p>
              </div>
            </div>

            <!-- Question 2 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.10s">
              <div class="dev-faq-header">
                <h3>Can you develop both websites and custom applications?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. We build high-converting marketing websites and e-commerce stores, as well as complex, database-driven web applications and desktop tools with custom workflows, business logic, and role-based permissions.</p>
              </div>
            </div>

            <!-- Question 3 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.15s">
              <div class="dev-faq-header">
                <h3>Do you work with existing websites and applications?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. We can audit, troubleshoot, modernize, refactor, and add new features to existing codebases and platforms, provided the existing infrastructure is accessible, maintainable, and aligned with agreed project goals.</p>
              </div>
            </div>

            <!-- Question 4 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.20s">
              <div class="dev-faq-header">
                <h3>Can you integrate third-party APIs and business systems?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. We regularly connect applications with third-party APIs, CRM platforms, customer support helpdesks, payment gateways, ERP systems, and internal databases using secure webhooks, background queues, and custom endpoints.</p>
              </div>
            </div>

            <!-- Question 5 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.25s">
              <div class="dev-faq-header">
                <h3>Can I request a custom desktop application?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. For workflows that require dedicated local computing performance, hardware integration (e.g. barcode scanners, local printers), or structured internal data processing without browser overhead, we engineer focused desktop applications using modern .NET technologies.</p>
              </div>
            </div>

            <!-- Question 6 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.30s">
              <div class="dev-faq-header">
                <h3>How do you estimate project cost and timeline?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>We estimate projects based on clear requirements, feature scope, architectural complexity, UI/UX requirements, and necessary third-party integrations. After an initial discovery discussion, we provide a detailed written proposal outlining milestones, delivery timelines, and budget before work begins.</p>
              </div>
            </div>

            <!-- Question 7 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.35s">
              <div class="dev-faq-header">
                <h3>Can I review the application before launch?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. We conduct milestone demonstrations and provide access to a secure staging environment where your team can review, test, and provide feedback on the working software before it is deployed to production.</p>
              </div>
            </div>

            <!-- Question 8 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.40s">
              <div class="dev-faq-header">
                <h3>Will I receive the source code and documentation?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. Upon project completion and final settlement under the agreed project agreement, you receive complete intellectual property ownership, source code transfer via your own GitHub repository, and technical handover documentation.</p>
              </div>
            </div>

            <!-- Question 9 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.45s">
              <div class="dev-faq-header">
                <h3>Do you offer maintenance after deployment?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. We offer post-launch hypercare and ongoing development agreements covering troubleshooting, performance monitoring, security patches, framework updates, and iterative feature expansion.</p>
              </div>
            </div>

            <!-- Question 10 -->
            <div class="dev-faq-item wow fadeInUp" data-wow-delay="0.50s">
              <div class="dev-faq-header">
                <h3>Can you work with an existing team or developer?</h3>
                <i class="fa fa-chevron-down dev-faq-icon"></i>
              </div>
              <div class="dev-faq-body">
                <p>Yes. We frequently collaborate with internal teams, handling specialized modules, backend integrations, or new product builds while adhering to your team's Git workflows, code review standards, and communication channels.</p>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- =================================================================
           13 — STRONG FINAL CTA SECTION
      ================================================================== -->
      <section class="py-5" style="background-color: #f9fafb; padding-top: 80px !important; padding-bottom: 80px !important;">
        <div class="container">
          <div class="dev-final-cta-box p-5 p-lg-5 wow fadeInUp" data-wow-delay="0.1s">
            <div class="row align-items-center">
              
              <div class="col-lg-7 mb-4 mb-lg-0 pr-lg-4">
                <span class="dev-eyebrow">READY TO BUILD?</span>
                <h2 style="font-family: 'Sora', sans-serif !important; font-size: 42px; font-weight: 700; color: #ffffff; letter-spacing: -1.2px; line-height: 1.15; margin-bottom: 16px;">
                  Let's Turn Your Requirements Into Working Software.
                </h2>
                <p style="font-family: 'Sora', sans-serif !important; font-size: 16px; color: #d1d5db; line-height: 1.65; margin-bottom: 30px;">
                  Whether you need a new website, an e-commerce store, a custom application, a desktop solution, or connected business systems, Techtox can help you define the next practical step.
                </p>
                <div class="d-flex align-items-center flex-wrap gap-3" style="gap: 16px;">
                  <a href="contact.html" class="fv-dual-btn">
                    <span class="fv-btn-pill">DISCUSS YOUR PROJECT</span>
                    <div class="fv-btn-circle">
                      <i class="fa fa-arrow-right arrow-main"></i>
                      <i class="fa fa-arrow-right arrow-hover"></i>
                    </div>
                  </a>
                  <a href="#dev-video-demo" class="btn btn-outline-light" style="font-family: 'Sora', sans-serif !important; font-size: 14px; font-weight: 600; padding: 12px 22px; border-radius: 9999px;">
                    <i class="fa fa-play mr-2" style="color: #FF2E3E;"></i> Watch Walkthrough
                  </a>
                </div>
              </div>

              <div class="col-lg-5">
                <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 28px;">
                  <h4 style="font-family: 'Sora', sans-serif !important; font-size: 16px; font-weight: 700; color: #ffffff; margin-bottom: 16px;">
                    What You Get With Techtox:
                  </h4>
                  <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px;">
                    <li style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #e5e7eb; display: flex; align-items: center; gap: 10px;">
                      <i class="fa fa-check text-danger"></i> Purpose-built architecture for your workflow
                    </li>
                    <li style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #e5e7eb; display: flex; align-items: center; gap: 10px;">
                      <i class="fa fa-check text-danger"></i> 100% intellectual property &amp; code ownership
                    </li>
                    <li style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #e5e7eb; display: flex; align-items: center; gap: 10px;">
                      <i class="fa fa-check text-danger"></i> Transparent milestone reviews &amp; staging demos
                    </li>
                    <li style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #e5e7eb; display: flex; align-items: center; gap: 10px;">
                      <i class="fa fa-check text-danger"></i> Secure, maintainable, scalable implementation
                    </li>
                    <li style="font-family: 'Sora', sans-serif !important; font-size: 14px; color: #e5e7eb; display: flex; align-items: center; gap: 10px;">
                      <i class="fa fa-check text-danger"></i> Dedicated post-launch support &amp; maintenance
                    </li>
                  </ul>
                </div>
              </div>

            </div>
          </div>
        </div>
      </section>

    </div>'''

# Load services.html
with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

# Pattern to find old #development div
pattern = r'(<div id="development"[^>]*>.*?</div>\s*</div>\s*</div>)'
match = re.search(pattern, services_content, re.DOTALL)
if not match:
    # Alternative search between <div id="development" and <div id="marketing"
    pattern2 = r'(<div id="development"[^>]*>.*?)(?=\s*<div id="marketing")'
    match2 = re.search(pattern2, services_content, re.DOTALL)
    if match2:
        old_block = match2.group(1)
        services_content = services_content.replace(old_block, dev_html)
        print("Replaced development section via pattern2!")
    else:
        print("ERROR: Could not find #development div in services.html")
else:
    # Replace the old development div
    old_block = match.group(1)
    services_content = services_content.replace(old_block, dev_html)
    print("Replaced development section via pattern1!")

# Also ensure interactive scripts for FAQ Accordion and Video Management are in services.html
script_code = '''
<!-- INTERACTIVE SCRIPTS: DEVELOPMENT FAQ ACCORDION & VIDEO SOURCE MANAGEMENT -->
<script>
$(document).ready(function() {
   // 1. Development FAQ Accordion
   $('.dev-faq-header').on('click', function() {
      var item = $(this).closest('.dev-faq-item');
      var isActive = item.hasClass('active');
      $('.dev-faq-item').removeClass('active');
      if (!isActive) {
         item.addClass('active');
      }
   });

   // 2. Video Player & Lightbox Initialization
   if ($.fn.magnificPopup) {
      $('.popup-youtube').magnificPopup({
         type: 'iframe',
         mainClass: 'mfp-fade',
         removalDelay: 160,
         preloader: false,
         fixedContentPos: false,
         iframe: {
            patterns: {
               youtube: {
                  index: 'youtube.com/',
                  id: 'v=',
                  src: 'https://www.youtube.com/embed/%id%?autoplay=1&rel=0'
               },
               vimeo: {
                  index: 'vimeo.com/',
                  id: '/',
                  src: '//player.vimeo.com/video/%id%?autoplay=1'
               }
            }
         }
      });
   }

   // 3. Admin Video Management Drawer Toggle & Persistence
   var storageKey = 'techtox_dev_video_config';
   
   function loadVideoConfig() {
      try {
         var saved = localStorage.getItem(storageKey);
         if (saved) {
            var cfg = JSON.parse(saved);
            if (cfg.url) {
               $('#dev-main-video-trigger').attr('href', cfg.url);
               $('#dev-hero-video-link').attr('href', cfg.url);
               $('#dev-cfg-url').val(cfg.url);
               $('#dev-video-source-label').text(cfg.url.indexOf('youtube') > -1 ? 'YouTube Walkthrough' : (cfg.url.indexOf('vimeo') > -1 ? 'Vimeo Walkthrough' : 'Configured MP4 Stream'));
            }
            if (cfg.poster) {
               $('#dev-video-inner-container').css('background-image', "linear-gradient(rgba(11, 15, 23, 0.72), rgba(11, 15, 23, 0.88)), url('" + cfg.poster + "')");
               $('#dev-cfg-poster').val(cfg.poster);
            }
            if (cfg.title) {
               $('#dev-video-title-display').text(cfg.title);
               $('#dev-cfg-title').val(cfg.title);
            }
            if (cfg.desc) {
               $('#dev-video-desc-display').text(cfg.desc);
               $('#dev-cfg-desc').val(cfg.desc);
            }
         }
      } catch (e) {
         console.warn('LocalStorage unavailable for video config', e);
      }
   }

   loadVideoConfig();

   $('#dev-toggle-video-admin').on('click', function(e) {
      e.preventDefault();
      $('#dev-video-config-drawer').slideToggle(200);
   });

   $('#dev-close-video-admin').on('click', function(e) {
      e.preventDefault();
      $('#dev-video-config-drawer').slideUp(200);
   });

   $('#dev-cfg-save-btn').on('click', function(e) {
      e.preventDefault();
      var newUrl = $('#dev-cfg-url').val().trim();
      var newPoster = $('#dev-cfg-poster').val().trim();
      var newTitle = $('#dev-cfg-title').val().trim();
      var newDesc = $('#dev-cfg-desc').val().trim();

      if (!newUrl) {
         alert('Please enter a valid video URL.');
         return;
      }

      var config = {
         url: newUrl,
         poster: newPoster || 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1920&q=80',
         title: newTitle || 'How Our Software Development Process Works',
         desc: newDesc || 'Watch a practical walkthrough of our software development process.'
      };

      try {
         localStorage.setItem(storageKey, JSON.stringify(config));
         loadVideoConfig();
         alert('Video configuration saved and applied successfully!');
         $('#dev-video-config-drawer').slideUp(200);
      } catch(err) {
         alert('Could not save to localStorage: ' + err.message);
      }
   });

   $('#dev-cfg-reset-btn').on('click', function(e) {
      e.preventDefault();
      try {
         localStorage.removeItem(storageKey);
         $('#dev-main-video-trigger').attr('href', 'https://www.youtube.com/watch?v=LXb3EKWsInQ');
         $('#dev-hero-video-link').attr('href', 'https://www.youtube.com/watch?v=LXb3EKWsInQ');
         $('#dev-video-inner-container').css('background-image', "linear-gradient(rgba(11, 15, 23, 0.72), rgba(11, 15, 23, 0.88)), url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1920&q=80')");
         $('#dev-video-title-display').text('How Our Software Development Process Works');
         $('#dev-video-desc-display').text('Watch a practical walkthrough of how a software project moves from business requirements and interface planning to development, testing, deployment, and ongoing support.');
         $('#dev-video-source-label').text('YouTube Walkthrough');
         $('#dev-cfg-url').val('');
         $('#dev-cfg-poster').val('');
         $('#dev-cfg-title').val('');
         $('#dev-cfg-desc').val('');
         alert('Restored default walkthrough video.');
         $('#dev-video-config-drawer').slideUp(200);
      } catch(err) {}
   });
});
</script>
</body>
'''

if 'dev-video-config-drawer' not in services_content:
    services_content = services_content.replace('</body>', script_code)
    print("Injected development scripts before </body>!")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_content)

print("Updated services.html successfully!")
