import { apiClient } from "@/shared/api/base";
import { useMutation } from "@tanstack/react-query";

interface ILoginParams {
  phone: string;
  password: string;
}

interface ILoginResponse {
  token: string;
}


const login = async (params: ILoginParams): Promise<ILoginResponse> => {
  return await apiClient.post('/api/v1/auth', params);
}

export const useLogin = () => {
  return useMutation({
    mutationFn: login,
  })
}