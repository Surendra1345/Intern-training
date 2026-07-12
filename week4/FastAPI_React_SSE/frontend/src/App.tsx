import { useEffect, useState } from "react";

function App() {
  const [time, setTime] = useState("");

  // Replace your current useEffect with this
  useEffect(() => {
    const eventSource = new EventSource("http://127.0.0.1:8002/clock");

    eventSource.onopen = () => {
      console.log("Connected");
    };

    eventSource.onmessage = (event) => {
      console.log("Time:", event.data);
      setTime(event.data);
    };

    eventSource.onerror = (err) => {
      console.log("Error", err);
    };

    return () => {
      eventSource.close();
    };
  }, []);

  return (
    <div
      style={{
        textAlign: "center",
        marginTop: "100px",
        fontFamily: "Arial",
      }}
    >
      <h1>Live Digital Clock</h1>
      <h2>{time}</h2>
    </div>
  );
}

export default App;