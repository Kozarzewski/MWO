// API configuration
const API_BASE_URL = 'http://localhost:8080'

// Generic API call function
async function apiCall(endpoint, options = {}) {
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
    },
  }

  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...defaultOptions,
      ...options,
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    console.error('API call failed:', error)
    throw error
  }
}

// Specific API functions
export const chatApi = {
  sendMessage: async (message, conversationHistory = []) => {
    return apiCall('/chat', {
      method: 'POST',
      body: JSON.stringify({
        message,
        conversationHistory
      })
    })
  },

  // Add other API calls here as needed
  getHistory: async () => {
    return apiCall('/history')
  },

  clearHistory: async () => {
    return apiCall('/history', { method: 'DELETE' })
  }
}