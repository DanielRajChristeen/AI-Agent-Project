import os

class BackendAgent:
    def create_api(self, brief: str):
        os.makedirs("outputs/backend_output", exist_ok=True)
        api_code = """
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
"""
        with open("outputs/backend_output/server.js", "w", encoding="utf-8") as f:
            f.write(api_code)
        return "✅ Express API generated at outputs/backend_output/server.js"
