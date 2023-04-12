/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./core/templates/*.html'],
  prefix: "tw-",
  important: true,
  theme: {
    extend: {},
  },
  corePlugins:{
    preflight: false,
  },
  plugins: [],
}

