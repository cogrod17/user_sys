import { View, Text } from "react-native";
import { FC } from "react";
import { useContext } from "react";
import { UserContext } from "../../context/User/UserContext";

export const Profile: FC = () => {
  const { user } = useContext(UserContext);

  return (
    <View>
      <Text>Profile</Text>
      <Text>{user?.email}</Text>
    </View>
  );
};
