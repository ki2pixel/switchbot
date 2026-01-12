document.addEventListener("click", async (event) => {
  const button = event.target.closest(".btn-copy");
  if (!button) {
    return;
  }

  const value = button.getAttribute("data-copy");
  if (!value) {
    return;
  }

  try {
    if (!navigator.clipboard) {
      throw new Error("Clipboard API unavailable");
    }

    await navigator.clipboard.writeText(value);
    const original = button.textContent;
    button.textContent = "Copié ✓";
    button.setAttribute("aria-live", "assertive");
    setTimeout(() => {
      button.textContent = original;
      button.removeAttribute("aria-live");
    }, 1800);
  } catch (err) {
    console.error("Clipboard copy failed", err);
  }
});
