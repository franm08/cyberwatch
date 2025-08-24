// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/vendors': 'http://127.0.0.1:5000',
      '/incidents': 'http://127.0.0.1:5000',
      '/compliance': 'http://127.0.0.1:5000'
    }
  }
})