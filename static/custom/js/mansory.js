
var masonry = document.querySelector('.js-mm-masonry')
var column = document.getElementById('column')
var gap = document.getElementById('gap')

column.addEventListener('input', () => {
  masonry.style.setProperty('--col-width', column.value)
})

gap.addEventListener('input', () => {
  masonry.style.setProperty('--gap', gap.value)
})