import { FC } from "react";

export interface ModalState {
  isOpen: boolean;
  component: FC | null;
}

export type ModalContextType = {
  modal: ModalState;
  actions: {
    open: (comp: FC) => void;
    close: () => void;
  };
};
