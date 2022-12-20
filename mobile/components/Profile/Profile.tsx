import { View, Text } from "react-native";
import { FC, useEffect } from "react";
import { useAppContext } from "../../context";
import { Login } from "../Login";
import { UserContextType } from "../../context";
import { ModalContextType } from "../../context";

export const Profile: FC = () => {
  const { user, modal } = useAppContext();
  useCheckLogin({ user, modal });

  return (
    <View>
      <Text>Profile</Text>
      <Text>{user?.email}</Text>
    </View>
  );
};

interface Props {
  user: UserContextType;
  modal: ModalContextType;
}

const useCheckLogin = ({ user, modal }: Props): void => {
  useEffect(() => {
    if (!user?.id) modal?.actions?.open(<Login />);
  }, []);
};
