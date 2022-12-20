import { createContext, FC, ReactNode, useMemo, useReducer } from "react";
import ModalReducer, { ModalActions } from "./ModalReducer";
import { ModalContextType } from "./types";
import { Props } from "../AppContext/combine";

const initModal = {
  isOpen: false,
  Component: null,
};

export const ModalContext = createContext<ModalContextType>({
  ...initModal,
});

export const ModalProvider: FC<Props> = ({ children }) => {
  const [modal, dispatch] = useReducer(ModalReducer, initModal);

  const actions = useMemo(
    () => ({
      open: (Component: ReactNode): void =>
        dispatch({ type: ModalActions.OPEN_MODAL, payload: Component }),
      close: () => dispatch({ type: ModalActions.CLOSE_MODAL, payload: null }),
    }),
    [dispatch]
  );

  return (
    <ModalContext.Provider value={{ ...modal, actions }}>
      {children}
    </ModalContext.Provider>
  );
};
