/**
 * Text-to-Speech using Web Speech API
 * Speaks translated text in the browser
 */

/** Speak the given text using browser TTS */
function speakText(text, lang) {
    if (!text || !window.speechSynthesis) {
        console.warn('Text-to-speech not supported');
        return;
    }

    // Cancel any ongoing speech
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    if (lang) {
        utterance.lang = lang;
    }

    // Visual feedback on active button
    utterance.onstart = function () {
        document.querySelectorAll('.tts-btn.speaking').forEach(b => b.classList.remove('speaking'));
    };
    utterance.onend = function () {
        document.querySelectorAll('.tts-btn.speaking').forEach(b => b.classList.remove('speaking'));
    };

    window.speechSynthesis.speak(utterance);
}

/** Bind TTS buttons that reference a textarea/input by ID */
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.tts-btn[data-tts-source]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const sourceId = btn.dataset.ttsSource;
            const el = document.getElementById(sourceId);
            if (el && el.value) {
                btn.classList.add('speaking');
                speakText(el.value);
            }
        });
    });
});
