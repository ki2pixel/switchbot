"""Tests pour le système de loaders frontend."""

import pytest
import os
from bs4 import BeautifulSoup


def test_loader_css_classes_present():
    """Vérifie que les classes CSS des loaders sont présentes dans theme.css."""
    theme_css_path = os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'switchbot_dashboard', 
        'static', 
        'css', 
        'theme.css'
    )
    
    with open(theme_css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Vérifier les classes essentielles
    required_classes = [
        '.sb-loader-overlay',
        '.sb-loader-spinner',
        '.sb-loader--active',
        '@keyframes sb-spin'
    ]
    
    for css_class in required_classes:
        assert css_class in css_content, f"La classe CSS {css_class} doit être présente"


def test_loader_js_file_exists():
    """Vérifie que le fichier loaders.js existe et contient les fonctions requises."""
    loaders_js_path = os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'switchbot_dashboard', 
        'static', 
        'js', 
        'loaders.js'
    )
    
    assert os.path.exists(loaders_js_path), "Le fichier loaders.js doit exister"
    
    with open(loaders_js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Vérifier les fonctions essentielles
    required_functions = [
        'showLoader',
        'hideLoader',
        'setupFormLoaders',
        'setupButtonLoaders',
        'SwitchBotLoaders'
    ]
    
    for func in required_functions:
        assert func in js_content, f"La fonction {func} doit être présente dans loaders.js"


def test_loader_js_has_failsafe_timeout():
    """Vérifie la présence du failsafe 15s dans loaders.js."""
    loaders_js_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'switchbot_dashboard',
        'static',
        'js',
        'loaders.js'
    )

    with open(loaders_js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()

    assert 'FAILSAFE_TIMEOUT_MS' in js_content, "Le failsafe 15s doit être défini dans loaders.js"
    assert 'scheduleFailsafe' in js_content, "L’API SwitchBotLoaders doit exposer scheduleFailsafe"


def test_templates_have_data_loader_attributes():
    """Vérifie que les templates HTML ont les attributs data-loader."""
    templates_dir = os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'switchbot_dashboard', 
        'templates'
    )
    
    templates_to_check = ['index.html', 'settings.html', 'quota.html']
    
    for template_name in templates_to_check:
        template_path = os.path.join(templates_dir, template_name)
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Vérifier la présence du script loaders.js
        assert 'loaders.js' in template_content, f"{template_name} doit inclure loaders.js"
        
        # Vérifier la présence d'au moins un attribut data-loader
        assert 'data-loader' in template_content, f"{template_name} doit avoir des éléments avec data-loader"


def test_index_template_structure():
    """Vérifie la structure spécifique du template index.html."""
    template_path = os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'switchbot_dashboard', 
        'templates',
        'index.html'
    )
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    soup = BeautifulSoup(template_content, 'html.parser')
    
    # Vérifier les formulaires POST avec data-loader
    post_forms = soup.find_all('form', method='post')
    assert len(post_forms) > 0, "index.html doit avoir des formulaires POST"
    
    for form in post_forms:
        assert form.has_attr('data-loader'), "Formulaire dans index.html doit avoir data-loader"


def test_all_post_forms_have_data_loader():
    """Every POST form in every page template must be wired to loaders.js."""
    templates_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        'switchbot_dashboard',
        'templates',
    )

    for filename in sorted(os.listdir(templates_dir)):
        if not filename.endswith('.html') or filename.startswith('_'):
            continue
        with open(os.path.join(templates_dir, filename), 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        for form in soup.find_all('form', method=lambda m: m and m.lower() == 'post'):
            assert form.has_attr('data-loader'), (
                f"POST form in {filename} is missing data-loader: "
                f"{form.get('action')}"
            )


def test_performance_documentation_exists():
    """Vérifie que la documentation des optimisations existe."""
    doc_path = os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'docs',
        'frontend-performance.md'
    )
    
    assert os.path.exists(doc_path), "La documentation frontend-performance.md doit exister"
    
    with open(doc_path, 'r', encoding='utf-8') as f:
        doc_content = f.read()
    
    # Vérifier les sections importantes
    required_sections = [
        'Optimisations Frontend',
        'Système de loaders',
        'Accessibilité',
        'Performance technique'
    ]
    
    for section in required_sections:
        assert section in doc_content, f"La documentation doit contenir la section '{section}'"


def test_csrf_interceptor_checks_same_origin():
    """Le token CSRF ne doit jamais partir vers une origine externe."""
    loaders_js_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'switchbot_dashboard',
        'static',
        'js',
        'loaders.js'
    )

    with open(loaders_js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Given/Then: helper and both interceptor paths are guarded
    assert 'isSameOrigin' in js_content
    assert 'isSameOrigin(input)' in js_content
    assert 'isSameOrigin(url)' in js_content
    assert 'this._csrfSameOrigin' in js_content


if __name__ == '__main__':
    pytest.main([__file__])
