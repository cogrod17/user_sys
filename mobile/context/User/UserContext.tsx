import { createContext, FC, useMemo, useReducer } from "react";
import { User, UserContextType } from "./types";
import { Props } from "../AppContext/combine";
import userReducer, { UserActions } from "./userReducer";

export const initUser = {
  id: null,
  username: null,
  bio: null,
  email: null,
  access_token: null,
};

export const UserContext = createContext<UserContextType>({ ...initUser });

export const UserProvider: FC<Props> = ({ children }) => {
  const [user, dispatch] = useReducer(userReducer, initUser);

  const actions = useMemo(
    () => ({
      setUser: (newData: User): void =>
        dispatch({ type: UserActions.SET_USER, payload: newData }),
    }),
    [dispatch]
  );

  return (
    <UserContext.Provider value={{ ...user, actions }}>
      {children}
    </UserContext.Provider>
  );
};
