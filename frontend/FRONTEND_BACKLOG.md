# Frontend Backlog: YouTube Video Management App (MVP)

## Task Distribution for 3 Developers

This backlog is organized to distribute work among three developers (Developer A, Developer B, Developer C) for the MVP. The goal is to assign cohesive features or sections to each developer to promote focused work and minimize file conflicts. Adherence to `frontend/UI_SYSTEM_DESIGN.md` is expected for all UI development.

**General Responsibilities:**
*   **Shared Components/Utils:** Components intended for broad reuse should be placed in `src/components/common` and align with `UI_SYSTEM_DESIGN.md`.
*   **Styling:** Tailwind CSS, following visual guidelines in `UI_SYSTEM_DESIGN.md`.
*   **API Services:** Services in `src/services`.
*   **Type Definitions:** Shared types in `src/types`.
*   **Testing:** Each developer is responsible for tests for their features.

---

## Developer A: Foundations & Authentication

**Focus:** Core application setup, routing, user authentication flow, and managing authentication state, using components from `UI_SYSTEM_DESIGN.md`.

*   **TASK-FE-001 (A):** Initialize Frontend Project
    *   **Description:** Set up a new React 19 project using Vite.
    *   **Details:**
        *   Install and configure Vite.
        *   Set up React 19.
        *   Integrate Tailwind CSS for styling.
        *   Establish basic project structure (e.g., `src/components`, `src/pages`, `src/services`, `src/hooks`, `src/store` or `src/contexts`, `src/utils`, `src/types`).
    *   **Tech Stack:** React 19, Vite, Tailwind CSS.
    *   **Architecture:** Follow Clean Architecture principles. Plan for testability. Project structure should accommodate common components as per UI System Design (e.g. `src/components/common/Button.jsx`).
    *   **Deliverables:** Basic working project structure, build configuration.
    *   **Acceptance Criteria:**
        *   1. Project can be initialized using `npm create vite@latest` (or similar) with React template.
        *   2. React 19 is specified in `package.json` and loads correctly.
        *   3. Tailwind CSS is configured and basic utility classes can be applied to components.
        *   4. Project includes directories: `src/components`, `src/pages`, `src/services`, `src/hooks`, `src/contexts` (or `src/store`), `src/utils`, `src/types`.
        *   5. Basic "Hello World" or similar component renders on the main page.
        *   6. Project can be built using `npm run build` and served using `npm run preview` without errors.
        *   7. ESLint and Prettier are configured for code linting and formatting.
        *   8. Vitest (or chosen test runner) is configured and a sample test passes.

*   **TASK-FE-002 (A):** Implement Routing & App Layout
    *   **Description:** Set up client-side routing and the main `AppLayout` component.
    *   **Details:**
        *   Define routes for authentication pages (Login, Signup), video listing (`/videos`), video details (`/videos/:id`), video upload (`/upload`), video edit (`/videos/:id/edit`).
        *   Implement protected routes that require authentication for video-related pages.
        *   Implement the `AppLayout` organism as per `UI_SYSTEM_DESIGN.md`, including placeholders for `App Header` content like navigation, user status, and logout.
    *   **Tech Stack:** React Router.
    *   **Depends on:** TASK-FE-001 (A)
    *   **Deliverables:** Router configuration, protected route mechanism, `AppLayout` component.
    *   **Acceptance Criteria:**
        *   1. Navigating to `/login` renders the Login page (placeholder initially).
        *   2. Navigating to `/signup` renders the Signup page (placeholder initially).
        *   3. Navigating to `/videos` when unauthenticated redirects to `/login`.
        *   4. Navigating to `/videos` when authenticated renders the Video List page (placeholder initially).
        *   5. Navigating to `/videos/:id` when authenticated renders Video Detail page (placeholder).
        *   6. Navigating to `/upload` when authenticated renders Upload Video page (placeholder).
        *   7. Navigating to `/videos/:id/edit` when authenticated renders Edit Video page (placeholder).
        *   8. A basic `AppLayout` organism exists, containing a header (e.g., with app title) and a main content area where page components are rendered.
        *   9. Attempting to access a protected route without authentication redirects to the login page.

*   **TASK-FE-003 (A):** Signup Page
    *   **Description:** Create a UI for user registration.
    *   **Mock API Interaction:**
        *   **Endpoint:** `POST /api/v1/auth/signup`
        *   **Request DTO:** `{ email: string, password: string }`
        *   **Response DTO (Success 201):** `{ message: string }`
        *   **Response DTO (Error 400):** `{ error: string }`
    *   **Details:** Implement using `Form Group` molecules for inputs and a primary `Button` atom for submission, all within a `Signup Form` organism. Basic client-side validation.
    *   **Tech Stack:** React 19, Tailwind CSS.
    *   **Architecture:** `SignupPage` (page template), `SignupForm` (organism), `AuthService`. Utilizes `Input`, `Label`, `Button` atoms.
    *   **Depends on:** TASK-FE-001 (A), TASK-FE-002 (A)
    *   **Deliverables:** Signup page UI and functionality using defined components.
    *   **Acceptance Criteria:**
        *   1. Signup page is accessible via the `/signup` route.
        *   2. Form contains input fields for 'Email' and 'Password', and a 'Sign Up' button.
        *   3. Basic client-side validation: email field requires a valid email format; password field requires a minimum length (e.g., 6 characters). Validation messages are shown.
        *   4. On valid submission, an API call is made to `POST /api/v1/auth/signup` with email and password.
        *   5. On successful API response (201), a success message is displayed (e.g., "Signup successful! Please login.").
        *   6. On API error response (e.g., 400 for existing email), an appropriate error message is displayed.
        *   7. Loading state is indicated during API call.

*   **TASK-FE-004 (A):** Login Page & Auth State Management
    *   **Description:** Create a UI for user login and set up global authentication state.
    *   **Mock API Interaction:**
        *   **Endpoint:** `POST /api/v1/auth/login`
        *   **Request DTO:** `{ email: string, password: string }`
        *   **Response DTO (Success 200):** `{ message: string }` (Session managed by cookie)
        *   **Response DTO (Error 401):** `{ error: string }`
    *   **Details:** Implement using `Form Group` molecules and a primary `Button` atom within a `Login Form` organism. On successful login, update global auth state and redirect.
    *   **Tech Stack:** React 19, Tailwind CSS.
    *   **Architecture:** `LoginPage` (page template), `LoginForm` (organism), `AuthService`, global `AuthContext`. Utilizes `Input`, `Label`, `Button` atoms.
    *   **Depends on:** TASK-FE-001 (A), TASK-FE-002 (A)
    *   **Deliverables:** Login page UI, login functionality, global auth state management.
    *   **Acceptance Criteria:**
        *   1. Login page is accessible via the `/login` route.
        *   2. Form contains input fields for 'Email' and 'Password', and a 'Login' button.
        *   3. Basic client-side validation for email and password presence.
        *   4. On valid submission, an API call is made to `POST /api/v1/auth/login` with email and password.
        *   5. On successful API response (200), global authentication state is updated to reflect logged-in user.
        *   6. On successful login, user is redirected to the `/videos` page.
        *   7. On API error response (e.g., 401 for invalid credentials), an appropriate error message is displayed on the login page.
        *   8. Loading state is indicated during API call.
        *   9. An `AuthContext` (or equivalent store) is created to provide authentication status and user information (if any) to the application.

*   **TASK-FE-005 (A):** Logout Functionality
    *   **Description:** Implement logout capability.
    *   **Mock API Interaction:**
        *   **Endpoint:** `DELETE /api/v1/auth/logout`
        *   **Response DTO (Success 200):** `{ message: string }`
    *   **Details:** Implement as a `Button` atom (likely in the `App Header` part of `AppLayout`). Clear auth state and redirect.
    *   **Tech Stack:** React 19.
    *   **Architecture:** Update `AuthService`, integrate with `AuthContext` and `AppLayout`.
    *   **Depends on:** TASK-FE-004 (A)
    *   **Deliverables:** Logout `Button` and functionality.
    *   **Acceptance Criteria:**
        *   1. A 'Logout' button/link is visible in the application layout when a user is authenticated.
        *   2. Clicking 'Logout' triggers an API call to `DELETE /api/v1/auth/logout`.
        *   3. On successful or unsuccessful API response, global authentication state is cleared.
        *   4. User is redirected to the `/login` page after clicking 'Logout'.
        *   5. The 'Logout' button/link is not visible when no user is authenticated.

---

## Developer B: Video Core & Display

**Focus:** Displaying video information, using components like `Video Card`, `Pagination Control`, and integrating status displays into the `App Header`.

*   **TASK-FE-006 (B):** Display YouTube Connection Status
    *   **Description:** Create a UI component to display the status of the YouTube API connection.
    *   **Mock API Interaction:**
        *   **Endpoint:** `GET /api/v1/youtube/connection_status`
        *   **Request DTO:** None (Authenticated request)
        *   **Response DTO (Success 200):** `{ connected: boolean, channel_name?: string }`
        *   **Response DTO (Error 503):** `{ error: string }`
    *   **Details:** Display connection status. Component to be integrated into `App Header` (from `AppLayout`).
    *   **Tech Stack:** React 19, Tailwind CSS.
    *   **Architecture:** `ConnectionStatusDisplay` (molecule or part of `App Header` organism), `YouTubeService`.
    *   **Depends on:** TASK-FE-001 (A), TASK-FE-004 (A) (for auth context to make authenticated call)
    *   **Deliverables:** Component displaying connection status, integrated into `AppLayout`.
    *   **Acceptance Criteria:**
        *   1. When an authenticated user is on a relevant page (e.g., main dashboard/layout), an API call is made to `GET /api/v1/youtube/connection_status`.
        *   2. If API returns `{ connected: true, channel_name: "Test Channel" }`, UI displays "Connected to Test Channel" (or similar).
        *   3. If API returns `{ connected: false }`, UI displays "Not connected to YouTube" (or similar).
        *   4. If API call fails or returns an error, an appropriate error message or status is shown (e.g., "Could not retrieve YouTube connection status").
        *   5. Loading state is shown while fetching connection status.
        *   6. Component is present in the application layout (e.g., header) for authenticated users.

*   **TASK-FE-007 (B):** List Videos Page
    *   **Description:** Create a page to display a list of videos from the user's YouTube channel.
    *   **Mock API Interaction:**
        *   **Endpoint:** `GET /api/v1/videos`
        *   **Request DTO:** Optional query params: `page?: number`, `per_page?: number` (Authenticated request)
        *   **Response DTO (Success 200):** `{ videos: VideoObjectShort[], pagination: { current_page: number, total_pages: number, total_count: number } }`
            *   `VideoObjectShort`: `{ id: string, title: string, thumbnail_url: string, views: number, published_at: string }`
        *   **Response DTO (Error 500/503):** `{ error: string }`
    *   **Details:** Use `Video Card / List Item` components for each video within a `Video List/Grid` organism. Implement `Pagination Control` molecule.
    *   **Tech Stack:** React 19, Tailwind CSS, React Router.
    *   **Architecture:** `VideoListPage` (page template), `VideoList` (organism), `VideoListItem` (organism/molecule), `PaginationControl` (molecule), `VideoService`.
    *   **Depends on:** TASK-FE-001 (A), TASK-FE-002 (A), TASK-FE-004 (A)
    *   **Deliverables:** Video list page with specified components.
    *   **Acceptance Criteria:**
        *   1. Navigating to `/videos` (when authenticated) displays the Video List Page.
        *   2. An API call to `GET /api/v1/videos` is made to fetch the first page of videos.
        *   3. For each video in the response, a `Video Card / List Item` displays: thumbnail, title, views, and publication date.
        *   4. If no videos are returned, a message "No videos found" is displayed.
        *   5. `Pagination Control` is visible if `total_pages` > 1.
        *   6. Clicking a 'Next Page' button on `Pagination Control` fetches and displays the next set of videos.
        *   7. Clicking a 'Previous Page' button on `Pagination Control` fetches and displays the previous set of videos.
        *   8. Clicking on a video title or thumbnail within `Video Card / List Item` navigates the user to the Video Details Page for that video (e.g., `/videos/:youtube_video_id`).
        *   9. Loading state (e.g., skeleton screen or `Spinner/Loader`) is shown while videos are being fetched.
        *   10. API errors are gracefully handled and a user-friendly message is shown (e.g. via `Notification/Toast`).

*   **TASK-FE-008 (B):** View Video Details Page
    *   **Description:** Create a page to display detailed information for a specific video.
    *   **Mock API Interaction:**
        *   **Endpoint:** `GET /api/v1/videos/:youtube_video_id`
        *   **Request DTO:** None (Authenticated request, `youtube_video_id` from URL param)
        *   **Response DTO (Success 200):** `VideoObjectFull`
            *   `VideoObjectFull`: `{ id: string, title: string, description: string, tags: string[], category: string, privacy_status: string, statistics: { likes: number, comments: number }, thumbnail_url: string, published_at: string }` (Extend based on actual API response)
        *   **Response DTO (Error 404):** `{ error: string }`
        *   **Response DTO (Error 500/503):** `{ error: string }`
    *   **Details:** Use `Video Detail Display` organism. Provide `Button` atoms for edit/delete actions.
    *   **Tech Stack:** React 19, Tailwind CSS, React Router.
    *   **Architecture:** `VideoDetailPage` (page template), `VideoDetailDisplay` (organism), `VideoService`.
    *   **Depends on:** TASK-FE-007 (B), TASK-FE-002 (A)
    *   **Deliverables:** Video detail page with specified components.
    *   **Acceptance Criteria:**
        *   1. Navigating to `/videos/:youtube_video_id` (when authenticated) displays the Video Details Page.
        *   2. An API call to `GET /api/v1/videos/:youtube_video_id` is made, using the ID from the URL.
        *   3. The `Video Detail Display` organism shows: video title, description, tags (if any), category, privacy status, statistics (likes, comments), thumbnail, and publication date.
        *   4. An 'Edit Video' `Button` is present, navigating to `/videos/:youtube_video_id/edit`.
        *   5. A 'Delete Video' `Button` is present (deletion confirmation/logic by Dev C).
        *   6. If the video ID is not found (404 from API), a "Video not found" message is displayed.
        *   7. Loading state (e.g. `Spinner/Loader`) is shown while video details are being fetched.
        *   8. API errors (non-404) are gracefully handled (e.g. via `Notification/Toast`).

---

## Developer C: Video Interaction & General UX

**Focus:** Implementing interactive video management features using `Video Metadata Form`, `Confirmation Modal`, and leading General UX components like `Notification/Toast` and `Spinner/Loader`.

*   **TASK-FE-009 (C):** Edit Video Metadata Page/Modal
    *   **Description:** Create a UI for editing a video's metadata.
    *   **Mock API Interaction:**
        *   **Endpoint:** `PUT /api/v1/videos/:youtube_video_id`
        *   **Request DTO:** `{ title?: string, description?: string, tags?: string[], category_id?: string, privacy_status?: string }` (Authenticated request, `youtube_video_id` from URL param)
        *   **Response DTO (Success 200):** `VideoObjectFull` (updated)
        *   **Response DTO (Error 400/404/500/503):** `{ error: string }`
    *   **Details:** Implement as `EditVideoPage` (page template) or `EditVideoModal` (organism), containing the `Video Metadata Form` organism. Use `Button` atoms for submit/cancel.
    *   **Tech Stack:** React 19, Tailwind CSS.
    *   **Architecture:** `EditVideoPage` or `EditVideoModal`, `VideoMetadataForm` (organism), `VideoService`. Utilizes `Input`, `Label`, `Button` atoms.
    *   **Depends on:** TASK-FE-008 (B), TASK-FE-002 (A), TASK-FE-013 (C)
    *   **Deliverables:** UI and functionality for editing, using specified components.
    *   **Acceptance Criteria:**
        *   1. Navigating to `/videos/:youtube_video_id/edit` (or triggering edit modal from detail page) displays the `Video Metadata Form`.
        *   2. Form is pre-filled with current video metadata.
        *   3. User can modify form fields.
        *   4. On submission with the submit `Button`, an API call is made.
        *   5. On successful API response (200), a success `Notification/Toast` is displayed.
        *   6. User is redirected to the Video Details Page or modal closes and detail page refreshes.
        *   7. API errors are handled and displayed via `Notification/Toast`.
        *   8. Loading state (`Spinner/Loader` on `Button`) is indicated during form submission.
        *   9. A 'Cancel' `Button` redirects or closes modal without saving.

*   **TASK-FE-010 (C):** Upload New Video Page/Modal
    *   **Description:** Create a UI for uploading a new video.
    *   **Mock API Interaction:**
        *   **Endpoint:** `POST /api/v1/videos`
        *   **Request DTO:** `FormData` containing video file and metadata fields: `title: string, description: string, tags: string[], category_id: string, privacy_status: string` (Authenticated request)
        *   **Response DTO (Success 201):** `VideoObjectFull` (newly uploaded)
        *   **Response DTO (Error 400/500/503):** `{ error: string }`
    *   **Details:** Implement as `UploadVideoPage` (page template) or `UploadVideoModal` (organism), containing the `Video Metadata Form` (adapted for upload, including file `Input` atom).
    *   **Tech Stack:** React 19, Tailwind CSS.
    *   **Architecture:** `UploadVideoPage` or `UploadVideoModal`, `VideoMetadataForm` (organism), `VideoService`. Utilizes file `Input` atom.
    *   **Depends on:** TASK-FE-001 (A), TASK-FE-002 (A), TASK-FE-004 (A), TASK-FE-013 (C)
    *   **Deliverables:** UI and functionality for uploading, using specified components.
    *   **Acceptance Criteria:**
        *   1. An 'Upload Video' `Button` is available.
        *   2. Clicking it navigates to `/upload` page or opens an upload modal containing `Video Metadata Form`.
        *   3. Form contains: file `Input` for video, text inputs for metadata.
        *   4. Client-side validation for required fields.
        *   5. On submission, a `FormData` API call is made.
        *   6. On successful API response (201), a success `Notification/Toast` is displayed.
        *   7. User is redirected.
        *   8. API errors are handled and displayed via `Notification/Toast`.
        *   9. File upload progress is visually indicated if possible.
        *   10. Loading state (`Spinner/Loader` on `Button`, progress bar) is clearly indicated.

*   **TASK-FE-011 (C):** Delete Video Functionality (with Confirmation)
    *   **Description:** Implement functionality to delete a video, including a confirmation step.
    *   **Mock API Interaction:**
        *   **Endpoint:** `DELETE /api/v1/videos/:youtube_video_id`
        *   **Request DTO:** None (Authenticated request, `youtube_video_id` from context)
        *   **Response DTO (Success 204):** No content
        *   **Response DTO (Error 404/500/503):** `{ error: string }`
    *   **Details:** Use a `ConfirmationModal` organism. Triggered by a `Button` atom.
    *   **Tech Stack:** React 19.
    *   **Architecture:** `ConfirmationModal` (organism, potentially reusable from `src/components/common`), update `VideoService`. Integrated into `VideoDetailPage` and/or `VideoListItem`.
    *   **Depends on:** TASK-FE-007 (B), TASK-FE-008 (B), TASK-FE-013 (C)
    *   **Deliverables:** Delete video functionality with `ConfirmationModal`.
    *   **Acceptance Criteria:**
        *   1. 'Delete Video' `Button` is functional.
        *   2. Clicking 'Delete Video' opens a `ConfirmationModal`.
        *   3. Modal has 'Confirm Delete' and 'Cancel' `Button`s.
        *   4. Clicking 'Cancel' closes the modal.
        *   5. Clicking 'Confirm Delete' makes an API call.
        *   6. On successful API response (204), a success `Notification/Toast` is displayed.
        *   7. The video is removed from the UI.
        *   8. API errors are handled and displayed via `Notification/Toast`.
        *   9. Loading state (`Spinner/Loader` on `Button`) indicated during deletion.

*   **TASK-FE-012 (C):** Responsive Design Implementation
    *   **Description:** Ensure the application is usable across different screen sizes by applying Tailwind CSS responsive utilities as per `UI_SYSTEM_DESIGN.md`.
    *   **Tech Stack:** Tailwind CSS.
    *   **Applies to:** All UI components developed by A, B, and C. Dev C takes the lead in establishing patterns and reviewing.
    *   **Deliverables:** Responsive UI across the application.
    *   **Acceptance Criteria:**
        *   1. All pages and key interactive elements (forms, video lists, modals) are usable and visually well-organized on desktop (e.g., >1024px), tablet (e.g., ~768px), and mobile (e.g., ~375px) screen widths.
        *   2. Navigation menus adapt appropriately (e.g., hamburger menu on mobile).
        *   3. Content does not overflow horizontally on smaller screens.
        *   4. Touch targets are appropriately sized on mobile.
        *   5. Readability is maintained across screen sizes.

*   **TASK-FE-013 (C):** Error Handling and Notifications System
    *   **Description:** Implement a user-friendly way to display global errors and success messages using `Notification/Toast` molecules.
    *   **Tech Stack:** React 19.
    *   **Architecture:** Global `NotificationContext` or service. Reusable `Notification/Toast` (molecule) from `src/components/common`.
    *   **Depends on:** TASK-FE-001 (A)
    *   **Deliverables:** System for `Notification/Toast` messages.
    *   **Acceptance Criteria:**
        *   1. A global `Notification/Toast` system is implemented.
        *   2. API errors trigger a global error `Notification/Toast`.
        *   3. Success messages for key operations are displayed as `Notification/Toast` messages.
        *   4. Notifications are dismissible.
        *   5. Notifications are styled consistently and are non-obtrusive.

*   **TASK-FE-014 (C):** Loading States Implementation
    *   **Description:** Provide visual feedback (`Spinner/Loader` atoms, skeleton screens) during API calls or long-running operations.
    *   **Tech Stack:** React 19, Tailwind CSS.
    *   **Applies to:** All components making API calls. Dev C takes lead in establishing patterns for `Spinner/Loader` usage.
    *   **Deliverables:** Consistent loading state indicators using `Spinner/Loader` atoms.
    *   **Acceptance Criteria:**
        *   1. Global loading indicator (e.g., top progress bar) is shown if applicable.
        *   2. Component-level `Spinner/Loader` atoms or skeleton elements are implemented for specified loading scenarios.
        *   3. `Spinner/Loader` indicators are clearly visible and correctly represent the busy state.

*   **TASK-FE-015 (C):** Basic Accessibility (A11y) Review
    *   **Description:** Follow basic accessibility best practices as outlined in `UI_SYSTEM_DESIGN.md`.
    *   **Tech Stack:** N/A.
    *   **Applies to:** All UI components. Dev C takes lead on A11y review and guidance.
    *   **Deliverables:** Improved accessibility across the application.
    *   **Acceptance Criteria:**
        *   1. All interactive elements are keyboard accessible.
        *   2. Logical focus order.
        *   3. Images have appropriate `alt` attributes.
        *   4. Form inputs associated with labels.
        *   5. Basic ARIA roles and attributes used where needed.
        *   6. Automated accessibility checks report no critical errors.

---

## VI. Testing (Collaborative)

*   **TASK-FE-016 (All):** Unit Tests
    *   **Description:** Write unit tests for critical components, services, hooks, and utility functions. Each developer is responsible for tests related to their assigned tasks.
    *   **Tech Stack:** Vitest (or Jest if preferred), React Testing Library.
    *   **Architecture:** Aim for good test coverage.
    *   **Acceptance Criteria:**
        *   1. Unit tests are written for key utility functions.
        *   2. Unit tests cover primary logic within React hooks.
        *   3. Unit tests for presentational components (atoms, molecules from `UI_SYSTEM_DESIGN.md`) verify rendering based on props.
        *   4. Unit tests for service functions mock API calls and verify request/response handling.
        *   5. Test coverage meets a project-defined target (e.g., >70% for new logic).

*   **TASK-FE-017 (All):** Integration Tests
    *   **Description:** Write integration tests for key user flows (e.g., login, video upload, video list to detail). Developers collaborate on tests spanning multiple individually-developed features.
    *   **Tech Stack:** Vitest, React Testing Library.
    *   **Acceptance Criteria:**
        *   1. Integration test for successful user login flow (enter credentials into `LoginForm`, submit, redirect to `/videos`).
        *   2. Integration test for signup flow (using `SignupForm`).
        *   3. Integration test for video listing (`VideoListPage` with `VideoCard / List Item`s) and navigating to a video detail page (`VideoDetailDisplay`).
        *   4. Integration test for video upload flow (fill `VideoMetadataForm`, submit, check for success `Notification/Toast`).
        *   5. Integration test for video edit flow (using `VideoMetadataForm`).
        *   6. Integration test for video delete flow (including `ConfirmationModal`).
        *   7. Tests mock API responses appropriately to simulate real user scenarios.

## Notes on Clean Architecture and Testability for Frontend:

*   **Separation of Concerns:**
    *   **Presentation (Components):** Dumb components (atoms, molecules from `UI_SYSTEM_DESIGN.md`) for UI rendering. Smart components (organisms, page templates from `UI_SYSTEM_DESIGN.md`) for state and logic.
    *   **Application Logic (Hooks/Services/Use Cases):** Business logic, API calls, state management logic separated from components.
    *   **Domain (Entities/Types):** Clear TypeScript interfaces/types in `src/types`.
*   **Dependency Rule:** Dependencies flow inwards. UI components depend on application logic.
*   **Testability:**
    *   Components (especially atoms and molecules) testable in isolation.
    *   Application logic testable independently.
    *   Mock dependencies.
*   **State Management:**
    *   **Authentication:** Global `AuthContext`.
    *   **Feature State:** Local/page-level state.
*   **Code Reusability:** Reusable components in `src/components/common` as per `UI_SYSTEM_DESIGN.md`.

This backlog provides a structured approach for parallel development. Regular communication, code reviews, and agreement on shared interfaces/components (as defined in `UI_SYSTEM_DESIGN.md`) will be crucial for success.
