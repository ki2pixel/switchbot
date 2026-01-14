(() => {
    const LOADER_CLASS = 'sb-loader';
    const LOADER_ACTIVE_CLASS = 'sb-loader--active';
    const LOADER_OVERLAY_CLASS = 'sb-loader-overlay';
    const LOADER_SPINNER_CLASS = 'sb-loader-spinner';
    const GLOBAL_LOADER_ID = 'sb-global-loader';
    const GLOBAL_LOADER_ACTIVE_CLASS = 'sb-global-loader--active';
    
    const createLoaderOverlay = () => {
        const overlay = document.createElement('span');
        overlay.className = LOADER_OVERLAY_CLASS;
        overlay.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('role', 'presentation');
        
        const spinner = document.createElement('span');
        spinner.className = LOADER_SPINNER_CLASS;
        spinner.setAttribute('role', 'img');
        spinner.setAttribute('aria-label', 'Chargement...');
        
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
    
    const showLoader = (element) => {
        if (!element || element.classList.contains(LOADER_ACTIVE_CLASS)) {
            return;
        }
        
        element.classList.add(LOADER_ACTIVE_CLASS);
        element.setAttribute('aria-busy', 'true');
        
        const overlay = createLoaderOverlay();
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
                    submitButton.textContent = 'Chargement...';
                    submitButton.disabled = true;
                    
                    setTimeout(() => {
                        form.submit();
                    }, 1000);
                    setTimeout(() => {
                        hideGlobalLoader();
                        hideLoader(submitButton);
                        submitButton.textContent = originalText;
                        submitButton.disabled = false;
                    }, 10000);
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
                button.textContent = 'Chargement...';
                button.disabled = true;
                
                setTimeout(() => {
                    hideLoader(button);
                    button.textContent = originalText;
                    button.disabled = false;
                }, 3000);
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
                setTimeout(() => {
                    window.location.href = href;
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
        };
    });
})();
