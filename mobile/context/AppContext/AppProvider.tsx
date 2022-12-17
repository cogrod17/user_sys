import { FC, useContext } from "react";
import { UserContext, UserProvider } from "../User";
import { ModalContext, ModalProvider } from "../Modal";
import combineComponents, { Props } from "./combine";

export const useAppContext = () => ({
  user: useContext(UserContext),
  modal: useContext(ModalContext),
});

export const AppProvider: FC<Props> = combineComponents([
  UserProvider,
  ModalProvider,
]);
