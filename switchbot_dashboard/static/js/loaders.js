(() => {
    const LOADER_CLASS = 'sb-loader';
    const LOADER_ACTIVE_CLASS = 'sb-loader--active';
    const LOADER_OVERLAY_CLASS = 'sb-loader-overlay';
    const LOADER_SPINNER_CLASS = 'sb-loader-spinner';
    
    const createLoaderOverlay = () => {
        const overlay = document.createElement('div');
        overlay.className = LOADER_OVERLAY_CLASS;
        overlay.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('role', 'presentation');
        
        const spinner = document.createElement('div');
        spinner.className = LOADER_SPINNER_CLASS;
        spinner.setAttribute('role', 'img');
        spinner.setAttribute('aria-label', 'Chargement...');
        
        overlay.appendChild(spinner);
        return overlay;
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
        document.querySelectorAll('form[data-loader]').forEach(form => {
            form.addEventListener('submit', (event) => {
                const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
                if (submitButton && !submitButton.disabled) {
                    showLoader(submitButton);
                    
                    const originalText = submitButton.textContent;
                    submitButton.textContent = 'Chargement...';
                    submitButton.disabled = true;
                    
                    setTimeout(() => {
                        hideLoader(submitButton);
                        submitButton.textContent = originalText;
                        submitButton.disabled = false;
                    }, 5000);
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
        document.querySelectorAll('a[data-loader]').forEach(link => {
            link.addEventListener('click', (event) => {
                showLoader(link);
                
                const originalText = link.textContent;
                link.textContent = 'Chargement...';
                
                setTimeout(() => {
                    hideLoader(link);
                    link.textContent = originalText;
                }, 2000);
            });
        });
    };
    
    document.addEventListener('DOMContentLoaded', () => {
        setupFormLoaders();
        setupButtonLoaders();
        setupNavigationLoaders();
        
        window.SwitchBotLoaders = {
            show: showLoader,
            hide: hideLoader
        };
    });
})();
