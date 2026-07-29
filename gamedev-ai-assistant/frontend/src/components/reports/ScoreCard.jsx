export default function ScoreCard({label,value}){return <div className="score-card"><b>{value}</b><span>{label}</span><progress value={value} max="100"/></div>}
