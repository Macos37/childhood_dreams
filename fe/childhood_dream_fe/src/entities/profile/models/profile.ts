export interface IProfile {
  id: number;
  name: string;
  surname: string;
  email: string | null;
  phone: string;
  cityId: number | null;
  city: string | null;
  photo: string | null;
  createdAt: string;
}