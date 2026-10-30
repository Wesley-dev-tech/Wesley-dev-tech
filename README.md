<!-- Original profile design for Wesley Dev & Tech. SVG artwork lives in /assets. -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="./assets/header-light.svg">
    <img src="./assets/header-dark.svg" alt="Wesley Dev & Tech. Full Stack & AI Automation Developer in training. From curiosity to code. One project at a time." width="100%">
  </picture>
</p>

<p align="center">
  <strong>Full Stack & AI Automation Developer in training at SyntraPXL · Belgium</strong><br>
  Turning curiosity and practical experience into useful web projects.
</p>

<p align="center">
  <a href="https://wesley-dev-tech.github.io/Portfolio/"><img src="./assets/button-portfolio.svg?v=3" alt="Explore my portfolio" width="190"></a>
  <a href="https://www.linkedin.com/in/wesley-bogaerts/"><img src="./assets/button-linkedin.svg?v=3" alt="Connect on LinkedIn" width="190"></a>
</p>

<p align="center">
  <a href="#01--the-person-behind-the-code"><img src="./assets/button-about.svg?v=3" alt="About me" width="148"></a> 
  <a href="#02--less-talk-more-projects"><img src="./assets/button-projects.svg?v=3" alt="Selected projects" width="148"></a> 
  <a href="#03--my-current-toolbox"><img src="./assets/button-toolbox.svg?v=3" alt="My toolbox" width="148"></a> 
  <a href="#04--the-next-chapter"><img src="./assets/button-contact.svg?v=3" alt="Get in touch" width="148"></a>
</p>

<picture><source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg"><img src="./assets/divider-dark.svg" alt="" width="100%"></picture>

## 01 / The person behind the code

Hi, I'm Wesley. After several years in administration and finance, I made a deliberate switch to IT. I'm now studying full-time at **SyntraPXL**, building my foundations in web development and databases while exploring AI automation.

I've worked with invoices, reporting and the processes behind them. That experience makes me curious about how software can help someone get a real task done. My flooring calculator is one example: user input becomes a price calculation, then a downloadable quote.

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/strengths-light.svg">
  <img src="./assets/strengths-dark.svg" alt="What I bring: business context from finance, data thinking through MySQL, and projects with practical output." width="100%">
</picture>

<details>
<summary><strong>Open developer.config.ts</strong></summary>

```ts
type Developer = {
  name: string;
  role: string;
  location: string;
  background: string[];
  education: { track: string; school: string };
  building: string[];
  toolbox: Record<string, string[]>;
  mindset: string;
};

const wesley: Developer = {
  name: "Wesley Bogaerts",
  role: "FULL STACK DEVELOPER // in training",
  location: "Belgium",
  background: ["Finance", "Administration", "Process thinking"],
  education: {
    track: "Full Stack & AI Automation Developer",
    school: "SyntraPXL",
  },
  building: [
    "Responsive websites and web applications",
    "Interactive tools with practical output",
    "AI-assisted workflow automation",
  ],
  toolbox: {
    frontend: ["HTML", "CSS", "JavaScript", "Responsive Design"],
    learning: ["TypeScript", "APIs", "Tailwind"],
    data: ["MySQL", "Joins", "Normalization 1NF → 3NF"],
    workflow: ["Git", "GitHub", "Scrum"],
  },
  mindset: "Learn by building. Understand, test, improve.",
};

export default wesley;
```

</details>

> “Learning without thought is labour lost; thought without learning is perilous.” — Confucius, *Analects* 2:15

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/learning-lab-light.svg">
  <img src="./assets/learning-lab-dark.svg" alt="My learning lab: web interfaces, data and logic, and AI automation. Animated illustrations of the areas I am learning." width="100%">
</picture>

## 02 / Less talk, more projects

These are hands-on learning projects. Open a demo, try the interactions and explore the code.

<table>
<tr>
<td width="50%" valign="top">
<a href="https://wesley-dev-tech.github.io/Portfolio/">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Wesley-dev-tech/Portfolio/main/images/portfolio-light.webp">
  <img src="https://raw.githubusercontent.com/Wesley-dev-tech/Portfolio/main/images/portfolio-dark.webp" alt="Screenshot of my developer portfolio" width="100%">
</picture>
</a>
<h3>01 / Developer portfolio</h3>
<p>A home for my work, with light and dark themes, swipeable project cards and a downloadable CV.</p>
<p><code>HTML</code> <code>CSS</code> <code>JavaScript</code></p>
<p><a href="https://wesley-dev-tech.github.io/Portfolio/"><img src="./assets/button-demo.svg?v=3" alt="Explore the site" width="148"></a> <a href="https://github.com/Wesley-dev-tech/Portfolio"><img src="./assets/button-code.svg?v=3" alt="View source code" width="148"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://wesley-dev-tech.github.io/Flooring_price_calculator/">
<img src="https://raw.githubusercontent.com/Wesley-dev-tech/Portfolio/main/images/vloermeesters.webp" alt="Screenshot of the Vloermeesters flooring quote calculator" width="100%">
</a>
<h3>02 / Flooring quote calculator</h3>
<p>Room dimensions and tile choices become a price breakdown with VAT and a downloadable PDF quote.</p>
<p><code>JavaScript</code> <code>Bootstrap</code> <code>jsPDF</code></p>
<p><a href="https://wesley-dev-tech.github.io/Flooring_price_calculator/"><img src="./assets/button-demo.svg?v=3" alt="Try the calculator" width="148"></a> <a href="https://github.com/Wesley-dev-tech/Flooring_price_calculator"><img src="./assets/button-code.svg?v=3" alt="View source code" width="148"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://wesley-dev-tech.github.io/Examen_Griezelnacht/">
<img src="https://raw.githubusercontent.com/Wesley-dev-tech/Portfolio/main/images/examen-ravenhoek.webp" alt="Screenshot of my Griezelnacht exam project" width="100%">
</a>
<h3>03 / From design to browser</h3>
<p>My Fundamentals & tooling exam: translating a supplied design into a responsive event page. <strong>Result: 96/100.</strong></p>
<p><code>HTML</code> <code>CSS</code> <code>Bootstrap</code> <code>Flexbox</code></p>
<p><a href="https://wesley-dev-tech.github.io/Examen_Griezelnacht/"><img src="./assets/button-demo.svg?v=3" alt="View the result" width="148"></a> <a href="https://github.com/Wesley-dev-tech/Examen_Griezelnacht"><img src="./assets/button-code.svg?v=3" alt="View source code" width="148"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://wesley-dev-tech.github.io/Animated_browser_mockup/">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Wesley-dev-tech/Portfolio/main/images/browsermockup-light.webp">
  <img src="https://raw.githubusercontent.com/Wesley-dev-tech/Portfolio/main/images/browsermockup-dark.webp" alt="Screenshot of my animated browser mock-up" width="100%">
</picture>
</a>
<h3>04 / A browser inside a browser</h3>
<p>A CSS-driven cursor and scrolling preview, built to practise animation and attention to visual detail.</p>
<p><code>HTML</code> <code>CSS animation</code> <code>SVG</code></p>
<p><a href="https://wesley-dev-tech.github.io/Animated_browser_mockup/"><img src="./assets/button-demo.svg?v=3" alt="Watch it move" width="148"></a> <a href="https://github.com/Wesley-dev-tech/Animated_browser_mockup"><img src="./assets/button-code.svg?v=3" alt="View source code" width="148"></a></p>
</td>
</tr>
</table>

<sub>The calculator and event page are fictional coursework demos. More projects and exam feedback are available in my portfolio.</sub>

<a href="https://github.com/Wesley-dev-tech?tab=repositories"><img src="./assets/button-all-projects.svg?v=3" alt="Browse all my repositories" width="210"></a>

<picture><source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg"><img src="./assets/divider-dark.svg" alt="" width="100%"></picture>

## 03 / My current toolbox

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/toolbox-light.svg">
  <img src="./assets/toolbox-dark.svg" alt="Learning toolbox: HTML, CSS, JavaScript, MySQL, Git and GitHub. Also exploring TypeScript, Bootstrap, Tailwind, APIs and AI automation." width="100%">
</picture>

| Working on now | What I'm practising |
| :-- | :-- |
| Web development | Responsive layouts, Flexbox, CSS Grid and JavaScript interactions. |
| Databases | MySQL queries and joins, relationships, normalization from 1NF to 3NF. |
| AI automation & APIs | Learning how existing AI tools and APIs can support practical workflows. |
| Team workflow | Git, GitHub and Scrum fundamentals through my training. |

<sub>This is a learning stack, with different levels of experience across the tools. My projects show where I am today.</sub>

## 04 / The next chapter

I'm interested in **junior development opportunities** where I can contribute my business experience and keep developing my technical skills alongside an experienced team.

If you're building software for real business processes, we already have something to talk about.

<a href="https://wesley-dev-tech.github.io/Portfolio/">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/footer-light.svg">
  <img src="./assets/footer-dark.svg" alt="Let's build something useful. Visit my portfolio to see my work and get in touch." width="100%">
</picture>
</a>

<p align="center"><a href="https://wesley-dev-tech.github.io/Portfolio/"><img src="./assets/button-portfolio.svg?v=3" alt="Portfolio and contact" width="148"></a>  <a href="https://www.linkedin.com/in/wesley-bogaerts/"><img src="./assets/button-linkedin.svg?v=3" alt="Connect on LinkedIn" width="148"></a>  <a href="#"><img src="./assets/button-top.svg?v=3" alt="Back to top" width="148"></a><br><sub>Wesley Dev & Tech · From curiosity to code. One project at a time.</sub></p>
