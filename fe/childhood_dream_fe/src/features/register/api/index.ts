import { apiClient } from "@/shared/api/base";
import { useMutation } from "@tanstack/react-query";

interface ISignUpParams {
  name: string;
  surname: string;
  email: string;
  phone: string;
  password: string;
}

const signUp = async (params: ISignUpParams) => {
  return await apiClient.post('/api/v1/register', params);
}

export const useSignUp = () => {
  return useMutation({
    mutationFn: signUp,
  })
}