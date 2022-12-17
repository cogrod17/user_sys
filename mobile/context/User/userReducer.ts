import { useReducer } from "react";
import { User, UserContextType } from "./types";
import { initUser } from "./UserContext";

export enum UserActions {
  SET_USER = "SET_USER",
  REMOVE_USER = "REMOVE_USER",
}

interface UserAction {
  type: UserActions;
  payload: User;
}

export default (state: User | null, { type, payload }: UserAction): User => {
  switch (type) {
    case UserActions.SET_USER:
      return { ...payload };
    case UserActions.REMOVE_USER:
      return initUser;
  }
};
