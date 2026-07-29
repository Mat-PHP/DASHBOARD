export default function TaskFilters({value,onChange}){return <input className="search" value={value} onChange={e=>onChange(e.target.value)} placeholder="Filtrar tarefas..."/>}
