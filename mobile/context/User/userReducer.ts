import { User } from "./types";

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
      return {
        id: null,
        username: null,
        bio: null,
        email: null,
        access_token: null,
      };
  }
};
