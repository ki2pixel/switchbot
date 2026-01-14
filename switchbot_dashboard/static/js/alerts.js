(() => {
  const DISMISS_CLASS = "alert-dismissed";

  const dismissAlert = (alertElement) => {
    if (!alertElement || alertElement.classList.contains(DISMISS_CLASS)) {
      return;
    }

    alertElement.classList.add(DISMISS_CLASS);
    const removeAfterTransition = () => {
      alertElement.removeEventListener("transitionend", removeAfterTransition);
      if (alertElement.parentElement) {
        alertElement.parentElement.removeChild(alertElement);
      }
    };

    alertElement.addEventListener("transitionend", removeAfterTransition);
    window.setTimeout(removeAfterTransition, 600);
  };

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-auto-dismiss]").forEach((alertElement) => {
      const timeout = Number(alertElement.dataset.autoDismiss) || 0;
      if (timeout <= 0) {
        return;
      }

      window.setTimeout(() => dismissAlert(alertElement), timeout);
    });
  });
})();
