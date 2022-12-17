export interface User {
  id?: number | null;
  username?: string | null;
  bio?: string | null;
  email?: string | null;
  access_token?: string | null;
}

export type UserContextType = {
  user: User | null;
  actions: {
    setUser: (user: User) => void;
    removeUser?: () => void;
  };
};
