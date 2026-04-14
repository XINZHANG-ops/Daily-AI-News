/**
 * AI Assistant Configuration
 *
 * This file manages the server URL for the AI assistant.
 * Update the SERVER_URL based on your deployment environment.
 *
 * NOTE: This configuration is shared with personal_page - both use the same backend.
 */

// Auto-detect environment and set appropriate URL
function getAIServerURL() {
  const hostname = window.location.hostname;

  // Local access (file:// or localhost or Mac mini itself)
  if (hostname === 'localhost' || hostname === '127.0.0.1' || hostname === '') {
    return 'http://localhost:5002/chat';
  }

  // GitHub Pages (remote access via LAN IP)
  if (hostname.includes('github.io')) {
    return 'http://10.0.0.209:5002/chat';
  }

  // LAN access from other machines
  return 'http://10.0.0.209:5002/chat';
}

// Export configuration
window.AI_SERVER_CONFIG = {
  serverUrl: getAIServerURL(),

  // Helper to update URL dynamically (useful for testing)
  setServerUrl: function(url) {
    this.serverUrl = url;
    console.log('AI Assistant: Server URL updated to', url);
  },

  // Check if we're on GitHub Pages
  isGitHubPages: function() {
    return window.location.hostname.includes('github.io');
  }
};




