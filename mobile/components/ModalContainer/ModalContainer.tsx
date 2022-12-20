import { FC, useContext } from "react";
import { Modal } from "react-native";
import { ModalContext } from "../../context/Modal";

export const ModalContainer: FC = () => {
  const { Component, isOpen } = useContext(ModalContext);

  return isOpen ? <Modal animationType="slide">{Component}</Modal> : null;
};
