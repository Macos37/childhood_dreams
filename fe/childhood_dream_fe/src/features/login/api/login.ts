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
  return apiClient.post('/login', params);
}

export const useLogin = () => {
  return useMutation({
    mutationFn: login,
  })
}