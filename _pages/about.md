---
permalink: /
title: "About me"
excerpt: "AI Systems Engineer & Researcher focused on high-performance systems, machine learning, and applied cryptography"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
/* Custom styles for about page - with dark mode support */
:root {
  --text-color: inherit;
  --accent-color: #2a76dd;
  --border-color: #f2f3f3;
  --card-bg-color: rgba(0, 0, 0, 0.05);
  --card-border-color: #2a76dd;
  --quote-bg-color: rgba(0, 0, 0, 0.03);
  --contact-link-bg: rgba(0, 0, 0, 0.03);
  --contact-link-hover-bg: rgba(0, 0, 0, 0.08);
}

.dark {
  --accent-color: #4d8fec;
  --border-color: rgba(255, 255, 255, 0.1);
  --card-bg-color: rgba(255, 255, 255, 0.05);
  --card-border-color: #4d8fec;
  --quote-bg-color: rgba(255, 255, 255, 0.05);
  --contact-link-bg: rgba(255, 255, 255, 0.08);
  --contact-link-hover-bg: rgba(255, 255, 255, 0.12);
}

.profile-header {
  margin-bottom: 2em;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 1em;
}

.highlight-text {
  font-weight: bold;
  color: var(--accent-color);
}

.lead-paragraph {
  font-size: 1.1em;
  line-height: 1.6;
  margin-bottom: 1.5em;
}

.section-heading {
  margin-top: 1.5em;
  padding-bottom: 0.5em;
  border-bottom: 1px solid var(--border-color);
}

.research-card {
  margin: 1em 0;
  padding: 1em;
  background-color: var(--card-bg-color);
  border-left: 3px solid var(--card-border-color);
  border-radius: 3px;
  color: var(--text-color);
}

.research-card h3 {
  margin-top: 0;
  color: var(--accent-color);
}

.research-card ul {
  padding-left: 1.5em;
}

.quote-box {
  font-style: italic;
  padding: 1em;
  margin: 1.5em 0;
  background-color: var(--quote-bg-color);
  border-radius: 5px;
  text-align: center;
  color: var(--text-color);
}

.goals-list {
  list-style-type: none;
  padding-left: 0;
}

.goals-list li {
  padding: 0.5em 0;
  margin-bottom: 0.5em;
}

.goals-list li:before {
  content: "→ ";
  color: var(--accent-color);
}

.contact-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1em;
  margin: 1.5em 0;
}

.contact-links a {
  display: inline-flex;
  align-items: center;
  padding: 0.5em 1em;
  background-color: var(--contact-link-bg);
  border-radius: 4px;
  text-decoration: none;
  transition: background-color 0.2s;
  color: var(--text-color);
}

.contact-links a:hover {
  background-color: var(--contact-link-hover-bg);
}

.signature {
  font-style: italic;
  margin-top: 2em;
  padding-top: 1em;
  border-top: 1px solid var(--border-color);
}

@media (max-width: 768px) {
  .contact-links {
    flex-direction: column;
  }
}
</style>

<div class="profile-header">
  <h1>I'm <span class="highlight-text">Girish Kulathumani</span></h1>
  <p class="lead-paragraph">A Computer Science undergraduate with a focus on <span class="highlight-text">high-performance systems, machine learning, and applied cryptography</span>. My work lies at the intersection of <span class="highlight-text">AI, systems engineering, and security</span>, where I build intelligent infrastructures that are fast, privacy-preserving, and scalable — both in code and concept.</p>
  
  <p>As a developer, I design and optimize pipelines for real-time analytics, secure communication, and edge-compatible AI. As a researcher, I explore deeper questions about perception, cognition, and the evolving architectures of intelligence — both biological and artificial.</p>
</div>

<h2 class="section-heading">Research & Development Focus</h2>

<div class="research-card">
  <h3>1. Federated & Multimodal Learning Systems</h3>
  <p>I currently lead the design of <strong>HabitatFL</strong>, a privacy-preserving framework for wildlife monitoring that integrates:</p>
  <ul>
    <li><strong>Federated Learning</strong> with dynamic configurations and resource-aware strategies</li>
    <li><strong>Multimodal perception models</strong> (vision and audio) optimized for edge inference</li>
    <li><strong>Open conservation datasets</strong> like WCS and FSC22, restructured for distributed learning</li>
  </ul>
  <p>This work aims to support ecological research while advancing edge-AI efficiency and privacy techniques.</p>
</div>

<div class="research-card">
  <h3>2. Secure Systems & Cryptographic Protocols</h3>
  <p>Through my project <strong>JIGSaw</strong>, I've developed a lightweight, parallelized secure messaging architecture featuring:</p>
  <ul>
    <li>A modified <strong>Double Ratchet algorithm</strong></li>
    <li><strong>AES-GCM</strong> encryption with advanced key management</li>
    <li>A <strong>parallel-processing pipeline</strong> with formal safety guarantees</li>
    <li>Experimental extensions into <strong>complexity-based cryptography</strong> and attacker-defender simulations</li>
  </ul>
</div>

<div class="research-card">
  <h3>3. Neuroscience-Inspired Computing</h3>
  <p>My long-term interest lies in bridging <strong>computational neuroscience</strong> and <strong>AI architectures</strong>. I'm actively exploring:</p>
  <ul>
    <li><strong>Brain decoding models</strong> for perception reconstruction</li>
    <li><strong>Recursive Perception Architectures</strong>, a novel cognitive engine that can rewrite its own perceptual rules</li>
    <li><strong>Meta-creative AI systems</strong> capable of redefining their aesthetic frameworks, inspired by human creativity and abstraction hierarchies</li>
  </ul>
  <p>I regularly write and publish insights on these themes through my research blog, <a href="https://greylattice.substack.com">GreyLattice</a>.</p>
</div>

<h2 class="section-heading">Philosophy of Work</h2>

<p>I approach systems as evolving, interpretable structures — not just codebases. Whether it's optimizing neural inference on GPUs or designing algorithms that adapt like biological entities, I care about <strong>clarity, modularity, and theoretical rigor</strong>.</p>

<div class="quote-box">
  <p>"Code should not only execute well — it should think clearly."</p>
</div>

<p>This mindset has led me to develop tools and frameworks that are both technically sound and conceptually grounded.</p>

<h2 class="section-heading">Academic Background</h2>

<p><strong>B.Tech in Computer Science and Engineering</strong><br>
Vellore Institute of Technology, Chennai<br>
(Graduating: [Your Year])</p>

<p><strong>Independent Research Focus:</strong></p>
<ul>
  <li>Federated Learning & Edge AI</li>
  <li>Cryptographic Protocol Design</li>
  <li>Computational Neuroscience & Brain-Computer Interfaces</li>
  <li>Meta-architectures for AI and Creativity</li>
</ul>

<h2 class="section-heading">Current Goals</h2>

<p>I am actively looking to:</p>
<ul class="goals-list">
  <li>Collaborate on <strong>research-driven development projects</strong></li>
  <li>Contribute to <strong>labs or open-source initiatives</strong> in edge intelligence, secure systems, or computational neuroscience</li>
  <li>Engage with teams that value both <strong>engineering precision</strong> and <strong>conceptual depth</strong></li>
  <li>Seek <strong>research internships</strong>, co-authoring opportunities, or industry-aligned academic partnerships</li>
</ul>

<h2 class="section-heading">Connect with Me</h2>

<div class="contact-links">
  <a href="https://www.girishklabs.com">🌐 Portfolio</a>
  <a href="https://greylattice.substack.com">✍️ GreyLattice Blog</a>
  <a href="https://linkedin.com/in/girish-kulathumani">💼 LinkedIn</a>
  <a href="https://github.com/Girish-K01">🐙 GitHub</a>
  <a href="mailto:girishkulathumani@gmail.com">📬 Email</a>
</div>

<div class="signature">
  <p><em>"I aim to build systems that perceive, protect, and evolve — while asking deeper questions about what intelligence, security, and understanding truly mean."</em></p>
</div>