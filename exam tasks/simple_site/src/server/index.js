const path = require('path')
const express = require('express')
const app = express()
const PORT = 8080


app.use('/', express.static(path.join(__dirname, '..', 'client')))

app.use((req, res, next) => {
  res.status(404).sendFile(path.join(__dirname, '..', 'client', '404page.html'))
})

app.listen(PORT, () => {
  console.log(`Server run on ${PORT}`)
})
