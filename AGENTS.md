# Antigravity Agent Configuration (AGENTS.md)
# This file provides global behavioral instructions to the Antigravity AI coding assistant for the Airbnb Clone project.

<user_rules>
<RULE[project_guidelines]>
- **Component Structure:** Always use functional React components with hooks (useState, useEffect). Avoid class components.
- **Styling:** Strictly match the provided layout, typography, and spacing from the reference URL. Do NOT use TailwindCSS, Material-UI, or Bootstrap. You must use vanilla custom CSS classes.
- **Assets:** Optimize SVG assets by inlining them directly into components to prevent HTTP overhead.
- **Accessibility:** When implementing modals or overlays, always trap focus and ensure `aria-hidden` attributes are toggled appropriately.
- **Behavior:** Prevent body scrolling when full-screen components (like the Photo Tour or Lightbox) are active.
</RULE[project_guidelines]>
</user_rules>
