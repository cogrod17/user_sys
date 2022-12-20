import { FC } from "react";
import { Pressable, StyleSheet, Text } from "react-native";
import { colors } from "../../../utils/styles";

export type ButtonProps = {
  onPress: Function;
  text: string;
  style: object;
};

export const Button: FC<ButtonProps> = ({ text, onPress, style }) => {
  return (
    <Pressable
      style={({ pressed }) =>
        pressed
          ? { ...styles.pressable, ...styles.pressed, ...style }
          : { ...styles.pressable, ...style }
      }
      onPress={() => onPress()}
    >
      <Text style={styles.text}>{text}</Text>
    </Pressable>
  );
};

const styles = StyleSheet.create({
  pressable: {
    backgroundColor: colors.green,
    paddingVertical: 5,
    paddingHorizontal: 15,
    borderRadius: 5,
  },
  text: {
    color: colors.white,
    textTransform: "uppercase",
    fontWeight: "bold",
    fontSize: 17,
  },
  pressed: {
    opacity: 0.5,
  },
});
