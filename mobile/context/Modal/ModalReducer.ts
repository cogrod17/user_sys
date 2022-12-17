import { FC } from "react";
import { ModalState } from "./types";

export enum ModalActions {
  CLOSE_MODAL = "CLOSE_MODAL",
  OPEN_MODAL = "OPEN_MODAL",
}

interface ModalAction {
  type: ModalActions;
  payload: FC | null;
}

export default (
  state: ModalState,
  { type, payload }: ModalAction
): ModalState => {
  switch (type) {
    case ModalActions.CLOSE_MODAL:
      return { isOpen: false, component: null };
    case ModalActions.OPEN_MODAL:
      return { isOpen: true, component: payload };
  }
};
