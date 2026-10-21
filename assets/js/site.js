/* Always open a page at the top (unless a link points to a section) */
(function () {
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  function top() { if (!location.hash) window.scrollTo(0, 0); }
  top();
  window.addEventListener("load", top);
  window.addEventListener("pageshow", function (e) { if (e.persisted) top(); });
})();

// Scroll reveal: elements with .reveal fade up once as they enter the screen.
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var links = document.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Contact form: opens the visitor's email app with the message filled in.
  var form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var to = form.getAttribute('data-email');
      var subject = 'Portfolio inquiry from ' + (f.get('first') || '') + ' ' + (f.get('last') || '');
      var body = (f.get('message') || '') + '\n\n' + (f.get('first') || '') + ' ' + (f.get('last') || '') + '\n' + (f.get('email') || '');
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject.trim()) + '&body=' + encodeURIComponent(body);
    });
  }

  var y = document.querySelector('#year');
  if (y) y.textContent = new Date().getFullYear();
})();


/* Testimonials carousel arrows */
(function () {
  var track = document.getElementById("t-track");
  if (!track) return;
  var prev = document.querySelector(".t-arrow.prev"), next = document.querySelector(".t-arrow.next");
  function cards() { return Array.prototype.slice.call(track.querySelectorAll(".t-card")); }
  function go(dir) {
    var x = track.scrollLeft, base = track.firstElementChild ? track.firstElementChild.offsetLeft : 0, target = null;
    var list = cards().map(function (c) { return c.offsetLeft - base; });
    if (dir > 0) { for (var i = 0; i < list.length; i++) if (list[i] > x + 8) { target = list[i]; break; } }
    else { for (var k = list.length - 1; k >= 0; k--) if (list[k] < x - 8) { target = list[k]; break; } }
    if (target === null) target = dir > 0 ? track.scrollWidth : 0;
    track.scrollTo({ left: target, behavior: "smooth" });
  }
  function sync() {
    var max = track.scrollWidth - track.clientWidth - 8;
    prev.disabled = track.scrollLeft <= 8;
    next.disabled = track.scrollLeft >= max;
  }
  prev.addEventListener("click", function () { go(-1); });
  next.addEventListener("click", function () { go(1); });
  track.addEventListener("scroll", sync, { passive: true });
  window.addEventListener("resize", sync);
  window.addEventListener("load", sync);
  sync();
})();

// Read-more panels: open the panel a link points to (e.g. "See it" → #storyboard), then scroll to it.
(function () {
  function openTarget() {
    if (!location.hash) return;
    var el = document.getElementById(location.hash.slice(1));
    if (!el) return;
    var d = el.tagName === 'DETAILS' ? el : el.closest('details');
    if (d && !d.open) { d.open = true; setTimeout(function () { el.scrollIntoView({ block: 'start' }); }, 0); }
  }
  window.addEventListener('hashchange', openTarget);
  openTarget();
})();
