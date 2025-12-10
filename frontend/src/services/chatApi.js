import config from "../config";

console.log("API BASE URL:", config.API_BASE_URL)

// Generic API call function
async function apiCall(endpoint, options = {}) {
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
    },
  }

  console.log("Calling endpoint:", endpoint)
  const response = await fetch(`${config.API_BASE_URL}${endpoint}`, {
    ...defaultOptions,
    ...options,
  })

  const contentType = response.headers.get("content-type")

  if (!response.ok) {
    const errorText = await response.text()
    console.error("API ERROR:", errorText)
    throw new Error(errorText)
  }

  if (contentType && contentType.includes("application/json")) {
    return await response.json()
  } else {
    return await response.text()
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
}

