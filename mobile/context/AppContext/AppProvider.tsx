import { FC, useContext } from "react";
import { UserContext, UserProvider } from "../User";
import { UserContextType, User } from "../User/types";
import combineComponents, { Props } from "./combine";

export const useAppContext = () => ({
  user: useContext(UserContext),
});

export const AppProvider: FC<Props> = combineComponents([UserProvider]);
