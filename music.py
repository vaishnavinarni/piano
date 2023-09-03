# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:03:42 2023

@author: VAISHNAVI
"""

import streamlit as st
import pygame

# Initialize pygame
pygame.init()

# Streamlit app title
st.title("Piano Musical Keys")

# Create a sidebar for selecting musical notes
selected_note = st.sidebar.selectbox("Select a musical note", ["C#", "D#", "F#", "G#", "Bb", "C", "D", "E", "F", "G", "A", "B", "C1", "D1", "E1", "F1"])

# Define a dictionary to map musical notes to their corresponding sound files
note_to_sound = {
    "C#": "sound1.mp3",
    "D#": "sound7.mp3",
    "F#": "sound8.mp3",
    "G#": "sound6.mp3",
    "Bb": "sound5.mp3",
    "C": "sound4.mp3",
    "D": "sound10.mp3",
    "E": "sound12.mp3",
    "F": "sound13.mp3",
    "G": "sound9.mp3",
    "A": "sound2.mp3",
    "B": "sound3.mp3",
    "C1": "sound15.mp3",
    "D1": "sound16.mp3",
    "E1": "sound11.mp3",
    "F1": "sound14.mp3",
}

# Function to play a selected note
def play_selected_note():
    note = selected_note
    sound_file = note_to_sound.get(note)
    if sound_file:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

# Streamlit button to play the selected note
st.sidebar.button("Play Note", on_click=play_selected_note)

# Streamlit app footer
st.sidebar.text("Enjoy playing your music!")

