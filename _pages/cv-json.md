---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
  - /cv
---

{% include base_path %}

<!-- Load required CSS -->
<link rel="stylesheet" href="{{ base_path }}/assets/css/cv-style.css">
<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"> -->

<!-- CV Content -->
{% include cv-template.html %}

<!-- Download Link -->
<div class="cv-download-links">
  <a href="{{ base_path }}/files/cv.pdf" class="btn btn--primary">Download PDF</a>
</div>

<!-- Print Button -->
<button onclick="window.print()" class="print-button" title="Print CV">
  <i class="fas fa-print"></i>
</button>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Make sure all CV sections are visible
    document.querySelectorAll('.cv-hide-in-resume').forEach(function(el) {
      el.style.display = 'block';
    });
    
    // Remove any condensed styling
    document.querySelectorAll('.cv-resume-condensed').forEach(function(el) {
      el.classList.remove('condensed');
    });
    
    // Print optimization
    window.onbeforeprint = function() {
      // Add any pre-print optimizations here
      document.body.classList.add('printing');
      
      // Ensure proper page breaks
      const sections = document.querySelectorAll('.cv-section');
      sections.forEach(function(section) {
        if (section.offsetTop > window.innerHeight * 0.75) {
          section.style.pageBreakBefore = 'always';
        }
      });
    };
    
    window.onafterprint = function() {
      // Reset any changes after printing
      document.body.classList.remove('printing');
      
      // Reset page break styles
      document.querySelectorAll('.cv-section').forEach(function(section) {
        section.style.pageBreakBefore = '';
      });
    };
    
    // Handle window resize for responsive layout
    window.addEventListener('resize', function() {
      // Add any responsive adjustments here
      if (window.innerWidth < 768) {
        // Mobile adjustments
        document.querySelectorAll('.cv-projects, .cv-skills, .cv-research').forEach(function(grid) {
          grid.style.gridTemplateColumns = '1fr';
        });
      } else {
        // Desktop adjustments
        document.querySelectorAll('.cv-projects, .cv-research').forEach(function(grid) {
          grid.style.gridTemplateColumns = 'repeat(2, 1fr)';
        });
        
        document.querySelectorAll('.cv-skills').forEach(function(grid) {
          grid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(250px, 1fr))';
        });
      }
    });
    
    // Trigger resize event initially
    window.dispatchEvent(new Event('resize'));
  });
</script>