# Simple RBAC (Role-Based Access Control) Simulation

# 1. Login Simulation (Hardcoded Users)
users = {
    "alice": {"role": "admin"},
    "bob": {"role": "user"}
}

# Current session (Change this to "bob" to see access denied)
current_user = "alice"

def requires_role(required_role):
    """Decorator to simulate access control logic."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_role = users.get(current_user, {}).get("role")
            if user_role == required_role:
                return func(*args, **kwargs)
            else:
                print(f"[-] Access Denied for {current_user}: Requires {required_role} role.")
        return wrapper
    return decorator

# 2. Protected Actions
@requires_role("admin")
def delete_database():
    print("[+] Admin Action: Database deleted successfully.")

@requires_role("user")
def view_dashboard():
    print("[+] User Action: Dashboard displayed.")

# 3. Execution
print(f"Logged in as: {current_user}")
view_dashboard()
delete_database()
