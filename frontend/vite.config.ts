// (STEP 1 • Contract) Dev server + proxy to backend
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://localhost:5001',
    },
  },
  test: {
    environment: 'jsdom',
    globals: true, // ✅ Add this line
  },
})
