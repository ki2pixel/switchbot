document.addEventListener("click", async (event) => {
  const button = event.target.closest(".btn-copy");
  if (!button) {
    return;
  }

  const value = button.getAttribute("data-copy");
  if (!value) {
    return;
  }

  const showFeedback = (message) => {
    const original = button.textContent;
    button.textContent = message;
    button.setAttribute("aria-live", "assertive");
    setTimeout(() => {
      button.textContent = original;
      button.removeAttribute("aria-live");
    }, 1800);
  };

  try {
    if (!navigator.clipboard) {
      throw new Error("Clipboard API unavailable");
    }

    await navigator.clipboard.writeText(value);
    showFeedback("Copié ✓");
  } catch (err) {
    console.warn("Clipboard API unavailable, using fallback", err);
    try {
      const textarea = document.createElement("textarea");
      textarea.value = value;
      textarea.setAttribute("readonly", "");
      textarea.style.position = "absolute";
      textarea.style.left = "-9999px";
      document.body.appendChild(textarea);
      textarea.select();
      const success = document.execCommand("copy");
      document.body.removeChild(textarea);
      if (success) {
        showFeedback("Copié ✓ (compatibilité)");
        return;
      }
      throw new Error("Fallback copy failed");
    } catch (fallbackError) {
      console.error("Clipboard copy failed", fallbackError);
      showFeedback("Copie impossible");
    }
  }
});
