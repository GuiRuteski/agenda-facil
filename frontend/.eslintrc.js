module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
  ],
  parserOptions: {
    requireConfigFile: false // ← ESSA LINHA resolve o erro!
  },
  rules: {
    'no-console': 'off',
    'no-debugger': 'off',
  }
}
