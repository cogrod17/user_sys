import { ReactNode } from "react";

export interface ModalState {
  isOpen: boolean;
  Component: ReactNode | null;
}

export interface ModalContextType extends ModalState {
  actions?: {
    open: (comp: ReactNode) => void;
    close: () => void;
  };
}
