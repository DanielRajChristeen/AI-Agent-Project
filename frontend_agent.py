import os

class FrontendAgent:
    def create_ui(self, brief: str):
        os.makedirs("outputs/frontend_output", exist_ok=True)
        component_code = """
import React from 'react';

export default function TaskManager() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Task Manager</h1>
      <button style={{ backgroundColor: '#007bff', color: 'white', padding: 10, borderRadius: 5 }}>
        Add Task
      </button>
    </div>
  );
}
"""
        with open("outputs/frontend_output/TaskManager.jsx", "w", encoding="utf-8") as f:
            f.write(component_code)
        return "✅ React UI component generated at outputs/frontend_output/TaskManager.jsx"
