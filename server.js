
import express from 'express';
const app = express();
app.use(express.json());

let tasks = [{ id: 1, title: 'Sample Task' }];

app.get('/tasks', (req, res) => {
  res.json(tasks);
});

app.post('/tasks', (req, res) => {
  const newTask = { id: tasks.length + 1, title: req.body.title };
  tasks.push(newTask);
  res.json(newTask);
});

app.listen(3000, () => console.log('🚀 API running on port 3000'));
