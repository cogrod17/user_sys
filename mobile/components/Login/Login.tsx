import { FC, useState } from "react";
import { Button, Modal, StyleSheet, TextInput, View } from "react-native";
import { useAppContext } from "../../context";
import api from "../../utils/api";
import { User } from "../../context/User/types";

interface LoginValues {
  email: string;
  password: string;
}

export const Login: FC = () => {
  const [values, setValues] = useState<LoginValues>({
    email: "",
    password: "",
  });
  const {
    user: { setUser },
  } = useAppContext();

  const onChange = (newValues: object) =>
    setValues({ ...values, ...newValues });

  const onSubmit = async () => {
    const { data }: { data: User } = await api.post("/users/login", values);
    setUser(data);
  };

  return (
    <Modal animationType="slide">
      <View style={styles.loginContainer}>
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

        <Button
          // style={({ pressed }) =>
          //   //dynamic styles!
          //   pressed ? { ...styles.button, opacity: 0.5 } : styles.button
          // }
          title="Login"
          onPress={onSubmit}
        />
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  loginContainer: {
    display: "flex",
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    borderColor: "red",
    borderWidth: 2,
  },
  input: {
    // borderColor: "#ccc",
    // borderWidth: 2,
    margin: 10,
    padding: 10,
    borderRadius: 10,
    width: 300,
    heigth: 10,
    color: "#fff",
    backgroundColor: "#696969",
  },
  buttonWrap: {
    display: "flex",
    // alignItems: "flex-start",
    width: 300,
  },
  button: { flex: 1 },
});
