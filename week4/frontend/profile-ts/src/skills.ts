interface Skill {
    id: number;
    name: string;
}

let skills: Skill[] = [
    { id: 1, name: "Python" },
    { id: 2, name: "JavaScript" },
    { id: 3, name: "HTML & CSS" }
];

function addSkill(name: string): Skill[] {
    const newSkill: Skill = {
        id: skills.length + 1,
        name: name
    };
    skills.push(newSkill);
    return skills;
}

function removeSkill(id: number): Skill[] {
    skills = skills.filter(skill => skill.id !== id);
    return skills;
}
export type{Skill}
export { skills, addSkill, removeSkill };

function getById<T extends { id: number }>(list: T[], id: number): T | undefined {
    return list.find(item => item.id === id);
}

console.log(getById(skills, 2));
console.log("All skills:", skills);
console.log("After adding:", addSkill("FastAPI"));
console.log("After removing id 1:", removeSkill(1));