// (STEP 7 • Polish) Simple UI test
import '@testing-library/jest-dom/vitest'
import { render, screen } from '@testing-library/react'
import React from 'react'
import App from './App'

it('renders upgraded executive form', () => {
  render(<App />)
  expect(screen.getByText('Executive Outreach Concierge')).toBeInTheDocument()
  expect(screen.getByLabelText(/Full name/i)).toBeInTheDocument()
  expect(screen.getByPlaceholderText('talent@company.com')).toBeInTheDocument()
  expect(screen.getByText(/Recipient email \(e.g. employer, partner, investor\)/i)).toBeInTheDocument()
  expect(screen.getByRole('button', { name: /send/i })).toBeInTheDocument()
})
