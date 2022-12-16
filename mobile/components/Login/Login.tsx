import { FC, useEffect, useState } from "react";
import { Button, Modal, StyleSheet, TextInput, View } from "react-native";
import { screens } from "../../utils";
import { useNavigation } from "@react-navigation/native";
import { Nav } from "../../utils/types";
import { useAppContext } from "../../context";

interface LoginValues {
  email: string;
  password: string;
}

export const Login: FC = () => {
  const nav = useNavigation<Nav>();
  const [values, setValues] = useState<LoginValues>({
    email: "",
    password: "",
  });
  const {
    user,
    user: { setUser },
  } = useAppContext();

  const onChange = (newValues: object) =>
    setValues({ ...values, ...newValues });

  const onSubmit = async () => {
    const body = JSON.stringify(values);

    const res = await fetch("http://localhost:8000/users/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body,
    });
    let json = await res.json();

    setUser(json);
  };

  useEffect(() => {
    console.log("------------");
    console.log(user);
    console.log("------------");
  }, [user]);

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
