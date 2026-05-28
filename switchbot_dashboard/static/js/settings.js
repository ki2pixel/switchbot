(() => {
  const initSettings = () => {
    const summary = document.getElementById("time_window_days_summary");
    if (!summary) {
      return;
    }

    const checkboxes = Array.from(
      document.querySelectorAll('input[name="time_window_days"]')
    );

    const render = () => {
      const selectedCount = checkboxes.filter((checkbox) => checkbox.checked).length;
      summary.textContent = `${selectedCount} jour(s) sélectionné(s).`;
    };

    checkboxes.forEach((checkbox) => {
      checkbox.addEventListener("change", render);
    });

    render();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initSettings);
  } else {
    initSettings();
  }
})();
