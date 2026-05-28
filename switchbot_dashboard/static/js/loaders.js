(() => {
    // ----------------------------------------------------
    // Unified CSRF Validation Interceptors
    // ----------------------------------------------------
    const setupCsrfInterceptors = () => {
        const csrfMethods = ['POST', 'PUT', 'DELETE', 'PATCH'];
        
        // 1. Fetch API Interceptor
        const originalFetch = window.fetch;
        window.fetch = function(input, init) {
            init = init || {};
            const method = init.method ? init.method.toUpperCase() : 'GET';
            
            if (csrfMethods.includes(method)) {
                const tokenMeta = document.querySelector('meta[name="csrf-token"]');
                if (tokenMeta && tokenMeta.content) {
                    init.headers = init.headers || {};
                    if (init.headers instanceof Headers) {
                        if (!init.headers.has('X-CSRFToken')) {
                            init.headers.append('X-CSRFToken', tokenMeta.content);
                        }
                    } else if (Array.isArray(init.headers)) {
                        const hasCsrf = init.headers.some(h => h[0].toLowerCase() === 'x-csrftoken');
                        if (!hasCsrf) {
                            init.headers.push(['X-CSRFToken', tokenMeta.content]);
                        }
                    } else {
                        if (!init.headers['X-CSRFToken'] && !init.headers['x-csrftoken'] && !init.headers['X-CSRF-Token'] && !init.headers['x-csrf-token']) {
                            init.headers['X-CSRFToken'] = tokenMeta.content;
                        }
                    }
                }
            }
            return originalFetch.call(this, input, init);
        };

        // 2. XMLHttpRequest Interceptor
        const originalOpen = XMLHttpRequest.prototype.open;
        XMLHttpRequest.prototype.open = function(method, url, ...args) {
            this._method = method;
            return originalOpen.apply(this, [method, url, ...args]);
        };

        const originalSend = XMLHttpRequest.prototype.send;
        XMLHttpRequest.prototype.send = function(...args) {
            const method = this._method ? this._method.toUpperCase() : 'GET';
            if (csrfMethods.includes(method)) {
                const tokenMeta = document.querySelector('meta[name="csrf-token"]');
                if (tokenMeta && tokenMeta.content) {
                    this.setRequestHeader('X-CSRFToken', tokenMeta.content);
                }
            }
            return originalSend.apply(this, args);
        };
    };

    // Initialize CSRF Interceptors immediately
    setupCsrfInterceptors();

    const LOADER_CLASS = 'sb-loader';
    const LOADER_ACTIVE_CLASS = 'sb-loader--active';
    const LOADER_OVERLAY_CLASS = 'sb-loader-overlay';
    const LOADER_SPINNER_CLASS = 'sb-loader-spinner';
    const GLOBAL_LOADER_ID = 'sb-global-loader';
    const GLOBAL_LOADER_ACTIVE_CLASS = 'sb-global-loader--active';
    const FAILSAFE_TIMEOUT_MS = 15000;
    
    const loaderFailsafes = new WeakMap();
    
    const clearLoaderFailsafe = (element) => {
        if (!element) {
            return;
        }
        const timerId = loaderFailsafes.get(element);
        if (timerId) {
            clearTimeout(timerId);
            loaderFailsafes.delete(element);
        }
    };
    
    const scheduleLoaderFailsafe = (element, cleanupCallback) => {
        if (!element || typeof cleanupCallback !== 'function') {
            return;
        }
        clearLoaderFailsafe(element);
        const timerId = window.setTimeout(() => {
            loaderFailsafes.delete(element);
            cleanupCallback();
        }, FAILSAFE_TIMEOUT_MS);
        loaderFailsafes.set(element, timerId);
    };
    
    const createLoaderOverlay = (element) => {
        const overlay = document.createElement('span');
        overlay.className = LOADER_OVERLAY_CLASS;
        overlay.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('role', 'presentation');
        
        const loaderText = element ? (element.getAttribute('data-loader-text') || 'Chargement...') : 'Chargement...';
        
        const spinner = document.createElement('span');
        spinner.className = LOADER_SPINNER_CLASS;
        spinner.setAttribute('role', 'img');
        spinner.setAttribute('aria-label', loaderText);
        
        overlay.appendChild(spinner);
        return overlay;
    };

    const ensureGlobalLoader = () => {
        let overlay = document.getElementById(GLOBAL_LOADER_ID);
        if (overlay) {
            return overlay;
        }

        overlay = document.createElement('div');
        overlay.id = GLOBAL_LOADER_ID;
        overlay.className = 'sb-global-loader';
        overlay.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('role', 'presentation');

        const spinner = document.createElement('div');
        spinner.className = 'sb-global-loader__spinner';
        spinner.setAttribute('role', 'img');
        spinner.setAttribute('aria-label', 'Chargement...');

        overlay.appendChild(spinner);
        document.body.appendChild(overlay);
        return overlay;
    };

    const showGlobalLoader = () => {
        const overlay = ensureGlobalLoader();
        overlay.classList.add(GLOBAL_LOADER_ACTIVE_CLASS);
        document.body.classList.add('sb-loading');
    };

    const hideGlobalLoader = () => {
        const overlay = document.getElementById(GLOBAL_LOADER_ID);
        if (!overlay) {
            return;
        }
        overlay.classList.remove(GLOBAL_LOADER_ACTIVE_CLASS);
        document.body.classList.remove('sb-loading');
    };
    
    const resetButtonState = (button, originalText) => {
        if (!button) {
            return;
        }
        if (typeof originalText === 'string') {
            button.textContent = originalText;
        }
        if ('disabled' in button) {
            button.disabled = false;
        }
    };
    
    const showLoader = (element) => {
        if (!element || element.classList.contains(LOADER_ACTIVE_CLASS)) {
            return;
        }
        
        element.classList.add(LOADER_ACTIVE_CLASS);
        element.setAttribute('aria-busy', 'true');
        
        const overlay = createLoaderOverlay(element);
        element.style.position = 'relative';
        element.appendChild(overlay);
        
        requestAnimationFrame(() => {
            overlay.style.opacity = '1';
        });
    };
    
    const hideLoader = (element) => {
        if (!element || !element.classList.contains(LOADER_ACTIVE_CLASS)) {
            return;
        }
        
        clearLoaderFailsafe(element);
        element.classList.remove(LOADER_ACTIVE_CLASS);
        element.removeAttribute('aria-busy');
        
        const overlay = element.querySelector(`.${LOADER_OVERLAY_CLASS}`);
        if (overlay) {
            overlay.style.opacity = '0';
            
            setTimeout(() => {
                if (overlay.parentElement) {
                    overlay.parentElement.removeChild(overlay);
                }
            }, 200);
        }
    };
    
    const setupFormLoaders = () => {
        const forms = document.querySelectorAll('form[data-loader]');
        forms.forEach((form) => {
            form.addEventListener('submit', (event) => {
                const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
                if (submitButton && !submitButton.disabled) {
                    event.preventDefault();
                    showGlobalLoader();
                    showLoader(submitButton);
                    
                    const originalText = submitButton.textContent;
                    const loaderText = submitButton.getAttribute('data-loader-text') || form.getAttribute('data-loader-text') || 'Chargement...';
                    submitButton.textContent = loaderText;
                    submitButton.disabled = true;
                    
                    setTimeout(() => {
                        form.submit();
                    }, 1000);

                    const finalizeSubmission = () => {
                        hideGlobalLoader();
                        hideLoader(submitButton);
                        resetButtonState(submitButton, originalText);
                    };

                    setTimeout(() => {
                        finalizeSubmission();
                        clearLoaderFailsafe(submitButton);
                    }, 10000);

                    scheduleLoaderFailsafe(submitButton, finalizeSubmission);
                }
            });
        });
    };
    
    const setupButtonLoaders = () => {
        document.querySelectorAll('button[data-loader]').forEach(button => {
            button.addEventListener('click', (event) => {
                if (button.disabled) {
                    event.preventDefault();
                    return;
                }
                
                showLoader(button);
                
                const originalText = button.textContent;
                const loaderText = button.getAttribute('data-loader-text') || 'Chargement...';
                button.textContent = loaderText;
                button.disabled = true;

                const finalizeAction = () => {
                    hideLoader(button);
                    resetButtonState(button, originalText);
                };
                
                setTimeout(() => {
                    finalizeAction();
                    clearLoaderFailsafe(button);
                }, 3000);

                scheduleLoaderFailsafe(button, () => {
                    hideGlobalLoader();
                    finalizeAction();
                });
            });
        });
    };
    
    const setupNavigationLoaders = () => {
        document.querySelectorAll('a[data-loader]').forEach((link) => {
            link.addEventListener('click', (event) => {
                if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) {
                    return;
                }

                const href = link.getAttribute('href') || '';
                if (!href || href.startsWith('#') || href.startsWith('javascript:')) {
                    return;
                }

                event.preventDefault();
                showGlobalLoader();
                showLoader(link);

                scheduleLoaderFailsafe(link, () => {
                    hideGlobalLoader();
                    hideLoader(link);
                });

                setTimeout(() => {
                    if (window.SwitchBotRouter && typeof window.SwitchBotRouter.navigate === 'function') {
                        window.SwitchBotRouter.navigate(href, link);
                    } else {
                        window.location.href = href;
                    }
                }, 150);
            });
        });
    };
    
    document.addEventListener('DOMContentLoaded', () => {
        ensureGlobalLoader();
        hideGlobalLoader();
        setupFormLoaders();
        setupButtonLoaders();
        setupNavigationLoaders();
        
        window.SwitchBotLoaders = {
            show: showLoader,
            hide: hideLoader,
            showGlobal: showGlobalLoader,
            hideGlobal: hideGlobalLoader,
            scheduleFailsafe: scheduleLoaderFailsafe,
            clearFailsafe: clearLoaderFailsafe,
            failsafeDelayMs: FAILSAFE_TIMEOUT_MS,
        };
    });
})();
