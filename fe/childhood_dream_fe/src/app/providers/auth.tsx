import { FC, createContext, useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { apiClient } from "@/shared/api/base";
import { queryClient } from "@/shared/api/query-client";
import { useProfile } from "@/entities/profile/api/get_profile";

interface IAuthContext {
  isAuthenticated: boolean;
  logout: () => void;
}

export const AuthContext = createContext<IAuthContext>({
  isAuthenticated: false,
  logout: () => {},
});

export const AuthProvider: FC<{children: React.ReactNode}> = ({children}) => {
  const { data: profile, isError, isLoading } = useProfile();
  const isAuthenticated = Boolean(profile && !isError);

  const logout = async () => {
    await apiClient.post('/api/v1/logout', {});
    queryClient.clear();
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <AuthContext.Provider value={{ isAuthenticated, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const ProtectedRoute: FC<{children: React.ReactNode}> = ({children}) => {
  const { isAuthenticated } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    console.log('isAuthenticated', isAuthenticated);
    if (!isAuthenticated) {
      navigate('/login');
    }
  }, [isAuthenticated, navigate]);

  return isAuthenticated ? <>{children}</> : null;
};