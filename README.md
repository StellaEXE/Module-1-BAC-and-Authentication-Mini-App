# Module-1-BAC-and-Authentication-Mini-App
This project demonstrates the core concepts of Authentication (knowing who a user is) and Authorization (knowing what the user is allowed to do).

### How it works
- **Authentication**: We simulate a logged-in user by searching their name in a hardcoded dictionary.
- **Authorization**:  A Python decorator `@requires_role` acts as a gatekeeper. This decorator checks the user's role against the required role for the function. If they do not match, the action is blocked.

### CIA Triad: Confidentiality
This app specifically demonstrates **Confidentiality**. By restricting the `delete_database` and `view_dashboard` functions to specific roles, we ensure that sensitive actions and information are only accessible to authorized parties. This prevents unauthorized users from "seeing" or interacting with data they shouldn't have access to.
