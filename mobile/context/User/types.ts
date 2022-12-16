export interface User {
  id?: number;
  username?: string;
  bio?: string;
  email?: string;
  access_token?: string;
}

export type UserContextType = {
  user: User | null;
  setUser: (user: User) => void;
  removeUser?: () => void;
};
