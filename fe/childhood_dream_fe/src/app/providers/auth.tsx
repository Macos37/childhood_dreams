import { FC, createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";


interface IAuthContext {
  token: string;
  setToken: (token: string) => void;
  removeToken: () => void;
}

interface IAuthProvider {
  children: React.ReactNode;
}

export const AuthContext = createContext<IAuthContext>({
  token: '',
  setToken: () => {},
  removeToken: () => {},
});

export const AuthProvider: FC<IAuthProvider> = (props) => {
  const { children } = props;
  const [token, setToken] = useState<string>('');
  const removeToken = () => setToken('');

  return (
    <AuthContext.Provider value={{ token, setToken, removeToken }}>
      {children}
    </AuthContext.Provider>
  )
}

interface IAuthRoute {
  children: React.ReactNode;
}

export const AuthRoute: FC<IAuthRoute> = (props) => {
  const { children } = props;
  const { token } = useContext(AuthContext);

  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate('/login');
    }
  }, [navigate, token]);

  if (!token) {
    return null;
  }

  return (
    <>
      {children}
    </>
  )
}