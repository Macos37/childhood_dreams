import { apiClient } from "@/shared/api/base";
import { IProfile } from "../models/profile";
import { useQuery } from "@tanstack/react-query";

const getProfile = async (): Promise<IProfile> => {
  
    return await apiClient.get('/api/v1/user/me');
};

export const useProfile = () => {
  return useQuery({
    queryKey: ['profile'],
    queryFn: getProfile,
  });
};