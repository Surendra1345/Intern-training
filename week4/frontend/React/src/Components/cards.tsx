interface CardProps {
    Name: string
    Role: string
    Company:string
}

function Card({ Name, Role,Company }: CardProps) {
    return (
        <div style={{
            border: "1px solid #ddd",
            borderRadius: "6px",
            padding: "10px",
            marginBottom: "10px",
            backgroundColor: "white"
        }}>
            <h3>{Name}</h3>
            <p>{Role}</p>
            <p>{Company}</p>
        </div>
    )
}

export default Card