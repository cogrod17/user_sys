import { useCallback, createContext, FC, useState } from "react";
import { User, UserContextType } from "./types";
import { Props } from "../AppContext/combine";

const initUser = {
  user: null,
  setUser: (user: User) => {},
  removeUser: () => {},
};

export const UserContext = createContext<UserContextType>(initUser);

export const UserProvider: FC<Props> = ({ children }) => {
  const [user, updateUser] = useState<User | null>(null);

  const setUser = useCallback(
    (newData: User) => updateUser({ ...user, ...newData }),
    [updateUser, user]
  );

  const removeUser = useCallback(() => updateUser(null), [updateUser]);

  const values: UserContextType = { user, setUser, removeUser };

  return <UserContext.Provider value={values}>{children}</UserContext.Provider>;
};

export default UserProvider;
