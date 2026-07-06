interface Item {
    id: number
    name: string
    score: number
}

function List() {
    const items: Item[] = [
        { id: 1, name: "Surendra", score: 92 },
        { id: 2, name: "Mohan", score: 45 },
        { id: 3, name: "Prasath", score: 78 },
        { id: 4, name: "Afzal", score: 38 },
        { id: 5, name: "Manvitha", score: 88 },
    ]

    return (
        <div>
            <h2>Students List</h2>
            <ul style={{ listStyle: "none", padding: 0 }}>
                {items.map(item => (
                    <li key={item.id}style={{
                            padding: "10px",
                            marginBottom: "8px",
                            borderRadius: "4px",
                            backgroundColor: item.score >= 50 ? "#d4edda" : "#f8d7da",
                            color: item.score >= 50 ? "#155724" : "#721c24"
                        }}
                    >
                        {item.name} — Score: {item.score}
                        {item.score >= 50 ? "Pass" : "Fail"}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default List