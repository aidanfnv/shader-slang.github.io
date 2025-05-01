// Read the Docs integration snippet
// https://docs.readthedocs.com/platform/stable/addons.html#integrate-with-search-as-you-type

// Furo theme's search input selector
const selector = "input.sidebar-search";

document.addEventListener("DOMContentLoaded", function(event) {
    const searchInput = document.querySelector(selector);
    if (searchInput) {
        // Trigger Read the Docs' search addon when the theme's input is clicked
        searchInput.addEventListener("click", (e) => {
            // Prevent the theme's default behavior if any (though Furo might not have one on click)
            e.preventDefault(); 
            const event = new CustomEvent("readthedocs-search-show");
            document.dispatchEvent(event);
        });
        
        // Also trigger on Enter key press within the input
        searchInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault(); // Prevent potential form submission
                const event = new CustomEvent("readthedocs-search-show");
                document.dispatchEvent(event);
            }
        });
    } else {
        console.warn("RTD Search Trigger: Could not find Furo search input with selector:", selector);
    }
}); 