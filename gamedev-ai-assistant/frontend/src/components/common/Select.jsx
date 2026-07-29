export default function Select({label,children,...p}){return <label>{label}<select {...p}>{children}</select></label>}
