export interface Student {
  id: number;
  name: string;
  age: number;
}

export async function getStudents(): Promise<Student[]> {
  const response = await fetch("http://127.0.0.1:8001/student/");

  if (!response.ok) {
    throw new Error("Failed to fetch students");
  }

  return response.json();
}