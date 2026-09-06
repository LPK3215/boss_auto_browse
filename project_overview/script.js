/* =========================================================================
   BOSS Auto Browse · Project Overview — script.js
   Interactions: scroll progress, nav highlight, theme toggle, count animation,
                 arch tooltip, copy buttons, back-to-top, mobile menu
   ========================================================================= */

document.addEventListener('DOMContentLoaded', () => {

  // --- Lucide Icons ---
  if (window.lucide) lucide.createIcons();

  // --- Scroll Progress Bar ---
  const progressBar = document.getElementById('scroll-progress');
  function updateScrollProgress() {
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const pct = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progressBar.style.width = pct + '%';
  }
  window.addEventListener('scroll', updateScrollProgress, { passive: true });
  updateScrollProgress();

  // --- Nav Active Highlight ---
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');
  function highlightNav() {
    let current = '';
    sections.forEach(sec => {
      const top = sec.offsetTop - 100;
      if (window.scrollY >= top) current = sec.id;
    });
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }
  window.addEventListener('scroll', highlightNav, { passive: true });

  // --- Smooth Scroll for Nav Links ---
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          window.scrollTo({ top: target.offsetTop - 70, behavior: 'smooth' });
        }
        // Close mobile nav if open
        mobileNav.classList.remove('open');
      }
    });
  });

  // --- Theme Toggle with localStorage persistence ---
  const themeToggle = document.getElementById('themeToggle');
  const html = document.documentElement;
  const STORAGE_KEY = 'boss-auto-browse-theme';

  // Priority: localStorage > system preference > default dark
  const savedTheme = localStorage.getItem(STORAGE_KEY);
  if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    html.setAttribute('data-theme', 'light');
  }

  // Set initial icon based on current theme
  const initIcon = themeToggle.querySelector('[data-lucide]');
  if (initIcon) {
    const currentTheme = html.getAttribute('data-theme') || 'dark';
    initIcon.setAttribute('data-lucide', currentTheme === 'dark' ? 'moon' : 'sun');
    if (window.lucide) lucide.createIcons();
  }

  themeToggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme') || 'dark';
    const next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem(STORAGE_KEY, next);
    // Update icon
    const icon = themeToggle.querySelector('[data-lucide]');
    if (icon) {
      icon.setAttribute('data-lucide', next === 'dark' ? 'moon' : 'sun');
      if (window.lucide) lucide.createIcons();
    }
  });

  // --- Mobile Menu ---
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav = document.getElementById('mobileNav');
  menuToggle.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
  });

  // --- Number Count Animation ---
  const statNums = document.querySelectorAll('.stat-num');
  const animateNumber = (el) => {
    const target = parseInt(el.dataset.target);
    const duration = 1200;
    const startTime = performance.now();
    const step = (now) => {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easeOut = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(target * easeOut).toLocaleString();
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = target.toLocaleString();
    };
    requestAnimationFrame(step);
  };

  // Trigger when hero is visible
  const heroObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        statNums.forEach(animateNumber);
        heroObserver.disconnect();
      }
    });
  }, { threshold: 0.3 });
  const hero = document.getElementById('hero');
  if (hero) heroObserver.observe(hero);

  // --- Copy Buttons ---
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const code = btn.dataset.code || '';
      navigator.clipboard.writeText(code).then(() => {
        const originalText = btn.textContent;
        btn.textContent = '已复制';
        btn.style.color = 'var(--accent)';
        btn.style.borderColor = 'var(--accent)';
        setTimeout(() => {
          btn.textContent = originalText;
          btn.style.color = '';
          btn.style.borderColor = '';
        }, 1500);
      }).catch(() => {
        // Fallback
        const textarea = document.createElement('textarea');
        textarea.value = code;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        btn.textContent = '已复制';
        setTimeout(() => { btn.textContent = '复制'; }, 1500);
      });
    });
  });

  // --- Architecture Tooltip ---
  const tooltip = document.getElementById('archTooltip');
  const archNodes = document.querySelectorAll('.arch-node');
  archNodes.forEach(node => {
    node.addEventListener('mouseenter', (e) => {
      const text = node.getAttribute('data-tooltip');
      if (text) {
        tooltip.textContent = text;
        tooltip.classList.add('show');
      }
    });
    node.addEventListener('mousemove', (e) => {
      tooltip.style.left = (e.clientX + 14) + 'px';
      tooltip.style.top = (e.clientY + 14) + 'px';
    });
    node.addEventListener('mouseleave', () => {
      tooltip.classList.remove('show');
    });
  });

  // --- Back to Top ---
  const backToTop = document.getElementById('backToTop');
  function toggleBackToTop() {
    if (window.scrollY > window.innerHeight) {
      backToTop.classList.add('show');
    } else {
      backToTop.classList.remove('show');
    }
  }
  window.addEventListener('scroll', toggleBackToTop, { passive: true });
  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // --- Card Reveal on Scroll ---
  const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.card').forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = `opacity 0.5s ease ${i * 0.05}s, transform 0.5s ease ${i * 0.05}s`;
    cardObserver.observe(card);
  });

});
