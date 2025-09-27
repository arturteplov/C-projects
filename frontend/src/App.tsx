// Executive-grade UI for generating polished resumes
import React, { useState } from 'react'
import './App.css'

type FormState = {
  fullName: string
  targetRole: string
  candidateEmail: string
  phone: string
  location: string
  linkedin: string
  portfolio: string
  summary: string
  skills: string
  experience: string
  projects: string
  education: string
  toEmail: string
}

const initialForm: FormState = {
  fullName: '',
  targetRole: '',
  candidateEmail: '',
  phone: '',
  location: '',
  linkedin: '',
  portfolio: '',
  summary: '',
  skills: '',
  experience: '',
  projects: '',
  education: '',
  toEmail: '',
}

type Result = { id: number; pdf?: string }

export default function App() {
  const [form, setForm] = useState<FormState>(initialForm)
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [result, setResult] = useState<Result | null>(null)
  const [error, setError] = useState<string | null>(null)

  const onFieldChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setForm(prev => ({ ...prev, [name]: value }))
  }

  const resetForm = () => {
    setForm({ ...initialForm })
    setResult(null)
    setError(null)
  }

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    setError(null)
    setResult(null)
    try {
      const res = await fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...form, sendNow: true }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data?.error || 'Request failed')
      setResult({ id: data.id, pdf: data.pdf })
    } catch (err: any) {
      setError(err.message || 'Unexpected error')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className='app-shell'>
      <header className='app-header'>
        <div className='brand-mark'>
          <span className='badge'>auto_resume_sender_v0</span>
          <h1>Send 100+ resumes fast!</h1>
        </div>
        <p>
        </p>
      </header>

      <main className='app-main'>
        <form className='form-panel' onSubmit={submit}>
          <section className='section-block'>
            <div className='section-heading'>
              <h2>Candidate Identity</h2>
              <p>These details surface in the contact rail of the resume.</p>
            </div>
            <div className='field-grid two'>
              <label className='field'>
                Full name
                <input id='fullName' name='fullName' value={form.fullName} onChange={onFieldChange} required placeholder='Taylor Cook' />
              </label>
              <label className='field'>
                Target role
                <input id='targetRole' name='targetRole' value={form.targetRole} onChange={onFieldChange} placeholder='Head of Engineering' />
              </label>
              <label className='field'>
                Candidate email
                <input id='candidateEmail' name='candidateEmail' value={form.candidateEmail} onChange={onFieldChange} placeholder='taylor@example.com' />
              </label>
              <label className='field'>
                Phone
                <input id='phone' name='phone' value={form.phone} onChange={onFieldChange} placeholder='+1 (555) 123-9876' />
              </label>
              <label className='field'>
                Location
                <input id='location' name='location' value={form.location} onChange={onFieldChange} placeholder='San Francisco, CA · Remote' />
              </label>
              <label className='field'>
                LinkedIn URL
                <input id='linkedin' name='linkedin' value={form.linkedin} onChange={onFieldChange} placeholder='https://linkedin.com/in/taylor' />
              </label>
              <label className='field'>
                Portfolio / Site
                <input id='portfolio' name='portfolio' value={form.portfolio} onChange={onFieldChange} placeholder='https://taylor.design' />
              </label>
            </div>
          </section>

          <section className='section-block'>
            <div className='section-heading'>
              <h2>Resume Narrative</h2>
              <p>Share high-signal content. Bullet items render exactly as entered.</p>
            </div>
            <div className='field-grid'>
              <label className='field'>
                Executive summary
                <textarea id='summary' name='summary' value={form.summary} onChange={onFieldChange} rows={4} placeholder='Strategic technology leader with a track record of shipping category-defining products.' />
              </label>
              <label className='field'>
                Experience highlights
                <textarea id='experience' name='experience' value={form.experience} onChange={onFieldChange} rows={5} placeholder={'- Scaled platform to 50M MAU with 99.99% uptime\n- Built and led a team of 120 engineers across 3 continents'} />
              </label>
            </div>
            <div className='field-grid two'>
              <label className='field'>
                Projects / wins
                <textarea id='projects' name='projects' value={form.projects} onChange={onFieldChange} rows={4} placeholder={'- Launched AI-powered onboarding wizard cutting time-to-value by 60%'} />
              </label>
              <label className='field'>
                Education 
                <textarea id='education' name='education' value={form.education} onChange={onFieldChange} rows={4} placeholder={'- MBA, Stanford Graduate School of Business\n- B.S. Computer Science, MIT'} />
              </label>
            </div>
            <div className='field-grid'>
              <label className='field'>
                Core skills (comma or newline separated)
                <textarea id='skills' name='skills' value={form.skills} onChange={onFieldChange} rows={3} placeholder='Product strategy, Platform architecture, M&A integration, Executive storytelling' />
              </label>
            </div>
          </section>

          <section className='section-block'>
            <div className='section-heading'>
          <h2>Delivery</h2>
          <p>Choose who requires to receive an email instanly.</p>
            </div>
            <div className='field-grid two'>
              <label className='field'>
                Recipient email (e.g. employer, partner, investor etc)
                <input id='toEmail' name='toEmail' value={form.toEmail} onChange={onFieldChange} required placeholder='talent@company.com' />
              </label>
            </div>
          </section>

          <div className='actions'>
            <button className='primary-btn' type='submit' disabled={isSubmitting}>
              {isSubmitting ? 'Sending…' : 'Send'}
            </button>
            <button className='ghost-btn' type='button' onClick={resetForm} disabled={isSubmitting}>
              Reset form
            </button>
          </div>
          <div className='status-inline'>
            {isSubmitting && <span className='status-chip pending'>Generating dossier…</span>}
            {!isSubmitting && !error && !result && <span className='status-chip idle'>Awaiting first submission.</span>}
            {error && (
              <span className='status-chip error'>
                {error}
                <button className='chip-action' type='button' onClick={() => setError(null)}>
                  dismiss
                </button>
              </span>
            )}
            {result && <span className='status-chip success'>Success!</span>}
          </div>
        </form>
      </main>

      <section className='tips-block'>
        <h3>Pro tips</h3>
        <ul>
          <li>Use bullet lines starting with “-” to control layout precision.</li>
          <li>Lead with outcomes — metrics shine in the executive template.</li>
          <li>Group core skills in short phrases; commas or newlines both work.</li>
          <li>Regenerate anytime — resumes overwrite by candidate and recipient.</li>
        </ul>
      </section>
    </div>
  )
}
