import { useQuery } from "@tanstack/react-query";
import { getStudents } from "./api/student";

function App() {
  const {
    data,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["students"],
    queryFn: getStudents,
  });

  if (isLoading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>Error fetching students!</h2>;
  }

  return (
    <div>
      <h1>Students List</h1>

      {data?.map((student) => (
        <div key={student.id}>
          <h3>{student.name}</h3>
          <p>Age: {student.age}</p>
        </div>
      ))}
    </div>
  );
}

export default App;