/**
 * Dark/Light theme toggle using Bootstrap 5.3 data-bs-theme
 * Persists preference in localStorage
 */
(function () {
    'use strict';

    const STORAGE_KEY = 'travel-assistant-theme';
    const html = document.documentElement;

    /** Apply theme to document and update icon */
    function setTheme(theme) {
        html.setAttribute('data-bs-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);
        updateIcon(theme);
    }

    /** Update moon/sun icon based on current theme */
    function updateIcon(theme) {
        const icon = document.getElementById('themeIcon');
        if (!icon) return;
        icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
    }

    /** Initialize theme from saved preference or system default */
    function initTheme() {
        const saved = localStorage.getItem(STORAGE_KEY);
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const theme = saved || (prefersDark ? 'dark' : 'light');
        setTheme(theme);
    }

    /** Toggle between dark and light */
    function toggleTheme() {
        const current = html.getAttribute('data-bs-theme') || 'light';
        setTheme(current === 'dark' ? 'light' : 'dark');
    }

    // Initialize on page load
    initTheme();

    // Bind toggle button
    document.addEventListener('DOMContentLoaded', function () {
        const btn = document.getElementById('themeToggle');
        if (btn) {
            btn.addEventListener('click', toggleTheme);
        }
    });

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
        if (!localStorage.getItem(STORAGE_KEY)) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });
})();
