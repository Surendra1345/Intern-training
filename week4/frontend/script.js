
const header = document.querySelector('header');

const themeBtn = document.createElement('button');
themeBtn.id = 'theme-btn';
header.appendChild(themeBtn);

let isDark = localStorage.getItem('theme') === 'dark';

function applyTheme() {
    if (isDark) {
        document.body.classList.add('dark-mode');
        themeBtn.textContent = 'Light Mode';
    } else {
        document.body.classList.remove('dark-mode');
        themeBtn.textContent = 'Dark Mode';
    }
}

applyTheme();

themeBtn.addEventListener('click', () => {
    isDark = !isDark;
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    applyTheme();
});

const skillsSection = document.querySelector('.skills');
const skillsList = document.getElementById('skills-list');

const inputRow = document.createElement('div');
inputRow.className = 'skill-input-row';
inputRow.innerHTML = `
    <input type="text" id="skill-input" placeholder="Add a skill...">
    <button type="button" id="add-skill-btn">Add</button>
`;
skillsSection.insertBefore(inputRow, skillsList);

const skillInput = document.getElementById('skill-input');
const addSkillBtn = document.getElementById('add-skill-btn');

const savedSkills = JSON.parse(localStorage.getItem('added-skills')) || [];
savedSkills.forEach(skill => appendSkillItem(skill));

function appendSkillItem(skillText) {
    const li = document.createElement('li');

    const label = document.createElement('span');
    label.textContent = skillText;

    const removeBtn = document.createElement('span');
    removeBtn.textContent = '✕';
    removeBtn.className = 'remove-btn';
    removeBtn.title = 'Remove skill';
    removeBtn.addEventListener('click', () => {
        li.remove();
        removeFromStorage(skillText);
    });

    li.appendChild(label);
    li.appendChild(removeBtn);
    skillsList.appendChild(li);
}

function saveToStorage(skillText) {
    const existing = JSON.parse(localStorage.getItem('added-skills')) || [];
    existing.push(skillText);
    localStorage.setItem('added-skills', JSON.stringify(existing));
}

function removeFromStorage(skillText) {
    const existing = JSON.parse(localStorage.getItem('added-skills')) || [];
    const updated = existing.filter(s => s !== skillText);
    localStorage.setItem('added-skills', JSON.stringify(updated));
}

function addSkill() {
    const value = skillInput.value.trim();
    if (!value) return;

    appendSkillItem(value);
    saveToStorage(value);

    skillInput.value = '';
    skillInput.focus();
}

addSkillBtn.addEventListener('click', addSkill);
skillInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') addSkill();
});

const profileContent = document.querySelector('.profile .content');