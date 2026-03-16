# Simple Simulation of RBAC (Role-Based Access Control)

# 1. Login Simulation (Hardcoded Users)
USERS = {
    "alice": "admin",
    "bob": "user"
}

# Current session (Change this to "bob" to see access change)
current_user = "alice"
current_role = USERS.get(current_user)

# 2. Access Control Logic (The Gatekeeper)
def requires_role(assigned_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_role == assigned_role:
                return func(*args, **kwargs)
            else:
                return f"403 Forbidden: {current_user} does not have {assigned_role} privileges."
        return wrapper
    return decorator

# 3. Protected Routes
@requires_role("admin")
def delete_database():
    return "Success: System records wiped by Admin."

@requires_role("user")
def view_dashboard():
    return "Success: Welcome to your personal dashboard."

# Testing the logic
print(f"Logged in as: {current_user} ({current_role})")
print(f"Action 1: {view_dashboard()}")
print(f"Action 2: {delete_database()}")
