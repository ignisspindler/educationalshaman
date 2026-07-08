/* Mindwright.ai */

(function () {
  'use strict';

  // ── SCROLL REVEALS (progressive: content visible without JS) ──
  // append ?static to the URL to disable, e.g. for screenshots
  if ('IntersectionObserver' in window && !location.search.includes('static')) {
    document.documentElement.classList.add('js');
    const targets = document.querySelectorAll(
      '.card, .problem-item, .service-item, .step, .triad-item, ' +
      '.bio-section, .book-note, .about-strip, .section-head, .specimen'
    );
    targets.forEach(el => el.classList.add('rise'));
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(el => io.observe(el));
  }

  // ── NAV SCROLL STATE ────────────────────────────────────
  const nav = document.querySelector('.site-nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ── MOBILE NAV TOGGLE ───────────────────────────────────
  const toggle = document.getElementById('navToggle');
  const links  = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.textContent = open ? 'Close' : 'Menu';
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        links.classList.remove('open');
        toggle.textContent = 'Menu';
      });
    });
  }

  // ── ACTIVE NAV LINK ─────────────────────────────────────
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href     = a.getAttribute('href') || '';
    const filename = href.replace(/^\//, '').replace(/#.*$/, '');
    const current  = path.replace(/^\//, '') || 'index.html';
    if (filename && current === filename) a.classList.add('active');
    if (!filename && (path === '/' || path === '/index.html')) a.classList.add('active');
  });

  // ── CONTACT FORM ────────────────────────────────────────
  const form    = document.getElementById('contactForm');
  const success = document.getElementById('formSuccess');
  const error   = document.getElementById('formError');
  const submit  = document.getElementById('submitBtn');

  if (form && submit) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const raw  = new FormData(form);
      const data = {};
      raw.forEach((v, k) => { data[k] = v; });

      submit.disabled    = true;
      submit.textContent = 'Sending\u2026';

      try {
        const res = await fetch('/api/contact', {
          method:  'POST',
          headers: { 'Content-Type': 'application/json' },
          body:    JSON.stringify(data),
        });
        if (res.ok) {
          form.style.display = 'none';
          if (success) success.style.display = 'block';
        } else {
          throw new Error('non-2xx');
        }
      } catch (_) {
        if (error) error.style.display = 'block';
        submit.disabled    = false;
        submit.textContent = 'Send Message';
      }
    });
  }
})();
