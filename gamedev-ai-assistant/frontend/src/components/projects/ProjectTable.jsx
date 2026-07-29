export default function ProjectTable({projects=[]}){return <table><tbody>{projects.map(p=><tr key={p._id}><td>{p.name}</td><td>{p.engine}</td><td>{p.status}</td></tr>)}</tbody></table>}
