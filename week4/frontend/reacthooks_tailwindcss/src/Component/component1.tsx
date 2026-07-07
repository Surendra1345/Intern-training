import { useState, useEffect } from "react";

function Hooks() {
  const [task, setTask] = useState("");
  const [tasks, setTasks] = useState<string[]>([]);  

  useEffect(() => {
    console.log("loaded");
  }, []);

  function addTask(e: React.FormEvent) {  
    e.preventDefault();
    if (task == "") return;
    setTasks([...tasks, task]);
    setTask("");
  }

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-3">Task Manager</h1>
      <form onSubmit={addTask} className="mb-4">
        <input
          type="text"
          placeholder="Enter task"
          value={task}
          onChange={(e) => setTask(e.target.value)}
          className="border p-2 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Add
        </button>
      </form>
      <ul>
        {tasks.map((task, index) => (
          <li key={index} className="border p-2 mb-1">
            {task}
          </li>
        ))}
      </ul>
      {tasks.length == 0 && <p className="text-gray-400">no tasks</p>}
    </div>
  );
}

export default Hooks;