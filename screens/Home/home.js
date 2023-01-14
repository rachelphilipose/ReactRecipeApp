import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import React, {useState} from 'react';

const HomePage = () => {
    <View style={styles.container}>
      <Text style={styles.titleText}> HELLO THERE</Text>
     <Text style={styles.baseText}>this is our super cool awesome app</Text>
      <StatusBar style="auto"> THIS IS THE STAT BAR</StatusBar>
    </View>
};


export default HomePage;


const styles = StyleSheet.create({
    titleText: {
      color: 'red',
      fontSize: 30,
    },
    baseText: {
      color: 'grey',
      fontSize: 15,
    },
    container: {
      flex: 1,
      backgroundColor: 'white',
      alignItems: 'center',
      justifyContent: 'center',
    },
  });



