# Step 6 - Last steps to get the game working

1. Add some sounds

   The old arcade games used to make really annoying sounds as you played them, so, to be realistic, our version of Breakout will include some of these sounds.
   When you use sounds in a Pygame Zero project you need to create a folder called **sounds** inside the project folder, where you can store all the sound files you want the programme to use. These should be .wav format files. 

   To get the sounds you need for this game:
    i) make a folder called sounds in your project folder
   ii) look at the top of this webpage for a folder icon labelled sounds and click on the icon. It will go to a new webpage where you will see four sound files. *For each file* click on the filename then in the new webpage click on the button at the right hand side labelled Download, and save the file in your new sounds folder. (After you download one file you will need to use the back button on your browser to get back to the list of files to get the next one.)

   Now we need to write code to use these sound files.

   We will use the sound blip.wav whenever the ball hits the bat.

   - Find the line in your code where there is an if block which tests for a collision between the bat and the ball.
   - At the end of this if block add
     ```
     sounds.blip.play()
     ```
     This is the Pygame Zero command to play the file blip.wav. (Make sure you indent this code to line up with the other statement in the if block.)

   We will use the sound block.wav whenever the ball hits one of the blocks

   - Find the line in your code where there is an if block which tests for a collision between the bat and any block.

   We will use the win.wav sound when the player has won the game.

   We will use the die.wav sound when the player loses and the ball goes off the bottom of the window.


2. Speeding up the ball

3. Winning and Losing


[Go to step 7](../step07-ideas_for_improvement)