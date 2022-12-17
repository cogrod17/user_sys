import { createContext, FC, Reducer, useMemo, useReducer } from "react";
import { User, UserContextType } from "./types";
import { Props } from "../AppContext/combine";
import userReducer, { UserActions } from "./userReducer";

export const UserContext = createContext<UserContextType | null>(null);

export const initUser = {
  id: null,
  username: null,
  bio: null,
  email: null,
  access_token: null,
};

export const UserProvider: FC<Props> = ({ children }) => {
  const [user, dispatch] = useReducer(userReducer, initUser);

  const actions = useMemo(
    () => ({
      setUser: (newData: User) =>
        dispatch({ type: UserActions.SET_USER, payload: newData }),
    }),
    [dispatch]
  );

  const values: UserContextType = { user, actions };

  return <UserContext.Provider value={values}>{children}</UserContext.Provider>;
};

export default UserProvider;
