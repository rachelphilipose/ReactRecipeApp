import 'react-native-gesture-handler';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native'; 
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, Pressable} from 'react-native';
import React, {useState} from 'react';
import HomePage from './screens/Home/home';
//import { ApplicationProvider, theme } from 'bulma-native';


const Stack = createStackNavigator();

function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}> Welcome to "Project" </Text>
    <Text style={styles.baseText}> Made for and by hungry college students, 
    this app will solve your cooking problems by helping you choose what to cook! </Text>

    <Pressable style= {styles.button} 
    onPress={() => navigation.navigate('InputOutput')} >
        <Text style= {styles.innerText}> Let's Get Started</Text>
    </Pressable>



      <StatusBar style="auto"> </StatusBar>
     </View>

  );
}

function InputOutput() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}> Input and Finished Recipie will go here!! </Text>
      <StatusBar style="auto"> </StatusBar>
     </View>

  );
}

function MyStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="InputOutput" component={InputOutput} />

    </Stack.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <MyStack />
    </NavigationContainer>
  );
}





const styles = StyleSheet.create({
  button: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 4,
    elevation: 3,
    backgroundColor: 'black',
  },
  titleText: {
    color: 'red',
    fontSize: 30,
    fontFamily: 'serif',
  },
  baseText: {
    color: 'grey',
    fontSize: 15,
  },
  innerText: {
    color: 'white',
    fontFamily: 'serif',
  },
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
