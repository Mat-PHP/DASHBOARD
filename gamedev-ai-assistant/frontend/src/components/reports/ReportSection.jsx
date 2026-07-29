export default function ReportSection({title,items=[]}){return <section><h4>{title}</h4><ul>{items.map(x=><li key={x}>{x}</li>)}</ul></section>}
