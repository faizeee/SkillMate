import {useState} from "react"
import { useNavigate } from "@tanstack/react-router"
import { useAuthStore } from "../store/useAuthStore"
import { toast } from "sonner";

export default function LoginPage () {
    const [username,setUsername] = useState("");
    const [password,setPassword] = useState("");
    const [error,setError] = useState("");
    const navigate = useNavigate();
    const login = useAuthStore((state)=>state.login);
    const handelSubmit  = async (e : React.FormEvent) => {
        e.preventDefault()
        try {
            await login({username,password}).then(()=>{
                navigate({to:"/"})
                console.info("loggedin, Redirecting to home")
            }).finally(()=>{console.info("loggedin")})
        }
        catch(err:any) {
            console.error(err.message || "Login failed")
             toast.error(err.message || "Login failed")
            setError(err.message || "Login failed");
        }
    };

    return (
        <div className="max-w-md p-6 mx-auto space-y-4">
      <h1 className="text-2xl font-bold text-gray-600">🔐 Login</h1>
       {error && <p className="text-red-500">{error}</p>}
       <form onSubmit={handelSubmit} className="space-y-4">
        <input
        type="text"
        value={username}
        onChange={e => setUsername(e.target.value)}     
        className="w-full p-2 text-white bg-black border border-gray-700 rounded"
          placeholder="Username"/>
        <input
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}     
        className="w-full p-2 text-white bg-black border border-gray-700 rounded"
          placeholder="Password"/>

          <button className="w-full p-2 font-bold text-white bg-green-500 rounded hover:bg-green-700">
            Login
            </button>
       </form>
      </div>
    )
}