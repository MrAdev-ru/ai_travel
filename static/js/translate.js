/**
 * Translation page interactions:
 * - Language swap
 * - Auto language detection
 * - Clear form
 */
(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        const sourceLang = document.getElementById('sourceLanguage');
        const targetLang = document.getElementById('targetLanguage');
        const sourceText = document.getElementById('sourceText');
        const translatedText = document.getElementById('translatedText');
        const detectBtn = document.getElementById('detectLangBtn');
        const swapBtn = document.getElementById('swapLanguages');
        const clearBtn = document.getElementById('clearBtn');
        const detectedLangEl = document.getElementById('detectedLang');

        // Swap source and target languages
        if (swapBtn && sourceLang && targetLang) {
            swapBtn.addEventListener('click', function () {
                const srcVal = sourceLang.value;
                const tgtVal = targetLang.value;

                // Swap text content too
                if (sourceText && translatedText) {
                    const tmp = sourceText.value;
                    sourceText.value = translatedText.value;
                    translatedText.value = tmp;
                }

                if (srcVal === 'auto') {
                    sourceLang.value = tgtVal;
                    targetLang.value = 'en';
                } else {
                    sourceLang.value = tgtVal;
                    targetLang.value = srcVal;
                }
            });
        }

        // Detect language via AJAX
        if (detectBtn && sourceText) {
            detectBtn.addEventListener('click', async function () {
                const text = sourceText.value.trim();
                if (!text) return;

                detectBtn.disabled = true;
                detectBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';

                try {
                    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                    const response = await fetch('/translate/api/detect/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrfToken,
                            'X-Requested-With': 'XMLHttpRequest',
                        },
                        body: JSON.stringify({ text: text }),
                    });
                    const data = await response.json();

                    if (data.language && sourceLang) {
                        // Set detected language in dropdown if option exists
                        const option = sourceLang.querySelector(`option[value="${data.language}"]`);
                        if (option) {
                            sourceLang.value = data.language;
                        }
                        if (detectedLangEl) {
                            const confidence = Math.round((data.confidence || 0) * 100);
                            detectedLangEl.textContent = `Detected: ${data.language.toUpperCase()} (${confidence}% confidence)`;
                        }
                    }
                } catch (err) {
                    console.error('Detection failed:', err);
                } finally {
                    detectBtn.disabled = false;
                    detectBtn.innerHTML = '<i class="bi bi-search"></i> Detect';
                }
            });
        }

        // Clear form
        if (clearBtn) {
            clearBtn.addEventListener('click', function () {
                if (sourceText) sourceText.value = '';
                if (translatedText) translatedText.value = '';
                if (detectedLangEl) detectedLangEl.textContent = '';
            });
        }
    });
})();
