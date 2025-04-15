// Main JavaScript file for OnlyFans AI Communication System

// Check authentication on page load
document.addEventListener('DOMContentLoaded', function() {
    // Skip auth check on login and register pages
    if (window.location.pathname === '/login' || window.location.pathname === '/register') {
        return;
    }
    
    // Check if user is logged in
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = '/login';
        return;
    }
    
    // Set up auth header for all fetch requests
    setupAuthHeader();
});

// Set up authentication header for fetch requests
function setupAuthHeader() {
    const token = localStorage.getItem('token');
    if (token) {
        // Intercept fetch to add auth header
        const originalFetch = window.fetch;
        window.fetch = function(url, options = {}) {
            // Don't add auth header for login/register endpoints
            if (!url.includes('/api/auth/login') && !url.includes('/api/auth/register')) {
                options.headers = options.headers || {};
                options.headers['Authorization'] = `Bearer ${token}`;
            }
            return originalFetch(url, options);
        };
    }
}

// Handle logout
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/login';
}

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString();
}

// Truncate text with ellipsis
function truncateText(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
}

// Show notification
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification`;
    notification.innerHTML = message;
    
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Hide and remove after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}
