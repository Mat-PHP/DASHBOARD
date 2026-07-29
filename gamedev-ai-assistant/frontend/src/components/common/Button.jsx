export default function Button({children,variant='',...props}){return <button className={`button ${variant}`} {...props}>{children}</button>}
