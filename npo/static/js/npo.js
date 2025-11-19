/**
 * @file npo.js
 * @description Global JS for NPO site
 * @version 1.0.0
 * @author Jobet P. Casquejo
 * @date 2025-11-19
 */

/**
 * Global frontend application class
 */
class SiteApp {
    /**
     * Create a SiteApp instance
     * @param {Object} config - Configuration
     * @param {number} [config.toastDuration=4000] - Toast display duration in ms
     * @param {string} [config.toastPosition='top-right'] - Toast position: top-right, top-left, bottom-right, bottom-left
     */
    constructor(config = {}) {
        this.config = Object.assign({
            toastDuration: 4000,
            toastPosition: 'top-right'
        }, config);

        // Containers
        this.$toastsContainer = $('#toasts-container');
        if (!this.$toastsContainer.length) {
            this.$toastsContainer = $('<div/>', { id: 'toasts-container' }).appendTo('body');
        }

        // Toast management
        this.activeToasts = [];
    }

    /**
     * Initialize AJAX form submissions
     */
    initForms() {
        const self = this;
        $('form.ajax-form').each(function () {
            const $form = $(this);

            $form.on('submit', function (e) {
                e.preventDefault();
                $.ajax({
                    url: $form.attr('action'),
                    type: $form.attr('method') || 'POST',
                    data: $form.serialize(),
                    dataType: 'json',
                    success: function (response) {
                        if (response.success) {
                            self.showToast('success', response.message || 'Form submitted successfully.');
                            $form[0].reset();
                            $form.find('.is-error').removeClass('is-error');
                        } else {
                            self.showToast('error', response.message || 'Form submission failed.');
                            if (response.errors) {
                                for (const field in response.errors) {
                                    $form.find(`[name="${field}"]`).addClass('is-error');
                                }
                            }
                        }
                    },
                    error: function (xhr, status, error) {
                        let message = `AJAX Erro: ${status} - ${error}`;
                        if(xhr.responseJSON && xhr.responseJSON.message) {
                            message = xhr.responseJSON.message;
                        } else if (xhr.responseText) {
                            message += `\nResponse: ${xhr.responseText}`;
                        }
                        self.showToast('error', message);
                    }
                });
            });
        });
    }

    /**
     * Show a toast notification
     * @param {string} type - 'success', 'error', 'info'
     * @param {string} message - Text to display
     */
    showToast(type = 'info', message = '') {
        const $toast = $('<div/>', { class: `toast toast-${type}`, text: message }).appendTo(this.$toastsContainer);

        const colors = {
            success: 'var(--success-color)',
            error: 'var(--error-color)',
            info: 'var(--info-color)'
        };

        $toast.css({
            'background-color': colors[type] || colors.info,
            'color': 'var(--text-inverse)',
            'padding': 'var(--space-md)',
            'border-radius': 'var(--border-radius-md)',
            'box-shadow': 'var(--shadow-md)',
            'margin-bottom': 'var(--space-sm)',
            'opacity': 0,
            'transition': `opacity var(--transition-speed) var(--transition-ease), transform var(--transition-speed) var(--transition-ease)`,
            'transform': 'translateY(-10px)',
            'pointer-events': 'auto'
        });

        // Animate in
        requestAnimationFrame(() => {
            $toast.css({ opacity: 1, transform: 'translateY(0)' });
        });

        // Remove after duration
        const duration = this.config.toastDuration;
        const timeout = setTimeout(() => this.removeToast($toast), duration);

        // Pause on hover
        $toast.hover(() => clearTimeout(timeout), () => {
            setTimeout(() => this.removeToast($toast), duration / 2);
        });

        this.activeToasts.push($toast);
    }

    /**
     * Remove a toast notification
     * @param {jQuery} $toast - Toast element
     */
    removeToast($toast) {
        $toast.css({ opacity: 0, transform: 'translateY(-10px)' });
        setTimeout(() => $toast.remove(), 400);
        this.activeToasts = this.activeToasts.filter(t => t[0] !== $toast[0]);
    }

    /**
     * Open a modal window
     * @param {jQuery} $modal - Modal element
     */
    openModal($modal) {
        $modal.addClass('is-active');
        $('body').addClass('is-clipped');
        this.trapFocus($modal);
    }

    /**
     * Close a modal window
     * @param {jQuery} $modal - Modal element
     */
    closeModal($modal) {
        $modal.removeClass('is-active');
        $('body').removeClass('is-clipped');
    }

    /**
     * Trap focus inside a modal for accessibility
     * @param {jQuery} $modal - Modal element
     */
    trapFocus($modal) {
        const focusable = $modal.find('a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])');
        const first = focusable.first();
        const last = focusable.last();

        $modal.on('keydown', function (e) {
            if (e.key === 'Tab') {
                if (e.shiftKey) {
                    if (document.activeElement === first[0]) { e.preventDefault(); last.focus(); }
                } else {
                    if (document.activeElement === last[0]) { e.preventDefault(); first.focus(); }
                }
            }
            if (e.key === 'Escape') {
                $modal.removeClass('is-active');
                $('body').removeClass('is-clipped');
            }
        });
    }

    /**
     * Utility: debounce a function
     * @param {Function} func - Function to debounce
     * @param {number} wait - Wait time in ms
     * @returns {Function} Debounced function
     */
    debounce(func, wait = 100) {
        let timeout;
        return function (...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }
}

/* --------------------------
   Initialize global SiteApp
--------------------------- */
$(document).ready(() => {
    const site = new SiteApp({ toastDuration: 4000, toastPosition: 'top-right' });
    window.site = site;
    site.initForms();
});