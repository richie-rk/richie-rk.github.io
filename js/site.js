// Progressive enhancement only: every page reads, navigates and looks right without this file.
(function () {
  'use strict';

  var root = document.documentElement;

  // Keep scroll-padding equal to the real header height. The CSS value assumes
  // one row; text zoom or unusual fonts can wrap the header onto two.
  var header = document.querySelector('.site-header');
  if (header && window.ResizeObserver) {
    new ResizeObserver(function () {
      root.style.setProperty('--header-offset', header.offsetHeight + 'px');
    }).observe(header);
  }

  // Copying. data-copy holds the text, or data-copy-from points at an element to
  // copy. One shared live region announces the result to screen readers.
  var status = document.createElement('div');
  status.className = 'visually-hidden';
  status.setAttribute('role', 'status');
  document.body.appendChild(status);

  // Email addresses are mailto links without JS. With JS they become real
  // buttons that copy the address; the "Open in…" buttons still open a draft.
  // The hidden prefix keeps the visible address inside the accessible name.
  document.querySelectorAll('a.email-copy').forEach(function (link) {
    var button = document.createElement('button');
    button.type = 'button';
    button.className = link.className;
    button.setAttribute('data-copy', link.getAttribute('data-copy'));
    var prefix = document.createElement('span');
    prefix.className = 'visually-hidden';
    prefix.textContent = 'Copy email address ';
    button.appendChild(prefix);
    while (link.firstChild) button.appendChild(link.firstChild);
    link.parentNode.replaceChild(button, link);
  });

  // Older browsers and some in-app webviews lack the Clipboard API, or reject it.
  // The textarea fallback puts focus back where it was, so keyboard users keep their place.
  var legacyCopy = function (text) {
    return new Promise(function (resolve, reject) {
      var previous = document.activeElement;
      var area = document.createElement('textarea');
      area.value = text;
      area.setAttribute('readonly', '');
      area.style.position = 'fixed';
      area.style.top = '0';
      area.style.opacity = '0';
      document.body.appendChild(area);
      area.select();
      try { document.execCommand('copy') ? resolve() : reject(); } catch (e) { reject(e); }
      document.body.removeChild(area);
      if (previous && previous.focus) previous.focus({ preventScroll: true });
    });
  };
  var copyText = function (text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).catch(function () { return legacyCopy(text); });
    }
    return legacyCopy(text);
  };
  document.querySelectorAll('button[data-copy], button[data-copy-from]').forEach(function (button) {
    // Buttons with a .copy-label swap that text; the email buttons show the state
    // through their icon (data-state drives the CSS).
    var labelEl = button.querySelector('.copy-label');
    var label = labelEl && labelEl.textContent;
    var timer;
    var report = function (state, shown, spoken) {
      button.setAttribute('data-state', state);
      if (labelEl) labelEl.textContent = shown;
      status.textContent = spoken;
      clearTimeout(timer);
      timer = setTimeout(function () {
        button.removeAttribute('data-state');
        if (labelEl) labelEl.textContent = label;
        status.textContent = '';
      }, 1600);
    };
    button.addEventListener('click', function () {
      var from = button.getAttribute('data-copy-from');
      var source = from && document.querySelector(from);
      var text = source ? source.innerText : button.getAttribute('data-copy');
      copyText(text).then(function () {
        report('copied', 'Copied', 'Copied to the clipboard');
      }, function () {
        report('failed', 'Copy failed', labelEl ? 'Copying failed. Select the text and copy it instead.' : 'Copying failed. The address is ' + text);
      });
    });
  });

  // "Also shipped" folds on phones only. From 48rem the list is meant to be
  // open, so open it whenever the window is or becomes that wide (a phone
  // turned sideways, even before this script loaded).
  var fold = document.querySelector('.ledger-fold');
  var wide = window.matchMedia && window.matchMedia('(min-width: 48rem)');
  if (fold && wide) {
    var openIfWide = function () { if (wide.matches) fold.open = true; };
    openIfWide();
    if (wide.addEventListener) wide.addEventListener('change', openIfWide);
  }

  // Theme. The inline <head> script applies any saved choice before first paint
  // and adds .js, which reveals the toggle through CSS. Without light-dark()
  // support the page is always dark.
  var canTheme = !!(window.CSS && CSS.supports && CSS.supports('color', 'light-dark(#000, #fff)'));

  // Keep the browser UI colour in step with the page. With no explicit choice
  // in a supporting browser, the media-queried theme-color metas already match.
  var syncThemeColor = function () {
    if (canTheme && !root.dataset.theme) return;
    var bg = getComputedStyle(document.body).backgroundColor;
    document.querySelectorAll('meta[name="theme-color"]').forEach(function (meta) {
      meta.setAttribute('content', bg);
    });
  };
  syncThemeColor();

  var toggle = document.querySelector('.theme-toggle');
  if (!toggle || !canTheme || !window.matchMedia) return;

  var prefersLight = window.matchMedia('(prefers-color-scheme: light)');

  var current = function () {
    return root.dataset.theme || (prefersLight.matches ? 'light' : 'dark');
  };

  var sync = function () {
    toggle.setAttribute('aria-pressed', String(current() === 'dark'));
    syncThemeColor();
  };

  // Re-read the saved choice. The head script doesn't re-run when a page comes
  // back from the back/forward cache, and other tabs may have changed it.
  var applySaved = function () {
    var saved = null;
    try { saved = localStorage.getItem('theme'); } catch (e) { /* storage blocked */ }
    if (saved === 'light' || saved === 'dark') root.dataset.theme = saved;
    else delete root.dataset.theme;
    sync();
  };

  sync();

  toggle.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) { /* private mode: the choice lasts for this page only */ }
    sync();
  });

  if (prefersLight.addEventListener) prefersLight.addEventListener('change', sync);
  window.addEventListener('pageshow', function (event) { if (event.persisted) applySaved(); });
  window.addEventListener('storage', function (event) { if (event.key === 'theme') applySaved(); });
})();
