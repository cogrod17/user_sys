export interface User {
  id?: number | null;
  username?: string | null;
  bio?: string | null;
  email?: string | null;
  access_token?: string | null;
}

export interface UserContextType extends User {
  actions?: {
    setUser: (user: User) => void;
    removeUser?: () => void;
  };
}
