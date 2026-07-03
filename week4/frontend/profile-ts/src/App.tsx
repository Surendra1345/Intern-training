import { skills, addSkill } from "./skills";

function App() {
    console.log(skills);
    console.log(addSkill("FastAPI"));

    return (
        <div>
            <h1>My Skills</h1>
            <ul>
                {skills.map(skill => (
                    <li key={skill.id}>{skill.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;