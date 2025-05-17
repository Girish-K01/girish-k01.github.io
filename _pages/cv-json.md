---
layout: archive
title: "Curriculum Vitae"
permalink: /cv-json/
author_profile: false
redirect_from:
  - /resume-json
---

{% include base_path %}

<link rel="stylesheet" href="{{ base_path }}/assets/css/cv-style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  .archive {
    width: 90%;
    margin: 0 auto;
    float: none;
    padding-right: 0;
  }
  
  @media (min-width: 80em) {
    .archive {
      width: 80%;
    }
  }
  
  @media print {
    .archive {
      width: 100%;
      margin: 0;
      padding: 0;
    }
    
    #main {
      margin: 0 !important;
      padding: 0 !important;
    }
    
    .page__content {
      padding: 0 !important;
    }
    
    .sidebar, header, nav, footer, .page__footer {
      display: none !important;
    }
  }
  
  /* Print Button Styles */
  .print-button {
    position: fixed;
    right: 20px;
    bottom: 20px;
    background-color: #6366f1;
    color: white;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    font-size: 24px;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    z-index: 1000;
  }
  
  .print-button:hover {
    background-color: #4f46e5;
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
  }
  
  @media print {
    .print-button {
      display: none !important;
    }
  }
</style>

{% include cv-template.html %}

<div class="cv-download-links">
  <a href="{{ base_path }}/files/cv.pdf" class="btn btn--primary">Download CV as PDF</a>
  <a href="{{ base_path }}/cv-json" class="btn btn--inverse">View Markdown CV</a>
</div>

<button onclick="window.print()" class="print-button" title="Print CV">
  <i class="fas fa-print"></i>
</button>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Add print optimization script
    window.onbeforeprint = function() {
      // Add any pre-print optimizations here
      document.body.classList.add('printing');
    };
    
    window.onafterprint = function() {
      // Reset any changes after printing
      document.body.classList.remove('printing');
    };
  });
</script>