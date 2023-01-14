import 'react-native-gesture-handler';
//import { createStackNavigator } from '@react-navigation/stack';
//import { NavigationContainer } from '@react-navigation/native'; 
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, Pressable} from 'react-native';
import React, {useState} from 'react';
import HomePage from './screens/Home/home';




export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}> Welcome to "Project" </Text>
    <Text style={styles.baseText}> Made for and by hungry college students, 
    this app will solve your cooking problems by helping you choose what to cook! </Text>

    <Pressable style= {styles.button}>
        <Text style= {styles.innerText}> Let's Get Started</Text>
    </Pressable>
      <StatusBar style="auto"> </StatusBar>
     </View>

   // <HomePage/>

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
