import { Login, Profile } from "./components";
import { StatusBar } from "expo-status-bar";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { screens } from "./utils";
import { Modal } from "react-native";
import { useEffect, useState } from "react";

const { Navigator, Screen } = createNativeStackNavigator();

export default function App() {
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    setInterval(() => setShowModal(true), 3000);
  }, []);

  return (
    <>
      <StatusBar style="dark" />
      {showModal && <Login />}
      <NavigationContainer>
        <Navigator initialRouteName={screens.PROFILE}>
          {/* <Screen name={screens.LOGIN} component={Login} /> */}
          <Screen name={screens.PROFILE} component={Profile} />
        </Navigator>
      </NavigationContainer>
    </>
  );
}
