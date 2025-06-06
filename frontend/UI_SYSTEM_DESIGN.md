# UI System Design: YouTube Video Management Frontend (MVP)

## 1. Introduction

This document outlines the UI System Design for the YouTube Video Management Frontend application. Its purpose is to ensure a consistent, cohesive, and high-quality user experience by providing a shared library of design principles, visual styles, and reusable UI components. This is a living document and will evolve alongside the application.

**Goals:**
*   Promote UI consistency across the application.
*   Accelerate development by providing reusable components.
*   Facilitate collaboration between developers.
*   Ensure a user-friendly and accessible interface.

**Tooling:**
*   **Primary Styling:** Tailwind CSS. Utility-first classes will be predominantly used.
*   **Component Structure:** React 19 components.

## 2. Design Principles

*   **Clarity:** The UI should be clear and easy to understand. Users should always know where they are and what to do next.
*   **Simplicity:** Strive for simplicity in design and interaction. Avoid unnecessary complexity.
*   **Efficiency:** Users should be able to accomplish tasks quickly and with minimal effort.
*   **Consistency:** UI elements and interaction patterns should be consistent throughout the application.
*   **Feedback:** Provide immediate and clear feedback for user actions.
*   **Accessibility (A11y):** Design with accessibility in mind from the start, aiming for WCAG 2.1 AA compliance where feasible for MVP.

## 3. Layout System

*   **Grid:** A flexible grid system will be primarily managed by Tailwind CSS's flexbox and grid utilities.
*   **Spacing:** Consistent spacing will be achieved using Tailwind's spacing scale (e.g., `p-4`, `m-2`). A base unit of 4px (Tailwind's default) is assumed.
    *   Small: 8px (`p-2`)
    *   Medium: 16px (`p-4`)
    *   Large: 24px (`p-6`), 32px (`p-8`)
*   **Responsive Breakpoints:** Utilize Tailwind's default breakpoints:
    *   `sm`: 640px
    *   `md`: 768px
    *   `lg`: 1024px
    *   `xl`: 1280px
    *   `2xl`: 1536px
*   **Page Structure (General):**
    *   **App Layout:** A main layout component (`AppLayout.jsx` by Dev A - TASK-FE-002) will typically include:
        *   **Header:** Contains app title/logo, navigation links (if any beyond context), user authentication status, logout button, YouTube connection status.
        *   **Main Content Area:** Where page-specific content is rendered.
    *   **Page Content:** Pages should generally have a clear title and well-structured content sections. Max width for content areas (e.g., `max-w-7xl mx-auto`) should be used for readability on large screens.

## 4. Typography

*   **Font Family:** System fonts will be used for simplicity in MVP. Tailwind's default sans-serif stack: `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"`.
*   **Font Sizes (Tailwind examples):**
    *   Page Titles (h1): `text-2xl` or `text-3xl`, `font-bold`
    *   Section Titles (h2): `text-xl` or `text-2xl`, `font-semibold`
    *   Sub-Section Titles (h3): `text-lg` or `text-xl`, `font-medium`
    *   Body Text: `text-base`
    *   Small/Helper Text: `text-sm`
*   **Line Height:** Use Tailwind's relative line heights (e.g., `leading-normal`, `leading-relaxed`) for readability.
*   **Color:** Default text color will be a dark gray (e.g., `text-gray-800` or `text-gray-900`). Links will have a distinct color (e.g., `text-blue-600`).

## 5. Color Palette (Basic MVP)

*   **Primary:** A neutral base with a single accent color for calls to action.
    *   `primary-bg`: White (`bg-white`) or Light Gray (`bg-gray-100`) for page backgrounds.
    *   `primary-text`: Dark Gray (`text-gray-900` or `text-gray-800`).
    *   `primary-accent`: Blue (e.g., `bg-blue-600`, `text-blue-600`). Used for primary buttons, links, focus indicators.
*   **Secondary/Neutral:** Grays for borders, disabled states, secondary text.
    *   `border-color`: `border-gray-300`
    *   `disabled-bg`: `bg-gray-200`
    *   `disabled-text`: `text-gray-500`
    *   `secondary-text`: `text-gray-600` or `text-gray-500`
*   **Feedback Colors:**
    *   `success`: Green (e.g., `bg-green-500`, `text-green-700`)
    *   `error`: Red (e.g., `bg-red-500`, `text-red-700`)
    *   `warning`: Yellow/Amber (e.g., `bg-yellow-500`, `text-yellow-700`)
    *   `info`: Blue (can be same as `primary-accent`)
*   **Naming Convention:** Use Tailwind CSS class names directly where possible. For custom color definitions in `tailwind.config.js`, use semantic names (e.g., `primary`, `accent`, `feedback-error`).

## 6. Core UI Components (Atomic Design Approach)

This list is based on identified needs from the `FRONTEND_BACKLOG.md`. Components should be developed in `src/components/common` or feature-specific directories if not broadly reusable. Props should be well-defined using TypeScript interfaces.

### 6.1 Atoms (Basic Building Blocks)

*   **Button:**
    *   Variations: Primary (accent color), Secondary (outline or light gray), Destructive (red), Link-style.
    *   States: Default, Hover, Focus, Disabled.
    *   Props: `onClick`, `type` (button, submit, reset), `disabled`, `isLoading` (shows spinner).
    *   Example Tailwind: `py-2 px-4 rounded font-semibold`. `bg-blue-600 hover:bg-blue-700 text-white` (primary).
*   **Input:**
    *   Types: Text, Email, Password, File.
    *   States: Default, Focus, Disabled, Error.
    *   Props: `value`, `onChange`, `placeholder`, `type`, `disabled`, `hasError`.
    *   Example Tailwind: `border border-gray-300 rounded px-3 py-2 focus:ring-blue-500 focus:border-blue-500`.
*   **Label:**
    *   Associated with form inputs.
    *   Example Tailwind: `block text-sm font-medium text-gray-700 mb-1`.
*   **Icon:**
    *   Use a library like Heroicons or Feather Icons (SVG-based).
    *   Props: `name` (or component itself), `size`, `color`.
*   **Spinner/Loader:**
    *   Indicates loading state.
    *   Variations: Small (for buttons), Medium, Large (for page loads).
    *   Example: Simple SVG spinner or CSS loader.
*   **Thumbnail Placeholder:**
    *   Used when video thumbnail is loading or unavailable.
    *   Example: Gray box with an icon.

### 6.2 Molecules (Simple Combinations of Atoms)

*   **Form Group:**
    *   Combines Label, Input, and optional error message display.
*   **Search Input:** (Future, but good to keep in mind)
    *   Input field with a search icon.
*   **Notification/Toast:**
    *   Displays success, error, warning, or info messages.
    *   Atom: Icon, Text. Molecule: Icon + Text + Dismiss button, within a styled container.
    *   (TASK-FE-013 by Dev C)
*   **Pagination Control:**
    *   Buttons for "Previous", "Next", and possibly page numbers.
    *   (Part of TASK-FE-007 by Dev B)
*   **User Avatar/Badge (Header):**
    *   Displays user initial or generic icon, possibly with a dropdown for logout. (Part of Layout in TASK-FE-002/TASK-FE-005 by Dev A)

### 6.3 Organisms (More Complex Components / Sections)

*   **App Header:**
    *   Contains app title/logo, navigation (if any), YouTube connection status, User Avatar/Logout.
    *   (Layout by Dev A - TASK-FE-002, Connection Status by Dev B - TASK-FE-006)
*   **Signup Form:**
    *   Combination of Form Groups for email, password, and a submit Button.
    *   (TASK-FE-003 by Dev A)
*   **Login Form:**
    *   Similar to Signup Form.
    *   (TASK-FE-004 by Dev A)
*   **Video Card / List Item:**
    *   Displays video thumbnail, title, views, publication date, and links/actions (view details).
    *   (TASK-FE-007 by Dev B)
*   **Video List/Grid:**
    *   Container for multiple Video Cards.
    *   (TASK-FE-007 by Dev B)
*   **Video Detail Display:**
    *   Section displaying all video metadata (title, description, tags, stats etc.).
    *   (TASK-FE-008 by Dev B)
*   **Video Metadata Form (for Edit/Upload):**
    *   A comprehensive form including inputs for title, description, tags, category, privacy status, and potentially file input for upload.
    *   (TASK-FE-009, TASK-FE-010 by Dev C)
*   **Confirmation Modal:**
    *   Generic modal for confirming actions (e.g., delete video). Title, message content, Confirm button, Cancel button.
    *   (TASK-FE-011 by Dev C)

### 6.4 Templates (Page Layouts)

*   **Auth Page Template:** Centered form layout for Login/Signup.
*   **Default Page Template:** App Header, main content area (e.g., for Video List, Video Detail).
*   **Form Page Template:** Layout for dedicated form pages like Upload or Edit (if not using modals).

## 7. Interaction Patterns

*   **Modals:**
    *   Overlay the page content.
    *   Include a clear title, content, action buttons (Confirm, Cancel), and a close button (X icon).
    *   Should be dismissible by clicking outside or pressing Escape key.
*   **Notifications/Toasts:**
    *   Appear in a consistent screen corner (e.g., top-right).
    *   Auto-dismiss after a few seconds, or manually dismissible.
*   **Form Submission:**
    *   Disable submit button and show loading state during submission.
    *   Display success or error messages clearly.
    *   Clear form or redirect on success.

## 8. Accessibility (A11y) Guidelines Specifics

*   **Focus Management:** Ensure logical focus order for keyboard navigation. Modals should trap focus.
*   **ARIA Attributes:** Use ARIA attributes appropriately for custom components or to provide additional context (e.g., `aria-live` for notifications, `aria-labelledby` for modals).
*   **Semantic HTML:** Use HTML5 semantic elements (`<nav>`, `<main>`, `<aside>`, `<article>`, `<section>`) where appropriate.
*   **Keyboard Navigation:** All interactive elements must be operable via keyboard.

## 9. Future Considerations

*   Dark Mode.
*   Theming capabilities.
*   More extensive icon library.
*   Advanced form validation patterns.
*   Animation and micro-interactions.

This UI System Design document provides a foundational guide. Developers should collaborate to evolve and refine it as the application grows. For any new broadly reusable component, consider adding its specification here after discussion.
