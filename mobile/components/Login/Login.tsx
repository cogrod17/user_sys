import { FC, useState } from "react";
import { Modal, StyleSheet, TextInput, View, Text } from "react-native";
import { useAppContext } from "../../context";
import api from "../../utils/api";
import { User } from "../../context/User/types";
import { colors } from "../../utils/styles";
import { Button } from "../Global";

interface LoginValues {
  email: string;
  password: string;
}

export const Login: FC = () => {
  const { user } = useAppContext();
  const [values, setValues] = useState<LoginValues>({
    email: "",
    password: "",
  });

  const onChange = (newValues: object) =>
    setValues({ ...values, ...newValues });

  const onSubmit = async () => {
    const { data }: { data: User } = await api.post("/users/login", values);
    user?.actions?.setUser(data);
  };

  return (
    <Modal animationType="slide">
      <View style={styles.loginContainer}>
        <View style={styles.titleContainer}>
          <Text style={styles.title}>Login</Text>
        </View>
        <TextInput
          onChangeText={(email) => onChange({ email })}
          placeholder="Email"
          style={styles.input}
        ></TextInput>
        <TextInput
          onChangeText={(password) => onChange({ password })}
          placeholder="Password"
          style={styles.input}
        ></TextInput>
        <Button style={{ marginTop: 10 }} text="Login" onPress={onSubmit} />
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  loginContainer: {
    display: "flex",
    flex: 1,
    backgroundColor: colors.tan,
    alignItems: "center",
    justifyContent: "center",
  },
  titleContainer: {
    position: "absolute",
    top: "30%",
  },
  title: {
    fontSize: 30,
    color: colors.brown,
    textTransform: "uppercase",
    letterSpacing: 1.5,
  },
  input: {
    borderColor: colors.white,
    borderWidth: 2,
    backgroundColor: colors.white,
    margin: 10,
    padding: 12,
    borderRadius: 20,
    width: 300,
    heigth: 10,
    color: colors.black,
  },
  buttonWrap: {
    display: "flex",
    // alignItems: "flex-start",
    width: 300,
  },
  button: { flex: 1 },
});
